from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
def index(request):
    students = Student.objects.all()
    return render(request,'index.html',{'students':students})
    
def submit(request):
    return render(request,"submit.html")
    
def create(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    birthday = request.POST.get("birthday")
    age = request.POST.get("age")    
    post = Student(name=name,email=email,birthday=birthday,age=age)
    post.save()
    return redirect("/")
    
def read(request,student_id):
    student = Student.objects.get(pk=student_id)
    return render(request,"read.html",{"student":student})
    
def delete(request,student_id):
    student = Student.objects.get(pk=student_id)
    student.delete()
    return redirect("/")
    
def edit(request,student_id):
    student=Student.objects.get(pk=student_id)
    return render(request,"edit.html",{"student":student})
    
def update(request,student_id):
    student=Student.objects.get(pk=student_id)
    student.name = request.POST.get("name")
    student.email = request.POST.get("email")
    student.birthday = request.POST.get("birthday")
    student.age = request.POST.get("age")    
    student.save()
    return redirect(f"/{student_id}/")
