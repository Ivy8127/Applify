from django.contrib import admin

from .models import *

# Register your models here.

# admin.site.register(User)
admin.site.register(Role)
admin.site.register(URL)
admin.site.register(Document)
admin.site.register(Education)
admin.site.register(WorkExperience)