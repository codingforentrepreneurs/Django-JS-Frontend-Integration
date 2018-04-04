
"""
Django 1.11 and below
from django.conf.urls import include, url as re_path
"""

# Using Django 2.0 and up
from django.urls import include, path, re_path
from django.contrib import admin

from pages.views import FrontendRenderView

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^api/products/', include("products.api.urls")),
    # re_path(r'^api/abc/', include("abc.api.urls")),
    # re_path(r'^api/cart/', include("cart.api.urls")),
]

urlpatterns += [
    # your integrate path
    re_path(r'(?P<path>.*)', FrontendRenderView.as_view(), name='home')
]
# django no longer handles 404/403/500 errors; frontend does