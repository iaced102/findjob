from django.shortcuts import render
from post.models import Recruitment_Post, Review_Post
from django.views.generic.detail import DetailView
# Create your views here.

class Detail_Recruitment(DetailView):
    model = Recruitment_Post
    template_name = 'apps/detail-recruitment.html'

class Detail_Review(DetailView):
    model = Review_Post
    template_name= 'apps/detail-review.html'