from django.conf.urls import patterns, url

from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

urlpatterns = patterns('',
    url(r'^$', views.api_root),
    url(r'^groups/$', views.GroupList.as_view(), name='group-list'),
    url(r'^groups/(?P<pk>[0-9]+)/$', views.GroupDetail.as_view(), name='group-detail'),
    url(r'^snippets/$', views.SnippetList.as_view(), name='snippet-list'),
    url(r'^snippets/permissions/users/$', views.SnippetUserPermissionList.as_view(), name='snippetuserpermission'),
    url(r'^snippets/permissions/users/(?P<pk>[0-9]+)/$', views.SnippetUserPermissionDetail.as_view(), name='snippetuserpermission-detail'),
    url(r'^snippets/permissions/groups/$', views.SnippetGroupPermissionList.as_view(), name='snippetgrouppermission'),
    url(r'^snippets/permissions/groups/(?P<pk>[0-9]+)/$', views.SnippetGroupPermissionDetail.as_view(), name='snippetgrouppermission-detail'),
    url(r'^snippets/permissions/defaults/$', views.SnippetDefaultPermissionList.as_view(), name='snippetdefaultpermission'),
    url(r'^snippets/permissions/defaults/(?P<pk>[0-9]+)/$', views.SnippetDefaultPermissionDetail.as_view(), name='snippetdefaultpermission-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='snippet-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
