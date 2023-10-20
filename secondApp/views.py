from django.shortcuts import render

from django.shortcuts import render

def indexApp2(request, juego_id):
    juego = None

    if juego_id == 'valorant':
        juego = {
            "titulo": "Valorant",
            "tipo": "FPS",
            "plataforma": "PC",
            "peso": "23 GB Aprox",
            "multijugador": "Sí cuenta con multijugador",
            "imagen": 'imagenes/valorant.jpg',
        }
    elif juego_id == 'lol':
        juego = {
            "titulo": "League of Legends",
            "tipo": "MOBA",
            "plataforma": "PC",
            "peso": "Varía",
            "multijugador": "Sí cuenta con multijugador",
            "imagen": 'imagenes/lol.jpg',
        }
    elif juego_id == 'aoe':
        juego = {
            "titulo": "Age of Empires",
            "tipo": "Estrategia",
            "plataforma": "PC",
            "peso": "Varía",
            "multijugador": "Sí cuenta con multijugador",
            "imagen": 'imagenes/aoe.jpg',
        }

    return render(request, 'secondApp/indexApp2.html', {'juego': juego})