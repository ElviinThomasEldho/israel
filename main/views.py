from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import send_mail

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import *
from .forms import *
from .decorators import *

from django.conf import settings

import hashlib
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template.context_processors import csrf
from translate import Translator
from uuid import uuid4

def indexEN(request):
    content = Content.objects.get()
    services = Service.objects.all();
    reviews = Review.objects.all();

    context = {
        'lang': "en",
        'content': content,
        'services': services,
        'reviews': reviews,
    }

    return render(request, 'main/main.html', context)

def indexHB(request):
    content = Content.objects.get()
    services = Service.objects.all();
    reviews = Review.objects.all();

    translator= Translator(to_lang="he")

    content.about = translator.translate(content.about);

    for service in services:
        service.title = translator.translate(service.title);
        service.desc= translator.translate(service.desc);
    
    for review in reviews:
        review.name = translator.translate(review.name);
        review.occupation = translator.translate(review.occupation);
        review.title = translator.translate(review.title);
        review.desc = translator.translate(review.desc);

    context = {
        'lang': "hb",
        'content': content,
        'services': services,
        'reviews': reviews,
    }

    return render(request, 'main/main.html', context)

@admin_only
def admin(request):
    content = Content.objects.get()
    services = Service.objects.all()
    reviews = Review.objects.all()

    context = {
        'lang': "en",
        'services': services,
        'reviews': reviews,
        'content': content,
    }

    return render(request, 'main/admin.html', context)

@admin_only
def addService(request):
    form = ServiceForm()

    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/admin-panel/')

    context = {
        'form': form,
    }


    return render(request, 'main/serviceForm.html', context)

@admin_only
def editService(request, id):
    service = Service.objects.get(id = id)
    form = ServiceForm(instance=service)

    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            return redirect('/admin-panel/')

    context = {
        'form': form,
    }

    return render(request, 'main/serviceForm.html', context)

@admin_only
def delService(request, id):
    service = Service.objects.get(id = id)
    service.delete();
    return redirect('/admin-panel/')

@admin_only
def addReview(request):
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/admin-panel/')

    context = {
        'form': form,
    }

    return render(request, 'main/reviewForm.html', context)

@admin_only
def editReview(request, id):
    review = Review.objects.get(id = id)
    form = ReviewForm(instance=review)

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            return redirect('/admin-panel/')

    context = {
        'form': form,
    }

    return render(request, 'main/reviewForm.html', context)

@admin_only
def delReview(request, id):
    review = Review.objects.get(id = id)
    review.delete();
    return redirect('/admin-panel/')

@admin_only
def editContent(request):
    content = Content.objects.get()
    form = ContentForm(instance=content)

    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES, instance=content)
        if form.is_valid():
            form.save()
            return redirect('/admin-panel/')

    context = {
        'form': form,
    }

    return render(request, 'main/contentForm.html', context)

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('admin')

        else:
            messages.info(request, 'Username or Password is incorrect')

    return render(request, 'main/login.html')

@admin_only
def logoutUser(request):
    logout(request)
    return redirect('home')