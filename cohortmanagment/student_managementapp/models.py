from django.db import models

# Create your models here.


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    
class Status(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    
class Cohort(models.Model):
    name = models.CharField(max_length=100, unique=True)
    score_type = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    
    
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    phone = models.IntegerField(null=True,)
    joined_date = models.DateTimeField(null=True)
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
                               
                               