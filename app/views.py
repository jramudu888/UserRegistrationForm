from django.shortcuts import render
from app.forms import *
# Create your views here.
def registration(request):
    UF=UserForm()
    PF=ProfileForm()
    d={'uf':UF,'PF':PF}
    return render(request,'registration.html',d)
