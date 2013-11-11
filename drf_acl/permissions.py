from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import permissions

from drf_acl.models import SnippetUserPermission


class SnippetListPermission(permissions.BasePermission):
    """
    Check if user has permission to list all snippets
    """

    def has_permission(self, request, view):
        if type(request.user) == AnonymousUser:
            return False
        else:
            return True


class SnippetDetailsUserPermission(permissions.BasePermission):
    """
    Check if user has permission to view snippet
    """

    def has_object_permission(self, request, view, obj):
        if type(request.user) == AnonymousUser:
            return False

        if request.user == obj.owner:
            return True

        try:
            snip_perm = SnippetUserPermission.objects.get(user=request.user, snippet=obj)
            if request.method == "GET":
                return snip_perm.get_perm
            elif request.method == "POST":
                return snip_perm.get_perm
            elif request.method == "DELETE":
                return snip_perm.delete_perm
            else:
                return False
        except ObjectDoesNotExist:
            return False
