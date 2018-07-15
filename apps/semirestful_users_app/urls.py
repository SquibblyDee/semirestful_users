from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    # root goes to the index
    url(r'^$', views.users),
    url(r'new', views.new),
    url(r'(?P<id>\d+)/destroy', views.edit),
    url(r'(?P<id>\d+)/edit', views.edit),
    url(r'(?P<id>\d+)', views.show),
    url(r'create', views.create),
]