"""PcadetAdmission URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from admissionlogin import views as lg
from admissDetail import views as ad

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', ad.IndexView.as_view(),name='index'),
    # path('', lg.index,name='index'),
    path('admin/', admin.site.urls),
    path('special/', lg.special,name='special'),
    path('admissionlogin/', include('admissionlogin.urls')),
    path('logout/', lg.user_logout, name='logout'),
    path('admissDetail/',include('admissDetail.urls')),
    path('pca65/',include('pca65.urls'))
]
