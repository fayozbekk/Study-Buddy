from django.shortcuts import render, redirect
from django.db.models import Q
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    cats = Category.objects.all()[:3]
    rms = RoomModel.objects.all()
    msgs = Message.objects.order_by('-created')[:3]
    if more := request.GET.get('more'):
        cats = Category.objects.all()

    if request.GET.get('search'):
        rms = RoomModel.objects.filter(
            Q(title__icontains=request.GET.get('search')) |
            Q(content__icontains=request.GET.get('search')) |
            Q(category__cat_name__icontains=request.GET.get('search')))
    context = {'rms': rms, 'cats': cats, 'msgs': msgs, 'cnt': rms.count()}
    return render(request, 'theme/index.html', context)


def room_detail(request, pk):
    rm = RoomModel.objects.get(id=pk)
    messages = Message.objects.filter(room_id=rm.pk).order_by('-created')
    participants = rm.participants.all()
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.user = request.user
            msg.room = rm
            msg.save()
            rm.participants.add(request.user)
            return redirect('room-detail', rm.pk)

    context = {
        'rm': rm,
        "messages": messages,
        'ptns': participants,
        'form': form,
    }
    return render(request, 'theme/room.html', context)


@login_required(login_url="login")
def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.user = request.user
            room.save()
            return redirect('home')

    context = {'form': form}
    return render(request, "theme/create-room.html", context)


@login_required(login_url="login")
def create_category(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, "room_form.html", context)


@login_required(login_url="login")
def update_room(request, pk):
    room = RoomModel.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)

        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, "theme/edit-room.html", context)


@login_required(login_url="login")
def delete_room(request, pk):
    room = RoomModel.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect('home')
    return render(request, 'theme/delete.html', {'obj': room.title})


def delete_message(request, pk):
    message = Message.objects.get(id=pk)
    if request.method == 'POST':
        message.delete()
        return redirect('room-detail', message.room.pk)
    return render(request, 'theme/delete.html', {'obj': message.message})


def categories(request):
    rms = RoomModel.objects.all()
    if s := request.GET.get('catsearch'):
        cats = Category.objects.filter(cat_name__contains=s)
    else:
        cats = Category.objects.all()
    return render(request, 'theme/topics.html', context={'cats': cats, 'cnt': rms.count()})


@login_required(login_url="login")
def create_cat(request):
    form = CategoryForm()

    if request.mathod == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'room_form.html', {'form': form})


@login_required(login_url="login")
def create_topic(request, pk):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, "room_form.html", context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,
                            username=username,
                            password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    form = UserForm()
    context = {'form': form}

    return render(request, 'theme/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


def registration_user(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'theme/signup.html', context)


def profile(request, pk):
    cats = Category.objects.all()[:3]
    user =  User.objects.get(id=pk)
    msgs = Message.objects.order_by('-created')[:3]
    rms = RoomModel.objects.filter(user_id=pk)
    context = {'user': user, 'cats': cats, 'msgs': msgs, 'rms': rms}
    return render(request, 'theme/profile.html', context)
