from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings

# SET THE NAMESPACE!
app_name = 'pca65'

# Be careful setting the name to just /login use user login instead!
urlpatterns = [
    # dynamic pages
    path('entry', views.entry, name='entry'),  # first check for first time (sign up)
    path('sign_in', views.sign_in, name='sign_in'),
    path('pca_status', views.pca_status, name='pca_status'),


    path('upload/', views.image_upload_view, name='upload'),
    path('bill', views.bill, name='bill'),
    path('success', views.success, name='success'),


    # todo need a better info filling system
    path('create/', views.StudentCreateView.as_view(success_url=".."), name='create'),
    path('<int:pk>/', views.StudentDetailView.as_view(), name='detail'),


    # static pages
    path('', views.index, name='index'),
    path('calendar', views.calendar, name='calendar'),
    path('admidstep', views.admit_step, name='admidstep'),
    path('answer', views.q_answer, name='answer'),
    path('exPlace', views.exam_place, name='exPlace'),
    path('document', views.document, name='document'),
    path('contact', views.contact, name='contact'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)