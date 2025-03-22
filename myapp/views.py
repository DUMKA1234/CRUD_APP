from django.shortcuts import render
from . import forms
from . import models
# Create your views here.
def employee(request):
    if request.method == "POST":
      form = forms.EmployeeForm(request .POST)
      if form.is_valid():
          try:
            form.save()
          except:
             pass
    else:
      form=forms.EmployeeForm()
    context ={'form':form}
    return render(request,'index.html',{'form':form})
def display(request):
   employees=models.Employee.objects.all()
   return render(request,"display.html",{'employees:employees'})

