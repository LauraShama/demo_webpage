from django.urls import path
from . import views

urlpatterns = [path("", views.get_credit_info, name="get_credit_info")
     
 ]
 
