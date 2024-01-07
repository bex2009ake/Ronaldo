from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from .models import *
from .form import *

# Create your views here.
def index(req):
    if req.user.is_authenticated:
        author = req.user
    else:
        author = Author.objects.first()
    
    context = {
        'author': author,
        'works': Works.objects.all().filter(owner=req.user),
        'educate': Education.objects.all().filter(author=req.user),
        'experience': Experience.objects.all().filter(author=req.user),
        'award': Award.objects.all().filter(author=req.user),
    }
    return render(req,'index.html',context)


def register(req):
    if req.user.is_authenticated:
        return redirect('home') 
    if req.method == 'POST':
        form = AuthorForm(req.POST,req.FILES)
        if form.is_valid():
            user = form.save()
            login(req,user)
            return redirect('home')
    else:
        form = AuthorForm()
    return render(req,'auth/register.html',{'form':form})


def login_page(req):
    if req.method == 'POST':
        form = AuthorLoginForm(data=req.POST)
        if form.is_valid():
            user = form.get_user()
            login(req,user)
            return redirect('home')
    else:
        form = AuthorLoginForm()
    return render(req,'auth/login.html',{"form":form})


def logout_page(req):
    if not req.user.is_authenticated:
        return redirect('register') 
    logout(req)
    return redirect('register')


def work_page(req):
    if req.method == 'POST':
        form = WorkForm(req.POST,req.FILES)
        if form.is_valid():
           el = form.save(commit=False)
           el.owner = req.user
           el.save()
           return redirect('home')
    else:
        form = WorkForm()
    return render(req,'work.html',{'form':form})


def educate_page(req):
    if req.method == 'POST':
        form = EducatekForm(req.POST)
        if form.is_valid():
           el = form.save(commit=False)
           el.author = req.user
           el.save()
           return redirect('home')
    else:
        form = EducatekForm()
    return render(req,'resume.html',{'form':form,'title':'Education'})



def experience_page(req):
    if req.method == 'POST':
        form = ExperienceForm(req.POST)
        if form.is_valid():
           el = form.save(commit=False)
           el.author = req.user
           el.save()
           return redirect('home')
    else:
        form = ExperienceForm()
    return render(req,'resume.html',{'form':form,'title':'Experience'})


def award_page(req):
    if req.method == 'POST':
        form = AwardForm(req.POST)
        if form.is_valid():
           el = form.save(commit=False)
           el.author = req.user
           el.save()
           return redirect('home')
    else:
        form = AwardForm()
    return render(req,'resume.html',{'form':form,'title':'Award'})