from django.urls.base import reverse, reverse_lazy
from django.shortcuts import render
from django.views.generic import FormView,ListView,DetailView,CreateView,UpdateView,DeleteView
from formview.forms import empform
from formview.models import empmodel
# Create your views here.

class detailsview(DetailView):
    model=empmodel
    template_name="empdetails.html"
    context_object_name='form'

class createview(CreateView):
    model=empmodel
    fields='__all__'
    context_object_name = 'form'
    template_name = "create.html"

class updateview(UpdateView):
    model=empmodel
    fields='__all__'
    context_object_name = 'form'
    template_name = "update.html"

class Listview(ListView):
    context_object_name = 'form'
    model = empmodel
    template_name ="emplist.html"

class deleteview(DeleteView):
    model=empmodel
    template_name = "delete.html"
    success_url = reverse_lazy('listview')

class Formview(FormView):
    form_class = empform
    template_name='form.html'








'''
#function based view
def samplefunc(request,pk):
    form = emp.objects.get(id=pk)
    return render(request,"homefunc.html",{'res':form})

#userdefined class based view
class samplecls(View):
    def get(self,request,pk):
        form = emp.objects.get(id=pk)
        return render(request,"homecls.html",{'res':form})

#predefined class based view
class detailsview(DetailView):
    model=empmodel


class detailsview(DetailView):
    model=empmodel
    template_name="empdetails.html"
    context_object_name='form'

'''

'''

#function based view
def samplefunc(request,name):
    emp.objects.filter(id=name).delete()
    form = emp.objects.all()
    return render(request,"homefunc.html",{'res':form})

#userdefined class based view
class samplecls(View):
    def get(self,request,name):
        emp.objects.filter(id=name).delete()
        form = emp.objects.all()
        return render(request,"homecls.html",{'res':form})

#predefined class based view
class Listview(ListView):
    model = empmodel

#predefined class based view
class Listview(ListView):
    context_object_name = 'form'
    model = empmodel
    template_name ="emplist.html"
'''

'''
#function based view
def samplefunc(request):
    form = empform
    return render(request,"homefunc.html",{'res':form})

#userdefined based view
class samplecls(View):
    def get(self,request):
        form = empform
        return render(request,"homecls.html",{'res':form})

#predefined based view
class Formview(FormView):
    form_class = empform
    template_name='form.html'


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

#predefined class based view
class Formview(FormView):
    form_class=empform
    template_name='form.html'
    def form_valid(self, form):
        form.save()
        return HttpResponse('form is summit')
'''