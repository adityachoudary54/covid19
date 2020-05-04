from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Notes
from .forms import notesForm,userForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.
def welcome(request):
    return HttpResponse("Welcome to notesapp")

def deleteNotes(request,id):
    if request.user.is_authenticated:
        obj = Notes.objects.get(id=id) 
        if request.method=='POST':
            obj.delete()
            return redirect('../')
        context={
            'obj':obj
        }
        return render(request,'notesApp/deleteNotes.html',context)
    else:
        return HttpResponse('Unauthorized access')
def modifyNotes(request,id):
    if request.user.is_authenticated:
        obj = Notes.objects.get(id=id)  
        form = notesForm(request.POST or None, instance = obj)  
        if form.is_valid():  
            form.save()  
            return redirect("../")  
        context={
            'form':form,
            'obj':obj
        }
        return render(request, 'notesApp/updateNotes.html', context)  
    else:
        return HttpResponse('Unauthorized access')
            

def listNotes(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            return redirect('add/')
        querySet=Notes.objects.all()
        context={
            'objList':querySet,
        }
        return render(request,'notesApp/listNotes.html',context)
    else:
        return HttpResponse('Unauthorized access')

def addNotes(request):
    if request.user.is_authenticated:
        form=notesForm(request.POST or None)
        print(request.user)
        querySet=Notes.objects.all()
        if form.is_valid():
            form.save()
            form=notesForm()
        context={
            'form':form,
            'objList':querySet,
        }
        return render(request,"notesApp/listNotesAdd.html",context)
    else:
        return HttpResponse('Unauthorized access')

def loginNotesApp(request):
    form=userForm()
    if request.method=='POST':
        form=userForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('details/')
            else:
                return HttpResponse('Unauthorized access')
    context={
        'form':form
    }
    return render(request,'notesApp/login.html',context)