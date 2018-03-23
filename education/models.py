from django.db import models


class Education(models.Model):
    # Institute name
    institute = models.CharField(max_length=500)
    # Degree name
    title = models.CharField(max_length=2000)
    # CGPA
    cgpa = models.CharField(max_length=2000)
    # Attended from
    year = models.CharField(max_length=2000)
    def __str__(self):
        return self.title

