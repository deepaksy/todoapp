from django.contrib import admin
from .models import mywebsite

class mywebsiteAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

# Register your models here.

admin.site.register(mywebsite, mywebsiteAdmin)