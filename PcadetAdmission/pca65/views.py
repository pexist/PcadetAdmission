# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.gis.geoip2 import GeoIP2
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)

from . import models
# from . import views
from . import forms

class StudentCreateView(CreateView):
    fields = '__all__'
    model = models.Student


class StudentDetailView(DetailView):
    context_object_name = 'student_details'
    model = models.Student
    template_name = 'admissDetail/student_detail.html'


def index(request):
    return render(request, 'index.html')


def calendar(request):
    return render(request, 'calendar.html')


def document(request):
    return render(request, 'document.html')


def admidstep(request):
    return render(request, 'admidstep.html')

def entry(request):
    # todo make form for test 13ID
    form = forms.FormName()
    model = models.id13in
    # queryset = models.id13in.objects
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            form_id13 = form.cleaned_data['ID13']
            print('TEST  :: '+ form_id13) #todo make log file
            # model.objects.get()
            idObj = model.objects.filter(ID13__exact= form_id13)
            # entry = Entry.objects.get(pk=123)
            context = {'id13': form_id13}
            if idObj.exists():
                print("user exists ")
                return render(request, 'success.html', context)
            else:
                return redirect('pca65:create')
                # return render(request, 'create.html', context)
    return render(request, 'entry.html',{'form':form})

def success(request):
    data = request.POST
    context = {'data': data}
    return render(request, 'success.html', context)


def dataCheck(request):
    # todo make form for student status with 13ID and BOD
    return render(request, 'dataCheck.html')


def exPlace(request):
    return render(request, 'exPlace.html')


def answer(request):
    return render(request, 'answer.html')


def contact(request):
    return render(request, 'contact.html')

def bill(request):
    return render(request, 'print_bill.htm')