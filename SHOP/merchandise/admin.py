from django.contrib import admin
from .models import Merchandise

class MerchandiseAdmin(admin.ModelAdmin): #shows slugField in admin
	list_display = ['__str__', 'slug']
	class Meta:
		model = Merchandise

admin.site.register(Merchandise, MerchandiseAdmin)

