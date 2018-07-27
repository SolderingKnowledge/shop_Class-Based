from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.shortcuts import render, redirect

from merchandise.models import Merchandise
from .models import Cart


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request) 
    return render(request, "cart/index.html", {"cart": cart_obj})


def cart_update(request):
    merchandise_id = request.POST.get('merchandise_id')
    
    if merchandise_id is not None:
        try:
            merchandise_obj = Merchandise.objects.get(id=merchandise_id)
        except Merchandise.DoesNotExist:
            print("Merchandise is gone?")
            return redirect("cart:home")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if merchandise_obj in cart_obj.merchandises.all():
            cart_obj.merchandises.remove(merchandise_obj)
            added = False
        else:
            cart_obj.merchandises.add(merchandise_obj)
            added = True
        request.session['cart_items'] = cart_obj.merchandises.count()
    return redirect("cart:index")


