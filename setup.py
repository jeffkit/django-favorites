#!/usr/bin/env python

from setuptools import setup, find_packages
from favorites import VERSION

url="https://github.com/jeffkit/django-favorites"

long_description="favorites app for django"

setup(name="django-favorites",
      version=VERSION,
      description=long_description,
      maintainer="jeff kit",
      maintainer_email="bbmyth@gmail.com",
      url = url,
      long_description=long_description,
      packages=find_packages('.'),
     )
