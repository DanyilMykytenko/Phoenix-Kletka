from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

def authorize_view (request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home/')
    context = {}
    return render(request, 'authorization/authorization.html', context)