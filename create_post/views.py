from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from post.models import Category_Job, Recruitment_Post, Review_Post


# Create your views here.

class Create_Recruitment_Form(LoginRequiredMixin, TemplateView):
    template_name = 'create-recruitment-post.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category_Job.objects.all()
        return context

def Create_Recruitment_Post(request):
    context = Category_Job.objects.all()
    if request.method == 'POST':
        type = request.POST.get('type')
        if type in [str(a) for a in range(len(context))]:
            category = Category_Job.objects.get(id=type)
        else:
            category = Category_Job.objects.create(name = type)
            category.save()
        title = request.POST.get('title')
        content = request.POST.get('content')
        rangewage = request.POST.get('range')
        company_name = request.POST.get('company_name')
        location = request.POST.get('location')
        user = request.user
        post = Recruitment_Post.objects.create(title=title, content=content, range=rangewage, type=category, author = user, company_name=company_name, locations=location)
        return redirect('home')



#create review post

class Create_Review_Post(LoginRequiredMixin,TemplateView):
    template_name = 'create-review-post.html'
    
    def get(self, request):
        return render(request, 'create-review-post.html')
    

    def post(self, request):
        print('POST nè :))')
        title = request.POST.get('title')
        user = self.request.user
        content = request.POST.get("content")
        post = Review_Post.objects.create(title =title, content = content, author = user)
        return redirect('home')