from django.db import models


# Create your models here.

def upload_to_image(instance, filename):
    return '/'.join(['images', str(instance.email), filename])

def upload_to_resume(instance, filename):
    return '/'.join(['resumes', str(instance.email), filename])

class Members(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=50)
    major = models.CharField(max_length=50, blank=True)
    graduation_time = models.CharField(max_length=10, null=True)
    photo = models.ImageField(upload_to=upload_to_image, null=True, blank=True, validators=[])
    resume = models.FileField(upload_to=upload_to_resume, null=True, blank=True, validators=[], unique=True)

    def __str__(self):
        name = self.name
        id = self.id
        return f"Member {name=} {id=}"

class Officers(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.OneToOneField(Members, on_delete=models.CASCADE, to_field='email')
    bio = models.TextField()
    position = models.CharField(max_length=50)
    responsibility = models.TextField()

    def __str__(self):
        name = self.email
        id = self.id
        return f"Officer {email=} {id=}"

class Events(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length= 100)
    scheduled_date_time = models.DateTimeField()
    location = models.CharField(max_length= 100)
    host = models.ManyToManyField(Members)
    sponsor = models.CharField(max_length=100, blank=True)
    rsvp = models.IntegerField(default=0)

    def __str__(self):
        name = self.name
        id = self.id
        return f"Event {name=} {id=}"

class Comments(models.Model):

    id = models.AutoField(primary_key = True)
    content = models.TextField()
    email = models.ForeignKey(Members, on_delete=models.CASCADE, to_field='email', related_name='comment')
    recipient = models.ForeignKey(Members, on_delete=models.CASCADE, to_field='id', related_name='commented_by')

    def __str__(self):
        email = self.email
        id = self.id
        return f"Member {email=} {id=}"








