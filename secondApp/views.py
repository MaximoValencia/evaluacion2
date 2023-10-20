from django.shortcuts import render

def indexApp2(request):
    return render(request,'templatesJuegos/indexApp2.html')   

def valorant(request):
    data={
        "titulo":"Valorant",
        'tipo':"tipo FPS.",
        'plataforma':"PC",
        'peso':"23 GB Aprox",
        'multijugador':"Si cuenta con multijugador",
        'imagen':'imagenes/producto.jpg'
    }
    return render(request,'templatesJuegos/juegos.html',data)

def lol(request):
    data={
        "titulo":"League of Legends",
        'tipo':"MMORPG",
        'plataforma':"PC",
        'peso':"15 GB aprox",
        'multijugador': "si cuenta con multijugador"
    }
    return render(request,'templatesJuegos/juegos.html',data)

def aoe(request):
    data={
        "titulo":"Age of Empires 2",
        'tipo':"Estrategia",
        'plataforma':"PC",
        'peso':"30 GB Aprox",
        'multijugador': "Si cuenta con multijugador"
    }
    return render(request,'templatesJuegos/juegos.html',data)