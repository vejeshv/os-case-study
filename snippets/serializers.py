from django.contrib.auth.models import Group, User

from rest_framework import serializers

from snippets.models import Snippet


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('name', )


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('title', 'owner', 'url', 'highlight', 'code', 'linenos', 'language', 'style')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(view_name='snippet-detail', many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'snippets')
