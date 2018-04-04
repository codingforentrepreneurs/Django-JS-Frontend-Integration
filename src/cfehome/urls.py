
"""
Django 1.11 and below
from django.conf.urls import include, url as re_path
"""

# Using Django 2.0 and up
from django.urls import include, path, re_path
from django.contrib import admin

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^api/products/', include("products.api.urls")),
]

urlpatterns += [
    # your integrate path
]