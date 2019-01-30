from django.urls import path
from menus import views

urlpatterns = [
    path("index/",views.index)
]
