from django.db import models
from django.conf import settings
from django.db.models import Q
from django.db.models.signals import pre_save
from django.urls import reverse

from SHOP.utilities import unique_slug_generator, get_filename

# Create your models here.


class MerchandiseQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def on_sale(self):
        return self.filter(on_sale=True, active=True)


    def look_up(self, query):
    	lookups = (Q(title__icontains=query) | 
                  Q(description__icontains=query) |
                  Q(price__icontains=query) |
                  Q(label__title__icontains=query)
                  )
    	return self.filter(lookups).distinct


#It's extending defaults NOT overwriting
class MerchandiseManager(models.Manager):
    def get_queryset(self):
        return MerchandiseQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def on_sale(self): #Merchandise.objects.on_sale() 
        return self.get_queryset().on_sale()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id) #Merchandise.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

    def look_up(self, query):
    	return self.get_queryset().active().look_up(query)




class Merchandise(models.Model):
    title           = models.CharField(max_length=120)
    slug            = models.SlugField(blank=True, unique=True)
    description     = models.TextField()
    price           = models.DecimalField(decimal_places=2, max_digits=20, default=40.00)
    image           = models.ImageField(upload_to="merchandise/", null=True, blank=True)
    on_sale        	= models.BooleanField()
    active          = models.BooleanField(default=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    objects = MerchandiseManager()

    def __str__(self):
    	return self.title

    def get_absolute_url(self):
    	return "/merchandise/{slug}/".format(slug=self.slug)



def merchandise_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)
pre_save.connect(merchandise_pre_save_receiver, sender=Merchandise)






















