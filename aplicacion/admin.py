from django.contrib import admin


# Register your models here.
from .models import *
admin.site.register(Curso)
admin.site.register(staff)
admin.site.register(agencias)


