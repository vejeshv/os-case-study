from django.contrib.auth.models import Group, User
from django.db import models

from snippets.models import Snippet


class SnippetUserPermission(models.Model):
    """
    Per user permissions for snippets
    """

    snippet = models.ForeignKey(Snippet)
    user = models.ForeignKey(User)
    get_perm = models.BooleanField(default=False)
    post_perm = models.BooleanField(default=False)
    delete_perm = models.BooleanField(default=False)

    class Meta:
        """
        Hack to fake a composite primary key
        """
        unique_together = (('snippet', 'user'),)


class SnippetGroupPermission(models.Model):
    """
    Per group permissions for snippets
    """

    snippet = models.ForeignKey(Snippet)
    group = models.ForeignKey(Group)
    get_perm = models.BooleanField(default=False)
    post_perm = models.BooleanField(default=False)
    delete_perm = models.BooleanField(default=False)

    class Meta:
        """
        Hack to fake a composite primary key
        """
        unique_together = (('snippet', 'group'),)


class SnippetDefaultPermission(models.Model):
    """
    Defaut permission for a snippet
    """

    snippet = models.ForeignKey(Snippet, primary_key=True)
    get_perm = models.BooleanField(default=True)
    post_perm = models.BooleanField(default=False)
    delete_perm = models.BooleanField(default=False)
