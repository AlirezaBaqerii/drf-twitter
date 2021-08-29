from django.urls import path

from .views import TweetList, TweetDetail, ProfileList, ProfileDetail


app_name = 'api'

urlpatterns = [
    path('tweets/', TweetList.as_view()),
    path('tweets/<int:pk>/', TweetDetail.as_view()),
    path('profiles/', ProfileList.as_view()),
    path('profiles/<int:pk>/', ProfileDetail.as_view())
]