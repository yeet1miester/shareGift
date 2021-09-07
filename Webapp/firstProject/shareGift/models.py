from django.db import models

class RSVP(models.Model):
    total = models.IntegerField(null=True)
    count = models.IntegerField(null=True)
    dates = models.CharField(null=True, max_length=500)

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.dates)