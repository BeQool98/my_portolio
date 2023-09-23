from django.shortcuts import render
from django.http import HttpResponse
from.models import *

# Create your views here.

def home(request):
    projects=Projects.objects.all().order_by("-date_created")
    last_job=projects[0]
    print(last_job)
    skills=Skills.objects.all()
    experience=SchoolExperience.objects.all()
    personal_detail=PersonalDetails.objects.get()
    about=AboutMyself.objects.get()
    print(about.title)

    
    
    
    context={"projects":projects, "skills":skills, "personal_detail":personal_detail,       
                    "about":about, "experience":experience, "last_job":last_job}
    return render(request, 'index.html', context)

def download_cv(request):
    pass

def messages_report(request):
    if request.method == "POST":
         name=request.POST.get('name')
         email=request.POST.get('email')
         subject=request.POST.get('subject')
         msg=request.POST.get('msg')
         new_message=MessageReport(name=name, email=email, subject=subject, msg_body=msg)
         new_message.save()
        
         
    return HttpResponse("success")
    
