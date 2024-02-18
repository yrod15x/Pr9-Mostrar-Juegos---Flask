#Programa que muestra una lista de video juegos cuando se hace click en una imagen de y titulo de la categoria que pertenecen

from flask import Flask, render_template, request

app = Flask(__name__)

juegos_accion = ['Red Dead Redemption 2', 'Sekiro: Shadows Die Twice', 'Bayonetta', 'Batman Arkham City','Hotline Miami', 'Devil May Cry 5', 'Monster Hunter World', 'Vanquish', 'Resident Evil 2', 'Grand Theft Auto V']

juegos_rpg = ['Disco Elysium', 'Chrono Trigger', 'The Witcher 3', 'Mass Effect 2', 'Fallout: New Vegas', 'Dark Souls', 'Baldur’s Gate 3', 'Deus Ex', 'Final Fantasy 7', 'The Elder Scrolls V: Skyrim']

juegos_deportes = ['Mike Tyson\'s Punch-Out', 'Tony Hawk\'s Pro Skater 2', 'Madden NFL 2004', 'Wii Sports', 'FIFA 10', 'NBA 2K11', 'Tecmo Super Bowl', 'MVP Baseball 2005', 'NBA Jam', 'Mario Tennis 64']

juegos_mmo = ['World Of Warcraft', 'Final Fantasy 14', 'Elder Scrolls Online', 'Star Wars: The Old Republic', 'EVE Online', 'Guild Wars 2', 'Lord Of The Rings Online', 'Runescape', 'Rift', 'EverQuest']

juegos_estrategia = ['Battle Brothers', 'Fire Emblem: Three Houses', 'XCOM 2', 'Civilization 6', 'Wargame: Red Dragon', 'Crusader Kings 3', 'Unity of Command 2', 'This War of Mine', 'Total War: Shogun 2', 'Slay the Spire']

juegos_indie = ['Minecraft', 'Inside', 'Cuphead', 'Braid', 'Spelunky', 'Darkest Dungeon', 'Undertale', 'Crypt Of The Necrodancer', 'Hotline Miami', 'Limbo']

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', titulo = "VideoJuegos Por Genero")

#<genero> es la variable que lleva en enlace en su href mediante la funcion url-for en el archivo index.html -> {{ url_for('mostrar', genero = 'accion') }}  accion es el valor de la variable. Uso enlaces en vez de botones y forms para ejecutar las funcioines aqui en flask
@app.route("/mostrar/<genero>")
def mostrar(genero):
    if genero == 'accion':
        return render_template('mostrar.html', titulo = "VideoJuegos De Accion",juegos = juegos_accion)
    elif genero == 'rpg':
        return render_template('mostrar.html', titulo = "VideoJuegos De RPG",juegos = juegos_rpg)
    elif genero == 'sports':
        return render_template('mostrar.html', titulo = "VideoJuegos De Deportes",juegos = juegos_deportes)
    elif genero == 'mmo':
        return render_template('mostrar.html', titulo = "VideoJuegos Online MMO",juegos = juegos_mmo)
    elif genero == 'estrategia':
        return render_template('mostrar.html', titulo = "VideoJuegos De Estrategias",juegos = juegos_estrategia)
    elif genero == 'indies':
        return render_template('mostrar.html', titulo = "VideoJuegos Indies",juegos = juegos_indie)
    else:
        return render_template('index.html', titulo = "VideoJuegos Por Genero")

if __name__ == '__main__':
    app.run()