from django.db import models

# Create your models here.

class Members(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=200)
    major = models.CharField(max_length=50)
    date_of_joining = models.DateField()
    photo_file_name = models.CharField(max_length=50)
    

