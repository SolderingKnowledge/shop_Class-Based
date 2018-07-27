from django.http import Http404
from django.shortcuts import render
from django.db.models import Q
from .models import Merchandise
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from cart.models import Cart


# Create your views here.






class MerchandiseOn_SaleList(ListView):
    template_name = "list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Merchandise.objects.all().on_sale()


class MerchandiseOn_SaleDetail(DetailView):
    queryset = Merchandise.objects.all().on_sale()
    template_name = "saleDetail.html"



class MerchandiseList(ListView):
    template_name = "list.html"


    def get_context_data(self, *args, **kwargs):
        context = super(MerchandiseList, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Merchandise.objects.all()


class MerchandiseDetail(DetailView):
    template_name = "detail.html"

    def get_context_data(self, *args, **kwargs):  #every CBV has this one to get context
        context = super(MerchandiseDetail, self).get_context_data(*args, **kwargs)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Merchandise.objects.get_by_id(pk)
        if instance is None:
            raise Http("Sorry, merchandise not found")
        return instance


class MerchandiseDetailSlug(DetailView):
    queryset = Merchandise.objects.all()
    template_name = "detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(MerchandiseDetailSlug, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context


    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')

        try:
            instance = Merchandise.objects.get(slug=slug, active=True)
        except Merchandise.DoesNotExist:
            raise Http404("Merchandise not found")
        except Merchandise.MultipleObjectsReturned:
            qs = Merchandise.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("This an error i wrote ")
        return instance































