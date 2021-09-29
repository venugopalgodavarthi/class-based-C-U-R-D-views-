from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from tempview.forms import empform
from tempview.models import emp

# Create your views here.



















'''
#function based view
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

#userdefined class based view
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

'''
#predefined class based view
class Tempview(TemplateView):
    template_name='temp.html'
    form = empform()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form']=self.form
        return context
    def post(self,request):
        if request.method=='POST':
            form= empform(request.POST)
        if form.is_valid():
            res=emp.objects.create(name = form.cleaned_data['name'],email=form.cleaned_data['email'],sal=form.cleaned_data['sal'])
            res.save()
            return HttpResponse("data insert")


























'''
#function based view
def samplefunc(request):
    form = empform
    return render(request,"homefunc.html",{'res':form})

#userdefined class based view
class samplecls(View):
    def get(self,request):
        form = empform
        return render(request,"homecls.html",{'res':form})


#predefined class based view
class Tempview(TemplateView):
    template_name='temp.html'
    form = empform()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form']=self.form
        return context

'''


'''
#function based view
def samplefunc(request):
    return render(request,"homefunc.html",{'name':akshay,'age':25,"address":"bangalore"})

#userdefined class based view
class samplecls(View):
    def get(self,request):
        return render(request,"homecls.html",{'name':akshay,'age':25,"address":"bangalore"})

#predefined class based view
class Tempview(TemplateView):
    template_name='temp.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name']='akshay'
        context['age']=25
        context['address']="bangalore"
        return context
'''


'''
#userdefined function based view
def templates(request):
    return render(request,'temp.html')

#userdefined class based view
class samplecls(View):
    def get(self,request):
        return render(request,"homecls.html")
#predefined class based view
class Tempview(TemplateView):
    template_name = 'temp.html'
'''