from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=False)
    tweet = models.CharField(max_length=320)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

