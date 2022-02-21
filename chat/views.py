from unicodedata import name
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Room, User


def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('chat'))
    else:
        return HttpResponseRedirect(reverse('login'))

@login_required
def chat(request):
    rooms = Room.objects.order_by('name')
    return render(request, 'chat/index.html', {
        'rooms': rooms
    })

@login_required
def room(request, room_name):
    rooms = Room.objects.order_by('name')
    room = Room.objects.filter(name=room_name).first()
    return render(request, 'chat/chatroom.html', {
        'room_name': room_name,
        'rooms': rooms,
        'room': room
    })


def login_view(request):
    if request.method == 'POST':
        
        # Attempt to sign user in
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        # Check if authentication is succesfull
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return HttpResponseRedirect(request.POST.get('next'))
            else:
                return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'chat/login.html', {
                'message': 'Invalid username and/or password'
            })

    else:
        return render(request, 'chat/login.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('login')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']

        # Ensure password matches confirmation
        password = request.POST['password']
        confirmation = request.POST['confirmation']
        if password != confirmation:
            return render(request, 'chat/register.html', {
                'message': 'Passwords didn\'t match.'
            })

        # Attempt to create user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, 'chat/register.html', {
                'message': 'Username already taken.'
            })
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'chat/register.html')