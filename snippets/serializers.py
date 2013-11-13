from django.contrib.auth.models import Group, User

from rest_framework import serializers

from snippets.models import Snippet


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    user_set = serializers.HyperlinkedRelatedField(view_name='user-detail', many=True)

    class Meta:
        model = Group
        fields = ('url', 'user_set')


class SnippetDetailsSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('title', 'owner', 'url', 'highlight', 'code', 'linenos', 'language', 'style')


class SnippetListSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('title', 'owner', 'url', 'highlight', 'language')


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
