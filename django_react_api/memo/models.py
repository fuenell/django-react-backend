from django.db import models


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=2048)
    created = models.DateTimeField(auto_created=True, auto_now=True)

    def __str__(self):
        return self.title


class Test(models.Model):
    tt = models.CharField(max_length=128)

    def __str__(self):
        return self.tt
