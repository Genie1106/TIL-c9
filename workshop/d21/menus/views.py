from django.shortcuts import render, redirect
from .models import Question,Choice
# Create your views here.

def index(request):
    quests = Question.objects.all()
    return render(request,"index.html",{'quests':quests})
    
def vote(request):
    question=Question.objects.last()
    return render(request,"vote.html",{'question':question})
    
def update(request):
    content=request.POST.get("content")
    choice = Choice.objects.filter(content=content)
    choice.votes+=1
    choice.save()
    return redirect("Survey:result")
    
def result(request):
    question=Question.objects.last()
    return render(request,"result.html",{'question':question})