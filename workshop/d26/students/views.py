from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student
# Create your views here.

def new(request):
    form = StudentForm()
    return render(request,'new.html',{'form':form})
    
def create(request):
    form = StudentForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        age = form.cleaned_data.get('age')
        student = Student.objects.create(name=name,age=age)
        
    return redirect('students:index')
    
def index(request):
    students = Student.objects.all()
    return render(request,"index.html",{"students":students})