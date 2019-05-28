from django.http import HttpResponse
from django.shortcuts import render

def new_profile(request):
    ls_profile = ['email', 'username', 'pin', 'website', 'address', 'alias']
    context = {'ls_profile': ls_profile}
    return HttpResponse(render(request, 'profiles/new.html', context))