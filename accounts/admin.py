from django.contrib import admin
from .models import User

# Register your models here.
class User_field(admin.ModelAdmin):
    model = User
    list_display=['username','email', 'first_name']


admin.site.register(User,User_field)