from django.conf.urls import include, url
from django.contrib import admin
from article import views as article_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', article_views.home, name='home'),
    url(r'^(?P<my_args>\d+)/$', article_views.detail, name='detail'),
    url(r'^test/$', article_views.test),
]
