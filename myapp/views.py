from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from myapp.models import emp
from myapp.forms import empform
# Create your views here.

def samplefunc(request):
    form = emp.objects.all()
    return render(request,"homefunc.html",{'res':form})


class samplecls(View):
    def get(self,request):
        form = emp.objects.all()
        return render(request,"homecls.html",{'res':form})



'''
def samplefunc(request):
    return HttpResponse('<h1>welcome to function based view </h1>')


class samplecls(View):
    def get(self,request):
        return HttpResponse('<h1>welcome to class based view </h1>')

def samplefunc(request):
    return render(request,"homefunc.html")


class samplecls(View):
    def get(self,request):
        return render(request,"homecls.html")

def samplefunc(request,name):
    return render(request,"homefunc.html",{'res':name})


class samplecls(View):
    def get(self,request,name):
        return render(request,"homecls.html",{'res':name})

def samplefunc(request):
    res=emp.objects.create(name="venu",email="venu@gmail.com",sal=15000)
    res.save()
    form = emp.objects.all()
    return render(request,"homefunc.html",{'res':form})


class samplecls(View):
    def get(self,request):
        res=emp.objects.create(name="murali",email="murali@gmail.com",sal=15000)
        res.save()
        form = emp.objects.all()
        return render(request,"homecls.html",{'res':form})


def samplefunc(request):
    form = empform
    return render(request,"homefunc.html",{'res':form})


class samplecls(View):
    def get(self,request):
        form = empform
        return render(request,"homecls.html",{'res':form})


def samplefunc(request):
    form = emp.objects.all()
    return render(request,"homefunc.html",{'res':form})


class samplecls(View):
    def get(self,request):
        form = emp.objects.all()
        return render(request,"homecls.html",{'res':form})


def samplefunc(request):
    if request.method=='POST':
        form = empform(request.POST)
        if form.is_valid():
            res=emp.objects.create(name = form.cleaned_data['name'],email=form.cleaned_data['email'],sal=form.cleaned_data['sal'])
            res.save()
            return HttpResponse("data insert")
    if request.method=='GET':
        form= empform()
    return render(request,"homefunc.html",{'res':form})


class samplecls(View):
    def get(self,request):
        form = empform
        return render(request,"homecls.html",{'res':form})

    def post(self,request):
        if request.method=='POST':
            form= empform(request.POST)
        if form.is_valid():
            res=emp.objects.create(name = form.cleaned_data['name'],email=form.cleaned_data['email'],sal=form.cleaned_data['sal'])
            res.save()
            return HttpResponse("data insert")


def samplefunc(request):
    if request.method=='POST':
        form = empform(request.POST)
        if form.is_valid():
            res=emp.objects.create(name = form.cleaned_data['name'],email=form.cleaned_data['email'],sal=form.cleaned_data['sal'])
            res.save()
            return HttpResponse("data insert")
    if request.method=='GET':
        form= empform()
    return render(request,"homefunc.html",{'res':form})


class samplecls(View):
    def get(self,request):
        form = empform
        return render(request,"homecls.html",{'res':form})

    def post(self,request):
        if request.method=='POST':
            form= empform(request.POST)
        if form.is_valid():
            res=emp.objects.create(name = form.cleaned_data['name'],email=form.cleaned_data['email'],sal=form.cleaned_data['sal'])
            res.save()
            return HttpResponse("data insert")


def samplefunc(request,name):
    emp.objects.filter(id=name).delete()
    form = emp.objects.all()
    return render(request,"homefunc.html",{'res':form})


class samplecls(View):
    def get(self,request,name):
        emp.objects.filter(id=name).delete()
        form = emp.objects.all()
        return render(request,"homecls.html",{'res':form})

def samplefunc(request,name):
    if request.method=='POST':
        res = emp.objects.get(id=name)
        res.name = request.POST['name']
        res.email = request.POST['email']
        res.sal = request.POST['sal']
        res.save()
        return HttpResponse("data update")
    if request.method=='GET':
       form = emp.objects.get(id=name)
    return render(request,"homefunc.html",{'res':form})


class samplecls(View):
    def get(self,request,name):
        form= emp.objects.get(id=name)
        return render(request,"homecls.html",{'res':form})

    def post(self,request,name):
        if request.method=='POST':
            res=emp.objects.get(id=name)
            res.name = request.POST['name']
            res.email=request.POST['email']
            res.sal=request.POST['sal']
            res.save()
            return HttpResponse("data update")

'''

