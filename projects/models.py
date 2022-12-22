from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    image = models.FilePathField(path="images/")
    github_url = models.URLField(max_length=100, null=True)


class Blog(models.Model):
    title = models.CharField(max_length=255)
    publish_date = models.DateTimeField()
    content = models.TextField()
    image = models.ImageField(upload_to='images/')