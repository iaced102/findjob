from django.urls import path
from django.urls import path
from .views import *

urlpatterns = [
    path('recruitment', Create_Recruitment_Form.as_view(),name = 'create_recruitment_form'),
    path('recruitment_create', Create_Recruitment_Post,name = 'create_recruitment_post'),
    path('review', Create_Review_Post.as_view(), name='create_review_post')
]