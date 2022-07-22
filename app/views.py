from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def registration(request):
    UF=UserForm()
    PF=ProfileForm()
    d={'uf':UF,'PF':PF}
    if request.method=='POST' and request.FILES:
        UD=UserForm(request.POST)
        PD=ProfileForm(request.POST,request.FILES)
        if UD.is_valid() and PD.is_valid():
            user1=UD.save(commit=False)
            user1.set_password(UD.cleaned_data['password'])
            user1.save()
            profile=PD.save(commit=False)
            profile.user=user1
            profile.save()
            return HttpResponse('registration is successfull')
        
    return render(request,'registration.html',d)
