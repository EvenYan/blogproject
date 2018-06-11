import datetime

from django.db.models import Q
from django.shortcuts import render, get_object_or_404

# Create your views here.
import markdown

from blog.models import Post
from comments.models import Comment
from comments.forms import CommentForm


def index(request):
    post_list = Post.objects.all().order_by('-create_time')
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # post.body = markdown.markdown(post.body,
    #                               extensions=[
    #                                   'markdown.extensions.extra',
    #                                   'markdown.extensions.codehilite',
    #                                   'markdown.extensions.toc',
    #                               ])
    form = CommentForm()
    comment_list = post.comment_set.all()
    comment_count = post.comment_set.count()
    context = {'post': post,
               'form': form,
               'comment_list': comment_list,
               'comment_count': comment_count
               }
    return render(request, 'blog/detail.html', context)


def archive(request, year, month):
    # 方法一
    # post_list = Post.objects.filter(Q(create_time__year=year)&Q(create_time__month=month)).order_by('-create_time')
    # 方法二
    # post_list = Post.objects.filter(create_time__year=year,
    #                                 create_time__month=month,
    #                                 ).order_by('-create_time')
    # 方法三
    post_list = Post.objects.filter(Q(create_time__gt=datetime.date(2018, int(month), 1))&Q(create_time__lt=datetime.date(2018, int(month)+1,1)))
    context = {'post_list': post_list}
    print(post_list.query)
    print(year, month, post_list)
    return render(request, 'blog/index.html', context)