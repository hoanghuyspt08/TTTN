from django.contrib import admin
from .models import Profile, Hotel, Room

class Profile_unit(admin.ModelAdmin):
    list_display = ('name', 'email','phone', 'birth_date','gender')

class Hotel_unit(admin.ModelAdmin):
    list_display = ('name','cost', 'address','utilities', 'describe')

class Room_unit(admin.ModelAdmin):
    list_display = ('type', 'width', 'cost', 'utilities')

admin.site.register(Profile, Profile_unit)
admin.site.register(Hotel, Hotel_unit)
admin.site.register(Room, Room_unit)