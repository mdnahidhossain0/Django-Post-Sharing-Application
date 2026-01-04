from django.urls import path
from . views import *
urlpatterns = [
    path('', TweetList, name='twitlist'),
    path('login/', Login, name='login'),
    path('signup/', Signup, name='signup'),
    path('twitcreate/', TweetCreate, name='twitcreate'),
    path('<int:tweet_id>/edit/', TweetEdit, name='twitedit'),
    path('<int:tweet_id>/delete/', TweetDelete, name='twitdelete'),
]
