from django.shortcuts import render

def authorize(request):
    return render(request, "authorization/authorization.html")