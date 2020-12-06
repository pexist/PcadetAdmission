from django.shortcuts import render
from django.contrib.gis.geoip2 import GeoIP2
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from . import models
from . import views


def get_client_ip(request):
    g = GeoIP2()
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for
        city = g.city(ip)
    else:
        ip = request.META.get('REMOTE_ADDR')
        city = g.city(ip)
    return ip, city


# Pretty simple right?
class IndexView(TemplateView):
    # Just set this Class Object Attribute to the template page.
    # template_name = 'app_name/site.html'
    template_name = 'admissDetail/index.html'

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        # ip,city = get_client_ip(self.request)
        context['injectme'] = "Test Injection!"
        # context['ip'] = ip
        # context['message'] = "message"
        # context['city'] = city

        return context

        ## Error return 127.0.0.1
        # def get_context_data(self,**kwargs):
        # context  = super().get_context_data(**kwargs)
        # ip,city = get_client_ip(self.request)
        # context['injectme'] = "Test Injection!"
        # context['ip'] = ip
        # context['message'] = "message"
        # context['city'] = city
        #
        # return context


class StudentListView(ListView):
    # If you don't pass in this attribute,
    # Django will auto create a context name
    # for you with object_list!
    # Default would be 'school_list'
    # Example of making your own:
    context_object_name = 'student_list'
    model = models.Student


class StudentDetailView(DetailView):
    context_object_name = 'student_details'
    model = models.Student
    template_name = 'admissDetail/student_detail.html'


class StudentCreateView(CreateView):
    fields = '__all__'
    model = models.Student


class StudentUpdateView(UpdateView):
    fields = '__all__'
    model = models.Student


class StudentDeleteView(DeleteView):
    model = models.Student
    success_url = reverse_lazy("admissDetail:list")


class CBView(View):
    def get(self,request):
        return HttpResponse('Class Based Views are Cool!')

