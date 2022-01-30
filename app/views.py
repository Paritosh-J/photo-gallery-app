from django.shortcuts import render, redirect
from .models import Category, Photo
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm


def userLogin(req):
    page = 'login'
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']

        user = authenticate(req, username=username, password=password)

        if user is not None:
            login(req, user)
            return redirect('index')

    return render(req, 'base/login.html', {'page': page})


def userLogout(req):
    logout(req)
    return redirect('login')


def registerUser(req):
    page = 'register'
    form = CustomUserCreationForm()

    if req.method == 'POST':
        form = CustomUserCreationForm(req.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            if user is not None:
                login(req, user)
                return redirect('index')
    
    context = {'form':form, 'page':page}
    return render(req, 'base/login.html', context)


@login_required(login_url='login')
def index(req):
    user = req.user
    categories = Category.objects.filter(user=user)
    context = {'categories':categories, 'photos':photos}
    return render(req, 'base/index.html')


@login_required(login_url='login')
def viewPic(req, id):
    photo = Photo.objects.get(id=pk)
    return render(req, 'base/viewPic.html', {'photo':photo})


@login_required(login_url='login')
def add(req):
    user = req.user
    categories = user.category_set.all()
    if req.method == 'POST':
        data = req.POST
        images = req.FILES.getlist('images')

        if data['category'] != 'none':
            category = category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(user=user, name=data['category_new'])
        else:
            category = None

        for i in images:
            photo = Photo.objects.create(category=category, description=data['description'], image=i)
            return redirect('index')

    context = {'categories':categories}
    return render(req, 'base/add.html', context)
