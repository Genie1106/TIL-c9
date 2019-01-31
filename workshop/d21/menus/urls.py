from django.urls import path
from menus import views

app_name = "Survey"

urlpatterns = [
    path("",views.index,name="index"),
    path("vote/",views.vote,name="vote"),
    path("result/",views.result,name="result"),
    path("update/",views.update,name="update"),
]
