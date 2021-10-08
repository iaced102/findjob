from django.contrib import admin
from .models import *
# Register your models here.

class Recruitment_models(admin.ModelAdmin):
    model = Recruitment_Post
    list_display= ['type', 'author', 'title', 'range']

admin.site.register(Recruitment_Post)
admin.site.register(Review_Post)
admin.site.register(Category_Job)