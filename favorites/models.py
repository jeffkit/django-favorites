#encoding=utf-8

from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext_lazy as _

if hasattr(settings, 'AUTH_USER_MODEL'):
    User = settings.AUTH_USER_MODEL
else:
    from django.contrib.auth.models import User


class FavoriteManager(models.Manager):
 
    def create_favorite(self, user, obj):
        """create Favorite for obj and user.
        """
        content_type = ContentType.objects.get_for_model(type(obj))
        favorite = Favorite(user=user, content_type=content_type,
                            object_id=obj.pk, content_object=obj)
        favorite.save()
        return favorite

    def favorites_for_obj(self, obj):
        """get favorites for specific object.
        """
        content_type = ContentType.objects.get_for_model(type(obj))
        return self.get_query_set().filter(content_type=content_type,
                                           object_id=obj.pk)

    def favorites_of_user(self, user):
        """get user's favorites item
        """
        return self.get_query_set().filter(user=user)


class Favorite(models.Model):
    user = models.ForeignKey(User)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    created_time = models.DateTimeField(auto_now_add=True)

    objects = FavoriteManager()

    class Meta:
        verbose_name = _('favorite')
        verbose_name_plural = _('favorites')
        unique_together = (('user', 'content_type', 'object_id'),)
        index_together = (('content_type', 'object_id'),)

    def __unicode__(self):
        return "%s likes %s" % (self.user, self.content_object)
