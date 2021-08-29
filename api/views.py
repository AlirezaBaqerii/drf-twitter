from rest_framework import generics

from .serializers import TweetSerializer, ProfileSerializer

from tweet.models import Tweet
from user_profile.models import Profile

class TweetList(generics.ListCreateAPIView):
    """
    View for listing list of tweets
    """
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


class TweetDetail(generics.RetrieveDestroyAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer    
