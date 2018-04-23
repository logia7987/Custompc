from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Hardware)
admin.site.register(Compa)
admin.site.register(Custom)
admin.site.register(Comment)