# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import (DetailView,
                                  CreateView)

# from . import views
from . import forms
from . import models
from .forms import ImageForm


# first page
def index(request):
    return render(request, 'pca65/index.html')


# หมายกำหนดการต่างๆ
def calendar(request):
    return render(request, 'calendar.html')


# pdf file
def document(request):
    return render(request, 'document.html')


# step to talk for admission
def admit_step(request):
    return render(request, 'admidstep.html')


# exam place
def exam_place(request):
    return render(request, 'exPlace.html')


# Q&A
def q_answer(request):
    return render(request, 'answer.html')


# contact
def contact(request):
    return render(request, 'contact.html')


# student register
# todo make nice table
class StudentCreateView(CreateView):
    fields = '__all__'
    model = models.Student


# student detail
class StudentDetailView(DetailView):
    context_object_name = 'student_details'
    model = models.Student
    template_name = 'pca65/student_detail.html'


# first check for first time (sign up)
def entry(request):
    # todo make form for test 13ID
    form = forms.FormName()
    model = models.id13in
    # queryset = models.id13in.objects
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            form_id13 = form.cleaned_data['ID13']
            print('TEST  :: ' + form_id13)  # todo make log file
            # model.objects.get()
            idObj = model.objects.filter(ID13__exact=form_id13)
            # entry = Entry.objects.get(pk=123)
            context = {'id13': form_id13}
            if idObj.exists():
                print("user exists ")
                # redirect to sign in
                return redirect('pca65:dataCheck')
            else:
                # todo create new application
                return render(request, 'pca65/status.html', context)

                # return render(request, 'create.html', context)
    return render(request, 'pca65/entry.html', {'form': form})


# status of application
def pca_status(request):
    # 5 field for register_number, info input, image upload, payment, print_exam_id_card
    return render(request, 'pca65/status.html')


# student login
def dataCheck(request):
    # todo make form for student status with 13ID and registration_id
    return render(request, 'pca65/dataCheck.html')


# upload image
def upload(request):
    # todo make form for student status with 13ID and registration_id
    return render(request, 'pca65/upload.html')


# print payment detail
def bill(request):
    return render(request, 'pca65/print_bill.htm')


# register success??
def success(request):
    data = request.POST
    context = {'data': data}
    return render(request, 'pca65/success.html', context)


def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'pca65/upload.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'pca65/upload.html', {'form': form})
