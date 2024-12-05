from django.db import models

# Create your models here.

class Members(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=50)
    major = models.CharField(max_length=50, blank=True)
    graduation_time = models.DateField(max_length=10, blank=True)
    profile_photo_name = models.CharField(max_length=30, blank=True)
    resume_file_name = models.CharField(max_length=30, blank=True)

class Officers(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.OneToOneField(Members, on_delete=models.CASCADE, to_field='name')
    bio = models.TextField()
    position = models.CharField(max_length=50)
    responsibility = models.TextField()

class Events(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length= 50)
    scheduled_date_time = models.DateTimeField()
    host = models.ManyToManyField(Members, to_field='name')
    sponsor = models.CharField(max_length=200, blank=True)
    rsvp = models.IntegerField(default=0)

class Comments(models.Model):

    id = models.AutoField(primary_key = True)
    content = models.TextField()
    author = models.ForeignKey(Members, on_delete=models.CASCADE, to_field='name')
    resume = models.ForeignKey(Members, on_delete=models.CASCADE, to_field='resume_file_name')









