from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.talk_list, name='talk-list')
]
