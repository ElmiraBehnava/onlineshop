from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'blog'

urlpatterns = [

    re_path(r'^$', views.post_list, name='post_list'),
    re_path(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<post>[-\w]+)/$', views.post_detail, name='post_detail'),
    re_path(r'^(?P<postcategory_slug>[-\w]+)/$', views.post_list, name='post_list_by_category'),

]

