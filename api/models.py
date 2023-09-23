from django.db import models

# Create your models here.

class Student(models.Model):
      
    GENDERS=(('F','Female'),
             ('M','Male'),
             ('u','undisclosed'))
    name = models.CharField(max_length=100)
    roll_number=models.IntegerField(unique=True)                     
    email=models.EmailField(max_length=100)
    gender=models.CharField(max_length = 1, choices = GENDERS,null=True)
    percentage=models.FloatField()
    institute=models.ForeignKey("Institute",on_delete= models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.name
    
class Institute(models.Model):
    
    TYPES=(('C','COLLEGe'),
             ('H','highschool'))
    name = models.CharField(max_length=200)
    inst_type=models.CharField(max_length=1,choices=TYPES)
    
        
    def __str__(self):
        return self.name