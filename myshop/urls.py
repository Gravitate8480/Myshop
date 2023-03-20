from django.urls import path
from . import views as vw


urlpatterns = [
    path('', vw.home, name='home'),
    path('registrar', vw.registrar, name='registrar'),
    path('editar/<int:id>', vw.editar_producto, name='editar'),
    path('consultar/<int:id>', vw.consultar, name='consultar'),
    path('lista-productos', vw.listar_productos, name='listar_productos'),
    path('borrar-producto/<int:id>', vw.borrar_producto, name='borrar_producto'),
    path('agregar-producto', vw.agregar_producto, name='agregar_producto'),
    path('carrito/<int:order_id>', vw.carrito, name='carrito'),
    path('finalizar-carrito', vw.finalizar_carrito, name='finalizar_carrito'),
    #path('ordenar/<int:id>', vw.ordenar, name='ordenar'),
    # path('registrar-orden/', vw.registrar_orden, name='registrar_orden'),
    # path('editar-orden/', vw.editar_orden, name='editar_orden'),
    # path('eliminar-orden/', vw.eliminar_orden, name='eliminar_orden'),
    # path('cunsultar-rorden/<int:id>/', vw.consultar_orden, name='consultar_orden'),
    path('listar-ordenes', vw.listar_ordenes, name='listar_ordenes')
]