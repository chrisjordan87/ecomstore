from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from cart import cart


def show_cart(request, template_name="cart/cart.html"):
    if request.method == 'POST':
        post_data = request.POST.copy()
        if post_data['submit'] == 'Remove':
            cart.remove_from_cart(request)
        if post_data['submit'] == 'Update':
            cart.update_cart(request)
        if post_data['submit'] == 'Checkout':
            url = urlresolvers.reverse('show_checkout')
            return HttpResponseRedirect(url)

    cart_items = cart.get_cart_items(request)
    cart_item_count = cart.cart_distinct_item_count(request)
    cart_subtotal = cart.cart_subtotal(request)
    page_title = 'Shopping Cart'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))