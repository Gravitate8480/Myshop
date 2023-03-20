import datetime
from .models import Order

def set_cart(request):
    try:
        order = Order.objects.get(pk = request.session['order_id'])
        print(f"---- order encontrada, id: {order.id}")
    except:
        order = Order.objects.create(status='carrito')
        request.session['order_id'] = order.id
        print(f'---- order creada, id: {order.id}')
        
    print(f"--- orderrrr: {order.id}")
    
    cart_count = order.orderdetail_set.count()
        
    return { 'order_id': order.id, 'count': cart_count }
