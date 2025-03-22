from django.urls import path
from .import views
urlpatterns = [
     path('emp', views.employee, name="emp"),
     path('display', views.display, name="display.html")
]