from django.db import models


class Experience(models.Model):
    title = models.CharField(max_length=500)
    institute = models.CharField(max_length=500)
    body = models.TextField()
    year = models.CharField(max_length=2000)

    def __str__(self):
        return self.title

