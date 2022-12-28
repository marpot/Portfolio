from django.db import models
# Create your models here.

class About(models.Model):
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="about")

    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"

    def __str__(self):
        return "About me"

#Service model
class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="Service name")
    description = models.TextField(verbose_name="About service")

    def __str__(self):
        return self.name

#Recent Work Model
class RecentWork(models.Model):
    title = models.CharField(max_length=100, verbose_name="Work title")
    image = models.ImageField(upload_to="works")

    def __str__(self):
        return self.title

#Client model
class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Client name")
    description = models.TextField(verbose_name="Client say")
    image = models.ImageField(upload_to="clients",default="default.png")

    def __str__(self):
        return self.name

#Job model
class Job(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    image = models.FilePathField(path="images/")
    github_url = models.URLField(max_length=100, null=True)

#Blog model
class Blog(models.Model):
    title = models.CharField(max_length=255)
    publish_date = models.DateTimeField()
    content = models.TextField()
    image = models.ImageField(upload_to='images/')

class Project(models.Model):
    title = models.CharField(max_length=255)
    technology = models.CharField(max_length=255)
    project = models.DateTimeField()
    github_url = models.CharField(max_length=255)

