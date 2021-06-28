# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import (DetailView,
                                  CreateView)
from django.contrib import messages
# from . import views
from . import forms
from . import models
from .models import id13in
from .forms import ImageForm


# first check for first time (sign up)
def entry(request):
    # todo make form for test 13ID

    # todo the session expire not setup. the logic might not be corrected
    if request.session.has_key('currentID'):
        messages.add_message(request,messages.SUCCESS,request.session['currentID'])
        # messages.success(request,request.session['currentID'])
        return redirect('pca65:pca_status')

    # gen from
    form = forms.FormEntry()
    # if submit
    if request.method == 'POST':
        form = forms.FormEntry(request.POST)
        if form.is_valid():
            # todo need id13 validation
            form_id13 = form.cleaned_data['ID13']
            print('ID13  :: ' + form_id13)  # todo make log file
            request.session['currentID'] = form_id13
            # todo find the better way to check database
            try:
                idObj = id13in.objects.get(ID13__exact=form_id13)
                # idObj = model.objects.filter(ID13__exact=form_id13)
            except:
                idObj = None

            context = {'id13': form_id13}
            if idObj is not None:
                print("user exists ")
                return redirect('pca65:pca_status',context)
            else:
                # todo create new application, redirect to sign in
                application = id13in()
                application.ID13 = form_id13
                application.save()
                return render(request, 'pca65/student_form.html', context)

                # return render(request, 'create.html', context)
    return render(request, 'pca65/entry.html', {'form': form})


# student login
def sign_in(request):
    # todo if session login, goto status page, otherwise login
    # todo query error, no BD yet
    form = forms.FormSignIn()
    model = models.id13in

    if request.method == 'POST':
        form = forms.FormSignIn(request.POST)
        if form.is_valid():
            form_id13 = form.cleaned_data['ID13']
            form_bd = form.cleaned_data['BD']
            print('TEST  :: ' + form_id13 + '::' + form_bd)  # todo make log file

            try:
                # idObj = id13in.objects.filter(ID13__exact=form_id13, BD__exact =  form_bd)
                idObj = id13in.objects.filter(ID13__exact=form_id13)
                # idObj = model.objects.filter(ID13__exact=form_id13)
            except:
                idObj = None

            # entry = Entry.objects.get(pk=123)
            context = {'id13': form_id13}
            if idObj.exists():
                print("user exists ")
                return redirect('pca65:pca_status')
            else:
                return render(request, 'pca65/student_form.html', context)

    return render(request, 'pca65/signin.html', {'form': form})


# status of application
def pca_status(request):
    # 5 field for register_number, info input, image upload, payment, print_exam_id_card
    return render(request, 'pca65/status.html')


# upload image
def upload(request):
    # todo make form for student status with 13ID and registration_id
    return render(request, 'pca65/upload.html')


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


# print payment detail
def bill(request):
    return render(request, 'pca65/print_bill.htm')


# register success??
def success(request):
    data = request.POST
    context = {'data': data}
    return render(request, 'pca65/success.html', context)


##################### Demo Student Creator ############################
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


##################### Fixed page ############################
# first page
def index(request):
    return render(request, 'pca65/index.html')


# หมายกำหนดการต่างๆ
def calendar(request):
    return render(request, 'calendar.html')


# step to talk for admission
def admit_step(request):
    return render(request, 'admidstep.html')


# Q&A
def q_answer(request):
    return render(request, 'answer.html')


# exam place
def exam_place(request):
    return render(request, 'exPlace.html')


# pdf file
def document(request):
    return render(request, 'document.html')


# contact
def contact(request):
    return render(request, 'contact.html')

##################### Fixed page ############################
