from django.db import models

# Create your models here.
class Forms(models.Model):
    name=models.CharField(max_length=122,null=True)
    text=models.CharField(max_length=122,null=True)
    def __str__(self):
        return self.name
