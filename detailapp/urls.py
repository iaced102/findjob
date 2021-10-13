from django.urls import path
from .views import Detail_Recruitment, Detail_Review

urlpatterns = [
    path('recruitment/<int:pk>', Detail_Recruitment.as_view(), name='detail_recruitment'),
    path('review/<int:pk>', Detail_Review.as_view(), name='detail_review')
]