from django.urls import path, re_path
from . import views

app_name = "details"


urlpatterns = [
    re_path(r'^$', views.index, name="index"),
    re_path(r'^home/$', views.home, name="home"),
    re_path(r'^about/$', views.about, name="about"),
    re_path(r'^contact/$', views.contact, name="contact"),
    re_path(r'^frequent_question/$', views.fq, name="fq"),
    re_path(r'^privacy_policy/$', views.privacy_policy, name="privacy_policy"),


]