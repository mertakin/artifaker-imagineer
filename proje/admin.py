from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Categories)
admin.site.register(Images)
admin.site.register(Comment)