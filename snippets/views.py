from django.contrib.auth.models import Group, User

from rest_any_permissions.permissions import AnyPermissions
from rest_framework import generics
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from drf_acl.models import SnippetDefaultPermission, SnippetGroupPermission, SnippetUserPermission
from drf_acl.permissions import SnippetListPermission, SnippetDetailsUserPermission, SnippetDetailsGroupPermission
from drf_acl.permissions import GroupListPermission, SnippetDetailsDefaultPermission, UserListPermission
from drf_acl.permissions import UserDetailPermission, GroupDetailPermission

from snippets.models import Snippet
from snippets.serializers import GroupSerializer, SnippetDetailsSerializer, SnippetListSerializer, UserListSerializer
from snippets.serializers import UserDetailSerializer, SnippetUserPermissionListSerializer, SnippetUserPermissionDetailSerializer
from snippets.serializers import SnippetGroupPermissionListSerializer, SnippetGroupPermissionDetailSerializer
from snippets.serializers import SnippetDefaultPermissionListSerializer, SnippetDefaultPermissionDetailSerializer


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'groups': reverse('group-list', request=request, format=format),
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })


@api_view(('GET',))
def permissions_root(request, format=None):
    return Response({
        'users': reverse('snippetuserpermission', request=request, format=format),
        'groups': reverse('snippetgrouppermission', request=request, format=format),
        'defaults': reverse('snippetdefaultpermission', request=request, format=format)
    })


class GroupList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [AnyPermissions]
    any_permission_classes = [GroupListPermission]


class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [AnyPermissions]
    any_permission_classes = [GroupDetailPermission]


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    permission_classes = (SnippetListPermission,)

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return SnippetListSerializer
        else:
            return SnippetDetailsSerializer

    def pre_save(self, obj):
        obj.owner = self.request.user

    def post_save(self, obj, created=False):
        if created:
            default_perm = SnippetDefaultPermission()
            default_perm.snippet = obj
            default_perm.save()


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetDetailsSerializer
    permission_classes = [AnyPermissions]
    any_permission_classes = [SnippetDetailsUserPermission, SnippetDetailsGroupPermission, SnippetDetailsDefaultPermission]

    def pre_save(self, obj):
        obj.owner = self.request.user


class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)
    permission_classes = [AnyPermissions]
    any_permission_classes = [SnippetDetailsUserPermission, SnippetDetailsGroupPermission, SnippetDetailsDefaultPermission]

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)


class SnippetUserPermissionList(generics.ListCreateAPIView):
    queryset = SnippetUserPermission.objects.all()
    serializer_class = SnippetUserPermissionListSerializer


class SnippetUserPermissionDetail(generics.RetrieveAPIView):
    queryset = SnippetUserPermission.objects.all()
    serializer_class = SnippetUserPermissionDetailSerializer


class SnippetGroupPermissionList(generics.ListCreateAPIView):
    queryset = SnippetGroupPermission.objects.all()
    serializer_class = SnippetGroupPermissionListSerializer


class SnippetGroupPermissionDetail(generics.RetrieveAPIView):
    queryset = SnippetGroupPermission.objects.all()
    serializer_class = SnippetGroupPermissionDetailSerializer


class SnippetDefaultPermissionList(generics.ListCreateAPIView):
    queryset = SnippetDefaultPermission.objects.all()
    serializer_class = SnippetDefaultPermissionListSerializer


class SnippetDefaultPermissionDetail(generics.RetrieveAPIView):
    queryset = SnippetDefaultPermission.objects.all()
    serializer_class = SnippetDefaultPermissionDetailSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AnyPermissions]
    any_permission_classes = [UserListPermission]

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return UserListSerializer
        else:
            return UserDetailSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [AnyPermissions]
    any_permission_classes = [UserDetailPermission]

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return UserListSerializer
        else:
            return UserDetailSerializer
