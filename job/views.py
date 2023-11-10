from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Job
from django.core.paginator import Paginator
from .form import ApplyForm , JobForm
from .filters import JobFilter


# Create your views here.

def job_list(request):
    
    
    filter = JobFilter(request.GET, queryset=Job.objects.all())
    job_list = filter.qs

    paginator = Paginator(job_list, 2)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'jobs' : page_obj,
        'job_count': job_list.count,
        'filter' : filter
    }
    return render(request,'job/job_list.html',context)



def job_detail (request ,slug):
    job_detail = Job.objects.get(slug=slug)
    
    if request.method=='POST':
        form = ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
              
    else: 
        form = ApplyForm() 
    context = {
        'job' : job_detail,
        'form' : form
    }
    return render(request,'job/job_detail.html',context)


@login_required
def add_job (request):
    # add_job = Job.objects.get(slug=slug)
    
    if request.method=='POST':
        form = JobForm(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = add_job
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))
              
    else:  
        form = JobForm() 
    context = {
        'form' : form,
    }
    return render(request,'job/add_job.html',context)
