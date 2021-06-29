from django.contrib import admin

from .models import Applicant
from .models import Login_log

# Register your models here.

admin.site.register(Applicant)
admin.site.register(Login_log)
