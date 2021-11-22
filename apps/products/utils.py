import json
from django.conf import settings
from .models import *
from django.core.mail import EmailMessage, send_mail


def cookieCart(request):
    # Create empty cart for now for non-logged in user
    try:
        cart = json.loads(request.COOKIES["cart"])
    except:
        cart = {}
        print("CART:", cart)

    items = []
    order = {"get_cart_total": 0, "get_cart_items": 0, "shipping": False}
    cartItems = order["get_cart_items"]
    # cartItems = len(cart)

    for i in cart:
        # We use try block to prevent items in cart that may have been removed from causing error
        try:
            cartItems += cart[i]["quantity"]

            product = Product.objects.get(id=i)
            total = product.price * cart[i]["quantity"]

            order["get_cart_total"] += total
            order["get_cart_items"] += cart[i]["quantity"]

            item = {
                "id": product.id,
                "product": {
                    "id": product.id,
                    "name": product.name,
                    "price": product.price,
                    "imageURL": product.imageURL,
                },
                "quantity": cart[i]["quantity"],
                "digital": product.digital,
                "get_total": total,
            }
            items.append(item)

            if product.digital == False:
                order["shipping"] = True
        except:
            pass
    return {"cartItems": cartItems, "order": order, "items": items}


def cartData(request):
    if request.user.is_authenticated:
        # import pdb
        # pdb.set_trace()
        # customer = request.user.customer
        user = request.user
        # order, created = Order.objects.get_or_create(customer=customer, complete=False)
        order = Order.objects.filter(user_id=user.id, complete=False).first()
        # order, created = Order.objects.get_or_create(user_id=user.id, complete=False)
        order_item = OrderItem.objects.filter(user_id=request.user.id, is_done=False)
        if order_item:
            # items = order.orderitem_set.all().order_by('id')
            items = order_item.all().order_by('id')
            # cartItems = order_item.get_cart_items
            cartItems = sum([item.quantity for item in order_item])
        else:
            cookieData = cookieCart(request)
            cartItems = cookieData["cartItems"]
            order = cookieData["order"]
            items = cookieData["items"]

    return {"cartItems": cartItems, "order": order, "items": items}


def get_cart_total(self):
    orderitems = self.orderitem_set.all()
    total = sum([item.get_total for item in orderitems])
    return float(format(total, ".2f"))


# def guestOrder(request, data):
#     customer_name = data["form"]["customer_name"]
#     email = data["form"]["email"]

#     cookieData = cookieCart(request)
#     items = cookieData["items"]

#     customer, created = Customer.objects.get_or_create(
#         email=email,
#     )
#     # todo: add new code
#     customer.user = request.user
#     customer.name = customer_name
#     customer.save()

#     order = Order.objects.create(
#         customer=customer,
#         complete=False,
#     )

#     for item in items:
#         product = Product.objects.get(id=item["id"])
#         orderItem = OrderItem.objects.create(
#             product=product,
#             order=order,
#             quantity=item["quantity"],
#         )
#     return customer, order


import re

from django.db.models import Q


def normalize_query(
        query_string,
        findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
        normspace=re.compile(r"\s{2,}").sub,
):
    """Splits the query string in invidual keywords, getting rid of unecessary spaces
    and grouping quoted words together.
    Example:

    >>> normalize_query('  some random  words "with   quotes  " and   spaces')
    ['some', 'random', 'words', 'with quotes', 'and', 'spaces']

    """
    return [normspace(" ", (t[0] or t[1]).strip()) for t in findterms(query_string)]


def get_query(query_string, search_fields):
    """Returns a query, that is a combination of Q objects. That combination
    aims to search keywords within a model by testing the given search fields.

    """
    query = None  # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None  # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query


# todo: new code
def get_or_create_customer(request, data):
    if request.user.user_type == 'Customer':
        print(request.user.user_type)
        customer_ins = Customer.objects.filter(user_id=request.user.id).first()
        print(customer_ins)
        customer_name = customer_ins.name
        customer_id = customer_ins.id
    else:
        customer_name_n_id = data["form"]["customer_name"]
        customer_id = customer_name_n_id.split('+')[1]
        customer_name = customer_name_n_id.split('+')[0]

    email = data["form"]["email"]
    cookieData = cookieCart(request)
    items = cookieData["items"]

    customer, created = Customer.objects.get_or_create(id=int(customer_id))
    # todo: add new code
    # customer.user = request.user
    customer.name = customer_name
    if email.strip() != '':
        customer.email = email
    customer.save()
    return customer


def send_contact_email(request):
    # mail_subject = "New contact from client."
    message = 'New contact from client: {0}.\nMessage: {1}\nEmail: {2}'.format(request.POST.get('name'),
                                                                               request.POST.get('message'),
                                                                               request.POST.get('email'))
    try:
        # send_mail(subject=request.POST.get('subject'), message=message, from_email=settings.DEFAULT_FROM_EMAIL,
        #           recipient_list=[settings.INTERNAL_EMAIL], auth_user=settings.EMAIL_HOST_USER,
        #           auth_password=settings.EMAIL_HOST_PASSWORD)
        email = EmailMessage(subject=request.POST.get('subject'), body=message, to=[settings.INTERNAL_EMAIL])
        email.send()
        return True
    except Exception as e:
        print(e)
        return False
