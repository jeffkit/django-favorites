#encoding=utf-8

from django.test import TestCase
from django.contrib.auth.tests.utils import skipIfCustomUser
from django.contrib.auth.models import User
from favorites.models import Favorite
from favorites.templatetags.favorite_tags import favorite_count


@skipIfCustomUser
class FavoriteManagerTestCase(TestCase):

    def test_create_favorite(self):
        jeff = User.objects.create_user('jeff', 'bbmyth@gmail.com')
        vera = User.objects.create_user('vera', 'vera@test.com')

        fav = Favorite.objects.create_favorite(jeff, vera)
        self.assertEqual(1, fav.pk)

    def test_favorite_for_obj(self):
        jeff = User.objects.create_user('jeff', 'bbmyth@gmail.com')
        vinky = User.objects.create_user('vinky', 'vinky@test.com')
        vera = User.objects.create_user('vera', 'vera@test.com')

        Favorite.objects.create_favorite(jeff, vinky)
        Favorite.objects.create_favorite(vera, vinky)

        favorites = Favorite.objects.favorites_for_obj(vinky)
        self.assertEqual(2, len(favorites))

    def test_favorite_of_user(self):
        jeff = User.objects.create_user('jeff', 'bbmyth@gmail.com')
        vinky = User.objects.create_user('vinky', 'vinky@test.com')
        vera = User.objects.create_user('vera', 'vera@test.com')

        Favorite.objects.create_favorite(jeff, vinky)
        Favorite.objects.create_favorite(jeff, vera)

        favorites = Favorite.objects.favorites_of_user(jeff)

        self.assertEqual(2, len(favorites))


class FilterTestCase(TestCase):

    def test_invalid_obj(self):
        value = 'str obj'
        try:
            favorite_count(value)
        except Exception, e:
            self.assertEqual(e.__class__, ValueError)

    def test_normal_case(self):
        jeff = User.objects.create_user('jeff', 'bbmyth@gmail.com')
        vinky = User.objects.create_user('vinky', 'vinky@test.com')
        vera = User.objects.create_user('vera', 'vera@test.com')

        Favorite.objects.create_favorite(jeff, vinky)
        Favorite.objects.create_favorite(vera, vinky)

        result = favorite_count(vinky)

        self.assertEqual('2', result)
