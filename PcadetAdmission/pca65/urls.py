from django.urls import path

from . import views

# SET THE NAMESPACE!
app_name = 'pca65'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns = [
    path('', views.index, name='index'),
    path('calendar', views.calendar, name='calendar'),
    path('document', views.document, name='document'),
    path('admidstep', views.admidstep, name='admidstep'),
    path('entry', views.entry, name='entry'),
    path('success', views.success,name='success'),

    path('dataCheck', views.dataCheck, name='dataCheck'),
    path('exPlace', views.exPlace, name='exPlace'),
    path('answer', views.answer, name='answer'),
    path('contact', views.contact, name='contact'),
    path('bill', views.bill, name='bill'),

    path('create/',views.StudentCreateView.as_view(success_url=".."),name='create'),
    path('<int:pk>/',views.StudentDetailView.as_view(),name='detail'),
]
