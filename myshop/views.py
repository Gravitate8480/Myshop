from django.shortcuts import render, redirect
from .forms import Formulario_producto
from .models import *


# Create your views here.
def home(request):
    
    return render(request, "myshop/inicio.html")


def registrar(request):
    if request.method == 'POST':
        form_full = Formulario_producto(request.POST)
        if form_full.is_valid():
            form_full.save()
            return redirect('listar_productos')
        else:
            print("Nose pudo guardar")
            return redirect('home')
            
           
    form = Formulario_producto()
    return render(request, 'myshop/registrar.html', {'form': form})


def listar_productos(request):
    
    productos = Product.objects.all()
    
    return render(request, 'myshop/lista.html', {'productos': productos})


def editar_producto(request, id):
    
    try:
        producto = Product.objects.get(pk=id)
        form = Formulario_producto(instance=producto)
    except:
        producto = None
        form = None
        print('error')
        
    if request.method == "POST":
        form = Formulario_producto(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            
            return redirect('listar_productos')
        else:
            print("Nose pudo guardar")
            return redirect('home')
        
    
    
    return render(request, 'myshop/editar.html', {'producto': producto, 'form': form})


def consultar(request, id):
    
    try:
        producto = Product.objects.get(pk=id)
    except:
        producto = None
        print('error')
        
    return render(request, "myshop/consultar.html", {'producto': producto})


def borrar_producto(request, id):
    
    try:
        producto = Product.objects.get(pk=id)
        producto.delete()
        return redirect('listar_productos')
    except:
        producto = None
        print('error')
        return redirect('home')
        
    return render(request)

def agregar_producto(request):
    print(request.POST['product_id'])
    product = Product.objects.get(pk=request.POST['product_id'])
    order = Order.objects.get(pk=request.POST['order_id'])
    
    try:
        order_detail = OrderDetail.objects.get(order=order, product=product)
    except:
        order_detail = OrderDetail.objects.create(order=order, product=product)
        
    order_detail.cuantity += 1
    order_detail.save()
    
    return redirect('listar_productos')


def carrito(request, order_id):
    order = Order.objects.get(pk = order_id)
    return render(request, 'myshop/carrito.html', {'order': order})


def finalizar_carrito(request):
    
    order = Order.objects.get(pk=request.POST['order_id'])
    order.status= 'terminado'
    order.save()
    del request.session['order_id']
    
    for detail in order.orderdetail_set.all():
        detail.product.stock -= detail.cuantity
        detail.product.save()
        
        
    return redirect('listar_ordenes')


def listar_ordenes(request):
    ordenes = Order.objects.filter(status='terminado')
    
    return render(request, 'myshop/lista_de_ordenes.html', {'ordenes': ordenes})
    