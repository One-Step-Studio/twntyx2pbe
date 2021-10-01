from django.db import models


# Create your models here.
class GameInstance(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    total_time_run = models.DateTimeField()

    class Meta:
        ordering = ['created']
