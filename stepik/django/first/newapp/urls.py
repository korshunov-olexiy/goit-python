from django.urls import path
# from django.urls.resolvers import URLPattern
from .views import index
# from django.urls.resolvers import URLPattern

#URLPattern(path('index', index))

urlpattern = [
    path('index', index)
]
