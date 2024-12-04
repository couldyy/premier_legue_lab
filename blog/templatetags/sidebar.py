from django import template
from blog.models import *

register = template.Library()

@register.inclusion_tag('blog/popular_posts.html')
def get_popular_posts(cnt=3):
    posts = Data.objects.order_by('-views')[:cnt]
    return {"posts": posts}
