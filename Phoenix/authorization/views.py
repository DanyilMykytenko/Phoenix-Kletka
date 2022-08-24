from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

def authorize_view (request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponse('Authenticated successfully')
    context = {}
    return render(request, 'authorization/authorization.html', context)