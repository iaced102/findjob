from django.urls import path
from django.urls import path
from .views import *

urlpatterns = [
    path('recruitment', Create_Recruitment_Post,name = 'create_recruitment_post')
]