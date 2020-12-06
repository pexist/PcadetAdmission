from django.urls import path, include
from . import views

app_name = 'admissDetail'

urlpatterns = [
    path('',views.StudentListView.as_view(),name='list'),
    path('', views.get_client_ip, name='ipaddress'),
    path('<int:pk>/',views.StudentDetailView.as_view(),name='detail'),
    path('create/',views.StudentCreateView.as_view(success_url=".."),name='create'),
    path('update/<int:pk>/',views.StudentUpdateView.as_view(success_url="../../"),name='update'),
    path('delete/<int:pk>/',views.StudentDeleteView.as_view(success_url="../../"),name='delete')
]
