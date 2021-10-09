from django.shortcuts import render
from .models import Recruitment_Post
from django.views.generic import TemplateView
# Create your views here.
class List_Recruitments(TemplateView):
    template_name = 'apps/recruitements/list-recruitments.html'
    list_recruitments = [a for a in range(10)]
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_recruitments'] = Recruitment_Post.objects.filter(id__in = self.list_recruitments)
        return context
    



class List_Reviews(TemplateView):
    template_name = 'apps/reviews/list-reviews.html'
    list_reviews = [a for a in range(10)]
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_reviews'] = Recruitment_Post.objects.filter(id__in = self.list_reviews)
        return context