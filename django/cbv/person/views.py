from django.shortcuts import render,redirect
from .models import Person
from .forms import PersonForm
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# def list(request):
#     persons = Person.objects.all()
#     return render(request, 'person/person_list.html',{'persons':persons}).

class PersonList(ListView):
    model = Person
    context_object_name='persons'
    
# def create(request):
#     if request.method == "POST":
#         person_form = PersonForm(request.POST)
#         if person_form.is_valid():
#             person_form.save()
#             return redirect("person:list")
#     else:
#         form=PersonForm()
#     return render(request,'person/person_form.html',{'form':form})

class PersonCreate(LoginRequiredMixin,CreateView):
    model = Person
    form_class = PersonForm
    success_url = '/person/'

            
        
        