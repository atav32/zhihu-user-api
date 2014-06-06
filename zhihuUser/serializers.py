from zhihuUser.models import ZhihuUser
from rest_framework import serializers

class ZhihuUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZhihuUser
        fields = ('username', 
                  'answers', 
                  'questions',
                  'edits',
                  'following',
                  'followers',
                  'views',
                  'essays',
                  'bookmarks',
                  'location')
