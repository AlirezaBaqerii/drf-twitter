from rest_framework import serializers

from tweet.models import Tweet
from user_profile.models import Profile

class TweetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tweet
        fields = ('id' ,'user', 'content', 'timestamp', 'is_drafted', 'is_tweeted')


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('id', 'user', 'display_name', 'bio', 'location', 'birth_date', 'is_protected_acc',)