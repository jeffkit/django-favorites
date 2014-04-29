#django-favorites

Favorite anything in Django.

## Install

install from pypi:

	pip install django-favorites

install from source:

	git clone https://github.com:jeffkit/django-favorites.git
	cd django-favorites
	sudo python setup.py install


## Play with django

add to install app:
	
	INSTALLED_APPS = (
	....
    'favorites',
	)


## Usage

### FavoriteManager

*create_favorite(user, obj):*

connect user with any kind of django model object obj.

	from favorites.models import Favorite
	
	Favorite.objects.create_favorite(user, obj)
	
*favorites_for_obj(obj):*

	from favorites.models import Favorite
	
	book = Book.objects.get(pk=1)
	favs = Favorite.objects.favorites_for_obj(book)

*favorites_of_uer(user)*

	from favorites.models import Favorite
	
	user = User.objects.get(pk=1)
	favs = Favorite.objects.favorites_for_user(user)

### Favorite Filters & Tags

django-favorites provider a set of tags and filters. before use them, load it.
	
	<% load favorite_tags %>

#### Filters

*favorite_count*

display favorite count of obj.

	{{user|favorite_count}}

	
