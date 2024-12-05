from django.db import models

# Create your models here.

class Members(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=50)
    major = models.CharField(max_length=50, blank=True)
    graduation_time = models.CharField(max_length=10, null=True)
    profile_photo_name = models.CharField(max_length=30, blank=True)
    resume_file_name = models.CharField(max_length=30, blank=True, unique=True)

class Officers(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.OneToOneField(Members, on_delete=models.CASCADE, to_field='email')
    bio = models.TextField()
    position = models.CharField(max_length=50)
    responsibility = models.TextField()

class Events(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length= 50)
    scheduled_date_time = models.DateTimeField()
    host = models.ManyToManyField(Members)
    sponsor = models.CharField(max_length=200, blank=True)
    rsvp = models.IntegerField(default=0)

class Comments(models.Model):

    id = models.AutoField(primary_key = True)
    content = models.TextField()
    email = models.ForeignKey(Members, on_delete=models.CASCADE, to_field='email', related_name='email_of_comment')
    resume = models.ForeignKey(Members, on_delete=models.CASCADE, to_field='resume_file_name', related_name='comment_on_resume')









