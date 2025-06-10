from django.contrib import admin
from models import Profile

class Profile_unit(admin.ModelAdmin):
    list_display = ('name', 'email','phone', 'birth_date','gender')

admin.site.register(Profile, Profile_unit)
