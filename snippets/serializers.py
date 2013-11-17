from django.contrib.auth.models import Group, User

from rest_framework import serializers

from drf_acl.models import SnippetUserPermission, SnippetGroupPermission, SnippetDefaultPermission
from snippets.models import Snippet


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    user_set = serializers.HyperlinkedRelatedField(view_name='user-detail', many=True)

    class Meta:
        model = Group
        fields = ('url', 'name', 'user_set')


class SnippetDetailsSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(view_name='user-detail')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('title', 'owner', 'url', 'highlight', 'code', 'linenos', 'language', 'style')


class SnippetListSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(view_name='user-detail')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('title', 'owner', 'url', 'highlight', 'language')


class SnippetUserPermissionListSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.Field(source='user.username')
    snippet = serializers.Field(source='snippet.title')

    class Meta:
        model = SnippetUserPermission
        fields = ('url', 'user', 'snippet', 'get_perm', 'post_perm', 'delete_perm')


class SnippetUserPermissionDetailSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.Field(source='user.username')
    snippet = serializers.Field(source='snippet.title')

    class Meta:
        model = SnippetUserPermission
        fields = ('url', 'user', 'snippet', 'get_perm', 'post_perm', 'delete_perm')


class SnippetGroupPermissionListSerializer(serializers.HyperlinkedModelSerializer):
    group = serializers.Field(source='group.name')
    snippet = serializers.Field(source='snippet.title')

    class Meta:
        model = SnippetGroupPermission
        fields = ('url', 'group', 'snippet', 'get_perm', 'post_perm', 'delete_perm')


class SnippetGroupPermissionDetailSerializer(serializers.HyperlinkedModelSerializer):
    group = serializers.Field(source='group.name')
    snippet = serializers.Field(source='snippet.title')

    class Meta:
        model = SnippetGroupPermission
        fields = ('url', 'group', 'snippet', 'get_perm', 'post_perm', 'delete_perm')


class SnippetDefaultPermissionListSerializer(serializers.HyperlinkedModelSerializer):
    snippet = serializers.Field(source='snippet.title')

    class Meta:
        model = SnippetDefaultPermission
        fields = ('url', 'snippet', 'get_perm', 'post_perm', 'delete_perm')


class SnippetDefaultPermissionDetailSerializer(serializers.HyperlinkedModelSerializer):
    snippet = serializers.Field(source='snippet.title')

    class Meta:
        model = SnippetDefaultPermission
        fields = ('url', 'snippet', 'get_perm', 'post_perm', 'delete_perm')


class UserDetailSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(view_name='snippet-detail', many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'groups')


class UserListSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(view_name='snippet-detail', many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'snippets', 'groups')
