from django.shortcuts import render, redirect
from .models import Quest, surv

# Create your views here.
def index(request):
    quests = surv.objects.all()
    return render(request,"index.html",{'quests':quests})
    
def create(request):
    title = request.POST.get('title')
    content1 = request.POST.get('content1')
    content2 = request.POST.get('content2')
    content3 = request.POST.get('content3')
    quest = surv(title=title,content1=content1,content2=content2,content3=content3)
    quest.save()
    q1 = Quest(content=content1,votes=0)
    q1.save()
    q1 = Quest(content=content2,votes=0)
    q1.save()
    q1 = Quest(content=content3,votes=0)
    q1.save()
    return redirect('Survey:list')
    
def create_survey(request):
    return render(request,"create_survey.html")
    
def vote(request):
    quests = surv.objects.first()
    return render(request,'vote.html',{'quests':quests})
    
def 
    