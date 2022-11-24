from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(StudentAccount)
admin.site.register(StaffAccount)
admin.site.register(Session)
admin.site.register(Hostel)
admin.site.register(Room)