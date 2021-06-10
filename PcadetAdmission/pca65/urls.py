from django.urls import path

from . import views

# SET THE NAMESPACE!
app_name = 'pca65'

# Be careful setting the name to just /login use user login instead!
urlpatterns = [
    # static pages
    path('admidstep', views.admit_step, name='admidstep'),
    path('answer', views.q_answer, name='answer'),
    path('calendar', views.calendar, name='calendar'),
    path('contact', views.contact, name='contact'),
    path('document', views.document, name='document'),
    path('exPlace', views.exam_place, name='exPlace'),
    path('', views.index, name='index'),

    # dynamic pages
    path('entry', views.entry, name='entry'),  # first check for first time (sign up)
    path('pca_status', views.pca_status, name='pca_status'),
    path('dataCheck', views.dataCheck, name='dataCheck'),

    # todo need a better info filling system
    path('create/', views.StudentCreateView.as_view(success_url=".."), name='create'),
    path('<int:pk>/', views.StudentDetailView.as_view(), name='detail'),

    path('upload/', views.image_upload_view, name='upload'),
    path('bill', views.bill, name='bill'),

    path('success', views.success, name='success'),

]
