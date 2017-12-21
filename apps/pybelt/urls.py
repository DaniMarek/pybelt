from django.conf.urls import url
from . import views
urlpatterns = [
  url(r'^$', views.index, name='casa'),
  url(r'^welcome$', views.welcome, name='login'),
  url(r'^comments$', views.comments, name='msg'),
]