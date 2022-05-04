from django.contrib import admin
from .models import WorkExperience, Education, URL, Document, Role
from .models import User
from django.contrib.auth import get_user_model
# Register your models here.
User = get_user_model()
admin.site.register(User)
admin.site.register(Role)
admin.site.register(URL)
admin.site.register(Document)
admin.site.register(Education)
admin.site.register(WorkExperience)