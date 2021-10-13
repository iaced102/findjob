from django.shortcuts import render
from django.views.generic import TemplateView
from post.models import Category_Job
# Create your views here.

class Home(TemplateView):
    template_name = 'pages/home.html'
    def get_context_data(self,*args, **kwargs):
        context= super().get_context_data(**kwargs)
        context['category_job'] = Category_Job.objects.all()
        return context