from django.shortcuts import render

def index(request):
    return render(request,'templatesJuegos/index.html')   

def valorant(request):
    data={
        "titulo":"Valorant",
        'producto1':"MAC",
        'producto2':"Celular",
        'producto3':"PlayStation",
        'url':'/www.inacap.cl',
        'imagen':'imagenes/producto.jpg'
    }
    return render(request,'templatesProductos/productos.html',data)

def lol(request):
    data={
        "titulo":"League of Legends",
        'producto1':"Pelota",
        'producto2':"Figura de Acción",
        'producto3':"Juego de Mesa",
        'imagen':'imagenes/producto.jpg'
    }
    return render(request,'templatesProductos/productos.html',data)

def aoe(request):
    data={
        "titulo":"Age of Empires 2",
        'producto1':"Polera",
        'producto2':"Chaqueta",
        'producto3':"Zapatilla",
        'imagen':'imagenes/producto.jpg'
    }
    return render(request,'templatesProductos/productos.html',data)