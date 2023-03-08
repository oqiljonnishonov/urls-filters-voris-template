from django import template
from djangoapp.models import Category, Counts

register = template.Library()

@register.simple_tag()
def get_ctegory():
    # return Category.objects.all()
    return Counts.objects.all()