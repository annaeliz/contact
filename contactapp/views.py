from django.shortcuts import render
from django.http import HttpResponse
from .models import contact

def home(request):
    return render(request,'index.html',{'msg':"WELCOME"})

def addcontact(request):
    responseDic={}
    if request.method=="POST":
        if(True):     
            try:
                Name=request.POST['nam']
                Phone=request.POST['num']
                x=contact.objects.all().values()
                for i in range(len(x)):
                    if x[i]['name']==Name or x[i]['phone']==Phone :
                        responseDic["msg"]="WELCOME"
                        responseDic["msg2"]="Contact Cannnot be Added, Already Exist!!"
                        return render(request,"index.html",responseDic)
                contdtls=contact(name=Name,phone=Phone)
                contdtls.save()
                responseDic["msg"]="WELCOME"
                responseDic["msg1"]="New Contact Added Successfully"
                return render(request,"index.html",responseDic)
            except Exception as e:
                print(e)
def display(request):
    contdtls=contact.objects.all()
    print(contdtls)
    return render(request,'index.html',{'msg':'WELCOME','cont':contdtls})

def delete(request):
    name=request.POST['nam']
    contdtls=contact.objects.filter(name=name)
    contdtls.delete()
    return render(request,'index.html',{'msg':"WELCOME",'msg3':'Conatct Removed'})

def update(request):
    if 'uname' in request.POST:
        name=request.POST['onam']
        newname=request.POST['nnam']
        contdtls=contact.objects.get(name=name)
        contdtls.name=newname
        contdtls.save()
        return render(request,'index.html',{'msg':"WELCOME",'msg4':"Update Name"})
    if 'unumber' in request.POST:
        name=request.POST['name']
        newnum=request.POST['nnum']
        contdtls=contact.objects.get(name=name)
        contdtls.phone=newnum
        contdtls.save()
        return render(request,'index.html',{'msg':"WELCOME",'msg5':"Update Number"})





