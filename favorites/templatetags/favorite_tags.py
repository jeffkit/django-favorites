#encoding=utf-8

from favorites.models import Favorite
from django.db import models
from django import template
register = template.Library()


def favorite_count(value):
    if not isinstance(value, models.Model):
        raise ValueError('value must be a Model object')
    count = Favorite.objects.favorites_for_obj(value).count()
    return str(count)


register.filter('favorite_count', favorite_count)
