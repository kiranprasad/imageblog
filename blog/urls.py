from django.conf.urls import url

from . import views
app_name = 'blog'
urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^new/', views.newpost, name="newpost"),
	url(r'^posts/(?P<post_title>[a-z|A-Z|0-9]+)/$', views.detail, name="detail" ),
	url(r'^post/$', views.post, name="post"),
	url(r'^comment/(?P<post_title>[a-z|A-Z|0-9]+)/$', views.newcomment, name = "newcomment")
]
