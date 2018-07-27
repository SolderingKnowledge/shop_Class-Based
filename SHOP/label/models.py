from django.db import models
from django.db.models.signals import pre_save, post_save
from django.urls import reverse

from SHOP.utilities import unique_slug_generator
from merchandise.models import Merchandise


class Label(models.Model):
    title         = models.CharField(max_length=120)
    slug          = models.SlugField()
    timestamp     = models.DateTimeField(auto_now_add=True)
    active        = models.BooleanField(default=True)
    merchandises  = models.ManyToManyField(Merchandise, blank=True)

    def __str__(self):
        return self.title


def label_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(label_pre_save_receiver, sender=Label)