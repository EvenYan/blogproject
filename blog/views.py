import datetime

from django.db.models import Q
from django.shortcuts import render, get_object_or_404

# Create your views here.
import markdown
from django.views.generic import ListView, DetailView

from blog.models import Post, Category
from comments.models import Comment
from comments.forms import CommentForm


# def index(request):
#     post_list = Post.objects.all().order_by('-create_time')
#     context = {'post_list': post_list}
#     return render(request, 'blog/index.html', context)

class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'


# def category(request, pk):
#     cate = get_object_or_404(Category, pk=pk)
#     post_list = Post.objects.filter(category=cate).order_by('-create_time')
#
#     return render(request, 'blog/index.html', context={'post_list': post_list})

class CategoryView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)


# def detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     # 阅读量+1
#     post.increase_views()
#     # post.body = markdown.markdown(post.body,
#     #                               extensions=[
#     #                                   'markdown.extensions.extra',
#     #                                   'markdown.extensions.codehilite',
#     #                                   'markdown.extensions.toc',
#     #                               ])
#     form = CommentForm()
#     comment_list = post.comment_set.all()
#     comment_count = post.comment_set.count()
#     context = {'post': post,
#                'form': form,
#                'comment_list': comment_list,
#                'comment_count': comment_count
#                }
#     return render(request, 'blog/detail.html', context)

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        response = super(PostDetailView, self).get(request, *args, **kwargs)
        self.object.increase_views()

        return response

    def get_object(self, queryset=None):
        post = super().get_object(queryset=None)
        post.body = markdown.markdown(post.body,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ])
        return post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({
            'form': form,
            'comment_list': comment_list,
        })
        return context



# def archive(request, year, month):
#     # 方法一
#     # post_list = Post.objects.filter(Q(create_time__year=year)&Q(create_time__month=month)).order_by('-create_time')
#     # 方法二
#     post_list = Post.objects.filter(create_time__year=year,
#                                     create_time__month=month,
#                                     ).order_by('-create_time')
#     # 方法三
#     # post_list = Post.objects.filter(Q(create_time__gt=datetime.date(2018, int(month), 1))&Q(create_time__lt=datetime.date(2018, int(month)+1,1)))
#     context = {'post_list': post_list}
#     print(post_list.query)
#     print(year, month, post_list)
#     return render(request, 'blog/index.html', context)

class ArchiveView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return super(ArchiveView, self).get_queryset().filter(create_time__year=year, create_time__month=month)
