from django.contrib import admin
from .models import Logger,Reservation,Menu
from django.contrib.auth.models import User
    
# Register your models here.
admin.site.register(Logger)
# admin.site.unregister(User)
admin.site.register(Reservation)
admin.site.register(Menu)

'''from django.contrib.auth.admin import UserAdmin 
@admin.register(User) 
class NewAdmin(UserAdmin): 
    readonly_fields = [ 
        'date_joined', 
    ] '''