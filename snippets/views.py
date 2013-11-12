from django.contrib.auth.models import User

from rest_any_permissions.permissions import AnyPermissions
from rest_framework import generics
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from drf_acl.models import SnippetDefaultPermission
from drf_acl.permissions import SnippetListPermission, SnippetDetailsUserPermission, SnippetDetailsGroupPermission
from drf_acl.permissions import SnippetDetailsDefaultPermission

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (SnippetListPermission,)

    def pre_save(self, obj):
        obj.owner = self.request.user

    def post_save(self, obj, created=False):
        if created:
            default_perm = SnippetDefaultPermission()
            default_perm.snippet = obj
            default_perm.save()


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [AnyPermissions]
    any_permission_classes = [SnippetDetailsUserPermission, SnippetDetailsGroupPermission, SnippetDetailsDefaultPermission]

    def pre_save(self, obj):
        obj.owner = self.request.user


class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
