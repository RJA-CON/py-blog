from django.conf.urls import url
from . import views


urlpatterns = [
	# view the blog
	url(r'^blog/$', views.post_list, name='post_list'),
	# view the full post
	url(r'^blog/post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	# write a new post
	url(r'^blog/post/new/$', views.post_new, name='post_new'),
	# edit a post
	url(r'^blog/post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	# view page of drafted posts
	url(r'^blog/drafts/$', views.post_draft_list, name='post_draft_list'),
	# publish the drafted posts
	url(r'^blog/post/(?P<pk>[0-9]+)/publish/$', views.post_publish, name='post_publish'),
	# remove post
	url(r'^blog/post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),
	# add post comment
	url(r'^blog/post/(?P<pk>[0-9]+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
	# to approve a comment
	url(r'^blog/comment/(?P<pk>[0-9]+)/approve/$', views.comment_approve, name='comment_approve'),
	# to remove a comment
	url(r'^blog/comment/(?P<pk>[0-9]+)/remove/$', views.comment_remove, name='comment_remove'),
]