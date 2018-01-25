from django.db import models

from .utils import code_generator, create_shortcode

class LftURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs = super(LftURLManager, self).all(*args, **kwargs)
        qs = qs.filter(active=True)
        return qs
    def refresh_shortcodes(self, items=None):
        qs = LftURL.objects.filter(id_gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.id)
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i=new_codes)

class LftURL(models.Model):
    url = models.CharField(max_length=220, )
    #shortcode = models.CharField(max_length=15)
    #shortcode = models.CharField(max_length=15, null=True) # Empty in database is ok
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    #empty_datetime = models.DateTimeField(auto_now=False, auto_now_add=False)

    objects = LftURLManager()
    #some_random = LftURLManager()

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(LftURL, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)


    '''
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    '''