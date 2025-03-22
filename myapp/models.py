from django.db import models

# Create your models here.
class Employee(models.Model):
  empid = models.CharField(max_length=30)
  name =models.CharField(max_length=30)
  email=models.EmailField()
  contact_no =models.CharField(max_length=30)
   

  def __str__(self):
    return self.name
  class Meta:
    db_table="employee"

  