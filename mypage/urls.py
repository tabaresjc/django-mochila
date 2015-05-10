from django.conf.urls import patterns, url
from mypage import views


urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
)
