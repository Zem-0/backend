from django.db import models

class Meeting(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.title
