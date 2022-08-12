from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'generator/home.html')
def password(request):
    length=int(request.GET.get('length'))
    thepassword=""
    char=list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXZ'))
    if request.GET.get('number'):
        char.extend(list('0123456789'))
    for i in range(length):
        thepassword += random.choice(char)



    return render(request,'generator/password.html',{'password':thepassword})
