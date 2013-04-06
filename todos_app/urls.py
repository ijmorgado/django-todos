from django.conf.urls import patterns, url
from todos_app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='Index'),
    url(r'^(?P<todo_id>\d+)/$', views.detail, name='Detail'),
)