from django.urls import path
from first_app import views


urlpatterns =[
    path("index",views.index,name="index"),
    path("forms",views.forms,name="forms"),
]