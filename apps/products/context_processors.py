from .models import *
from django.db.models import Sum

def order_item_context_processors(request):
    if request.user.is_authenticated:
        order_item_count = OrderItem.objects.filter(user=request.user, is_done=False).aggregate(Sum('quantity'))
        return {"order_item_count": order_item_count['quantity__sum']}
    else:
        return {"order_item_count": 0}
