from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import user,music,musicz,contact,premium
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method=='POST':
        name=request.POST['username']
        
        email=request.POST['email']
        password=request.POST['password']
        emailExist=user.objects.filter(email=email)
        if emailExist:
            messages.info(request,'email already exist')
            return render(request,'index.html')
        else:
            user(name=name,email=email,password=password).save()
            return render(request,'topsongs.html')
            messages.success(request,'the user '+request.POST['username']+' is saved successfully')
    return render(request,'index.html')
def topsongfn(request):
    musiclist=music.objects.all()
    musiczlist=musicz.objects.all()
    context={
        'musiclist': musiclist,
        'musiczlist': musiczlist


    }
    
    return render(request,'topsongs.html',context)

def detailfn(request,music_id):
    detailed=music.objects.get(id=music_id)
    

    return render(request,'detail.html',{'detailed':detailed})
def detailfnz(request,musicz_id):
    
    detailedz=musicz.objects.get(id=musicz_id)

    return render(request,'detailz.html',{'detailedz':detailedz})   
def aboutfn(request):
    return render(request,'about.html')
def contactfn(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        
        message=request.POST['message']
        contact(name=name,email=email,message=message).save()
    

        return render(request,'contact.html')
    else:
        return render(request,'contact.html')
def premiumfn(request):
    if request.method=='POST':
        card=request.POST['card']
        cvv=request.POST['cvv']
        email=request.POST['email']
        password=request.POST['password']
        premium(card=card,cvv=cvv,email=email,password=password).save()

        return render(request,'premium.html')
    else:
        messages.info(request,'booking not confirmed')
        return render(request,'premium.html')