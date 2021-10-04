from django.shortcuts import render
from post.models import Category_Job
from django.views.generic import TemplateView

# Create your views here.

def Create_Recruitment_Post(request):
    context = Category_Job.objects.all()

    if request.method == "GET":
        return render(request, 'create-recruitment-post.html', context)