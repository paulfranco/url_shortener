from django.db import models

# Create your models here.
from apps.shortener.models import LftURL

class ClickEventManager(models.Manager):
    def create_event(self, lftInstance):
        if isinstance(lftInstance, LftURL):
            obj, created = self.get_or_create(lft_url=lftInstance)
            obj.count += 1
            obj.save()
            return obj.count
        return None

class ClickEvent(models.Model):
    lft_url     = models.OneToOneField(LftURL)
    count       = models.IntegerField(default=0)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects     = ClickEventManager()
    
    def __str__(self):
        return "{i}".format(i=self.count)