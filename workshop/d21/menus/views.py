from django.shortcuts import render
from .models import Question,Choice
# Create your views here.

def index(request):
    quest = Question.objects.get(Question_id)
    return render(request,"index.html",{'quest':quest})