from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    # root goes to the index
    url(r'^$', views.users),
    url(r'new', views.new),
    url(r'(?P<num>\d+)/edit', views.edit),
    url(r'(?P<num>\d+)', views.show),
    url(r'create', views.create),
]