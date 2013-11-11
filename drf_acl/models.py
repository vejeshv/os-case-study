from django.contrib.auth.models import User
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
