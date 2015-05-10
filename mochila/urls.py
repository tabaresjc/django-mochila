from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^mypage', include('mypage.urls')),
    url(r'^admin/', include(admin.site.urls))
)
