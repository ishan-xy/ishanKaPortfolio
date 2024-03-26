from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ImageField(upload_to='projects/images', default='')
    githubLink = models.URLField(max_length=200, null = True, blank = True, default='')
    demoLink = models.URLField(max_length=200, null = True, blank = True, default='')

    def __str__(self):
        return self.title