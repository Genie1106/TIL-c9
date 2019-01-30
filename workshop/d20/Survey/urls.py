from django.urls import path
from . import views

app_name = "Survey"

urlpatterns = [
    path('', views.index,name="list"),
    path('create/',views.create,name="create"),   
    path('create_survey/',views.create_survey,name="create_survey"),
    path('vote/',views.vote,name="vote"),
]