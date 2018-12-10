from django.conf.urls import url
#from django.contrib import admin
from bookmark.views import BookmarkLV, BookmarkDV


app_name= 'bookmark'

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^bookmarks/$', BookmarkLV.as_view(), name='index'),
    url(r'^bookmarks/(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail'), 
]
