from django.shortcuts import render
from django.views.generic import ListView
from merchandise.models import Merchandise


class LookUpMerchandiseList(ListView):
	template_name = "look_up/view.html"

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		query = self.request.GET.get('q')
		context['query'] = query
		return context

	def get_queryset(self, *args, **kwargs):
	    request = self.request
	    query = request.GET.get('q', None)
	    if query is not None:
	        return Merchandise.objects.look_up(query)
	    return Merchandise.objects.on_sale()
