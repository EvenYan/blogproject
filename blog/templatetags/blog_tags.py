from django.db.models import Count

from blog.models import Post, Category, Tag
from django import template


register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-create_time')[:num]


@register.simple_tag
def archive():
    return Post.objects.dates('create_time', 'month', order='DESC')


@register.simple_tag
def get_category():
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
    # return Category.objects.all()


@register.simple_tag
def get_tag():
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
