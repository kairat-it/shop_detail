from django.template.loader import render_to_string
from django.urls import reverse
from carts.models import Cart
from carts.utils import get_user_carts


class CartMixin:
    def get_cart(self, request, part=None, cart_id=None):

        if request.user.is_authenticated:
            query_kwargs = {"user": request.user}
        else:
            if not request.session.session_key:
                request.session.create()
            query_kwargs = {"session_key": request.session.session_key}

        if part:
            query_kwargs["part"] = part
        if cart_id:
            query_kwargs["id"] = cart_id

        return Cart.objects.filter(**query_kwargs).first()

    def render_cart(self, request):
        user_cart = get_user_carts(request)
        context = {"carts": user_cart}

        referer = request.META.get("HTTP_REFERER")
        if reverse("order:order_create") in referer:
            context["order"] = True

        return render_to_string(
            "cart/includes/included_cart.html", context, request=request
        )
