from django.conf.urls import include, url
from django.contrib import admin
from article import views as article_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', article_views.home, name='home'),
    url(r'^(?P<id>\d+)/$', article_views.detail, name='detail'),
    url(r'^tag/(?P<tag>\w+)/$', article_views.search_tag, name = 'search_tag'),
    url(r'^archives/$', article_views.archives, name = 'archives'),
    url(r'^aboutme/$', article_views.about_me, name = 'about_me'),
    url(r'^search/$', article_views.blog_search, name = 'search'),

]
