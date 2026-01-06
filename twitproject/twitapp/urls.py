from django.urls import path
from . views import *
urlpatterns = [
    path('', TweetList, name='twitlist'),
    path('login/', Login, name='login'),
    path('signup/', Signup, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('profile/', Profile, name='profile'),
    path('search/', Search, name='search'),
    path('twitcreate/', TweetCreate, name='twitcreate'),
    path('<int:tweet_id>/edit/', TweetEdit, name='twitedit'),
    path('<int:tweet_id>/delete/', TweetDelete, name='twitdelete'),
    path('edit/', edit_profile, name='edit_profile')

]
