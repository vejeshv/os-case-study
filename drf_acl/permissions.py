from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import permissions

from drf_acl.models import SnippetDefaultPermission, SnippetGroupPermission, SnippetUserPermission


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


class SnippetDetailsGroupPermission(permissions.BasePermission):
    """
    Check if any of the user's groups have permission to view snippet
    """

    def has_object_permission(self, request, view, obj):
        if type(request.user) == AnonymousUser:
            return False

        groups = request.user.groups.get_query_set()

        try:
            for group in groups:
                snip_perm = SnippetGroupPermission.objects.get(group=group, snippet=obj)
                if request.method == "GET":
                    return snip_perm.get_perm
                elif request.method == "POST":
                    return snip_perm.get_perm
                elif request.method == "DELETE":
                    return snip_perm.delete_perm
        except ObjectDoesNotExist:
            return False

        return False


class SnippetDetailsDefaultPermission(permissions.BasePermission):
    """
    Check if default permission to view snippet satisfies request
    """

    def has_object_permission(self, request, view, obj):
        if type(request.user) == AnonymousUser:
            return False

        snip_perm = SnippetDefaultPermission.objects.get(snippet=obj)
        if request.method == "GET":
            return snip_perm.get_perm
        elif request.method == "POST":
            return snip_perm.post_perm
        elif request.method == "DELETE":
            return snip_perm.delete_perm
        else:
            return False
