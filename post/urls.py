from django.urls import path
from .views import *

urlpatterns = [
        path('recruitments', List_Recruitments.as_view(), name ='list_recruitments'),
        path('reviews', List_Reviews.as_view(), name = 'list_reviews'),

    ]