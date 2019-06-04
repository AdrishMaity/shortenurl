from django.db import models
from django.core.validators import URLValidator

# Create your models here.
class ShortenURL(models.Model):

    class Meta:
        verbose_name_plural = "Shorten URL"

    def __str__(self):
        return self.id + '_' + self.linkTitle

    linkTitle = models.CharField(max_length=100, default="A Site")
    urlToBeShortened = models.CharField(max_length=500, validators=[URLValidator()])
    shortenedUrl = models.CharField(max_length=300, validators=[URLValidator()])
