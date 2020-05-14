from django.db import models

# Create your models here.
class PollutionEntry(models.Model):
    date_time = models.DateTimeField(name='date/time')
    pm2_5 = models.FloatField(name='pm 2.5 level')
    pm10_mask = models.FloatField(name='pm 10 mask level')
    retrospective = models.BooleanField()

    def __str__(self):
        return self.date_time.__str__() + ': ' + self.pm2_5