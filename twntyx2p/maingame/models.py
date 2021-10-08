from django.db import models
# Create your models here.
from twntyx2p.accounts.models import User


class UserGame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    total_time_run = models.FloatField(default=0.0)

    class Meta:
        ordering = ['created']