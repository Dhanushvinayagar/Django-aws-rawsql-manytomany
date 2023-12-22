from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Employee)

# Big H
admin.site.register(TableDb)
admin.site.register(UserRole)

#Big U
admin.site.register(PersonaDb)
admin.site.register(Kpi)
admin.site.register(Filter)
admin.site.register(Report)