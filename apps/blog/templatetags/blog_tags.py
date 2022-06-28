# from django.template import Library
from django.template import Library, loader, Context

from ..models import Post
 
register = Library()


@register.inclusion_tag('blog/menu_last.html')
def menu_lastposts(count):
    count = int(count)
    if not count:
        count = 4

    qs = Post.objects.all()[:count]

    context = {}
    context['list'] = qs

    return context