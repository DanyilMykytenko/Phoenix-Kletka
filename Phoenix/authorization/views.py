from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import User


def authorize_view (request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('pass')
        checkUsername = User.objects.filter(full_name = username)
        checkPassword = User.objects.filter(password = password)
        if checkUsername != checkPassword:
            error_message = "Wrong username or password..."
        # user = authenticate(request,username=username,password=password)
        # if user is not None:
        #     login(request,user)
        #     return redirect('home/')
    context = {}
    return render(request, 'authorization/authorization.html', context)