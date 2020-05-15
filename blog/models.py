from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now=False)
    tweet = models.CharField(max_length=320)
    url = models.URLField(blank=True)

