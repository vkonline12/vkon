from django.shortcuts import render
from .models import Web_Project,website,myweb

# Create your views here.

def myworks(request):
    myworks=myweb.objects.all()
    context={
        'myworks':myworks
    }

    return render(request,'index.html',context)

def details(request):
    details=Web_Project.objects.all()
    context={
        'details':details
    }
    return render(request,'details.html',context)

def spef_det(request,id):
    mweb=myweb.objects.filter(id=id)
    return render(request,'Spefic_detail.html',{'mweb':mweb})

def my_detail(request,id):
    all_detail=Web_Project.objects.filter(id=id)
    return render(request,'my_detail.html',{'all_detail':all_detail})

def add(request):
    if request.method=='POST':
        name=request.POST.get('name', )
        address=request.POST.get('address', )
        contact=request.POST.get('contact', )
        email=request.POST.get('email', )
        type_of_website=request.POST.get('type_of_website', )
        date=request.POST.get('date', )

        my_wap=website(name=name,address=address,contact=contact,email=email,type_of_website=type_of_website,date=date)
        my_wap.save()
    return render(request,'add.html')
