from django.contrib import admin

from .models import Applicant
from .models import Login_log
from .models import Image

# Register your models here.

admin.site.register(Applicant)
admin.site.register(Login_log)
admin.site.register(Image)
