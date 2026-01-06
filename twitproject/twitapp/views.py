from django.http import JsonResponse
from django.shortcuts import render
from . models import *
from . forms import *
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login ,logout
from .forms import UserUpdateForm, ProfileUpdateForm

def Login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            username = User.objects.get(email=email).username
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('twitlist')

        return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


def Signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already exists'})

        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': 'Email already exists'})

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)
        return redirect('twitlist')

    return render(request, 'signup.html')

def TweetList(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'twitlist.html', {'tweets': tweets})

@login_required
def TweetCreate(request):
    if request.method== 'POST' :
       form =TweetForm(request.POST, request.FILES)
       if form.is_valid():
           tweet =form.save(commit= False)
           tweet.author = request.user
           tweet.save()
           return redirect('twitlist')
    else:
        form = TweetForm()

    return render(request,'twitcreate.html',{'form':form})


@login_required
def TweetEdit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user =request.user)
    if request.method== 'POST' :
       form =TweetForm(request.POST, request.FILES, instance=tweet)
       if form.is_valid():
           tweet =form.save(commit= False)
           tweet.author = request.user
           tweet.save()
           return redirect('twitlist')
    else:
        form = TweetForm(instance=tweet)

    return render(request,'twitedit.html',{'form':form})
@login_required
def TweetDelete(request, tweet_id):
    tweet= get_object_or_404(Tweet, pk=tweet_id, user =request.user)
    if request.method== 'POST' :
        tweet.delete()
        return redirect('twitlist')
    return render(request,'twitdelete.html',{'tweet':tweet})

def logout_view(request):
    logout(request)
    return redirect('login')

def Search(request):
    q = request.GET.get('q', '').strip()

    tweets = Tweet.objects.filter(content__icontains=q)

    payload = []
    for t in tweets:
        payload.append({
            'content': t.content,
            'author': t.author.username
        })

    return JsonResponse({
        'payload': payload
    })


def Profile(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        request.user.first_name = request.POST.get('first_name')
        request.user.last_name = request.POST.get('last_name')
        request.user.save()

    user_tweets = Tweet.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'profile.html', {'tweets': user_tweets})

def edit_profile(request):
    return render(request, 'edit_profile.html')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'edit_profile.html', context)
