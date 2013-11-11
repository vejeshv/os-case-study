from django.contrib.auth.models import AnonymousUser

from rest_framework import permissions


class SnippetListPermission(permissions.BasePermission):
    """
    Check if user has permission to list all snippets
    """

    def has_permission(self, request, view):
        if type(request.user) == AnonymousUser:
            return False
        else:
            return True
