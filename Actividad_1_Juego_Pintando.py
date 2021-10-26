# 26/10/2021
# 01:01 pm

# Juego que dibuja figuras y lineas en puntos especificados en un plano
# Modificado por:
# Gabriel Sebastián Garibay Dávila
# Daniel Evaristo Escalera Bonilla
# Francisco Cruz Vázquez
# Juan Carlos Martínez Zacarías
# Carmina López Palacios

from turtle import *
from freegames import vector

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circle(start, end):
    r = end.x-start.x
    "Draw circle from start to end"
    up()
    goto(start.x, start.y) # Coloca la pluma en la posición inicial
    down()
    
    begin_fill()
    right(90) # Gira para mirar hacia abajo
    for count in range(360):
        forward(r/45) # Crea 360 lineas de una fracción del radio con ángulos de 1°
        left(1)
        
    left(90) # Gira para reiniciar el cursor
    end_fill()

def rectangle(start, end):
    "Draw rectangle from start to end."
    up()
    goto(start.x, start.y) # Coloca la pluma en la posición inicial
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.x) # Crea la linea horizontal, gira 90°
        left(90)
        forward(end.y - start.y) # Crea la linea vertical, gira 90°
        left(90)

    end_fill()

def triangle(start, end):
    "Draw triangle from start to end."
    up()
    goto(start.x, start.y) # Coloca la pluma en la posición inicial
    down()
    begin_fill()

    for count in range(3):
        forward(end.x - start.x) # Crea tres lineas de la medida especificada con ángulos de 120°
        left(120)
        
    end_fill()

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

"El progrma registra la tecla que se presióna y eso define la figura que se creará y su color"
state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('gray'), 'A') # Se agregó esta linea para incluir el color gris
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y') # Se agregó esta línea para incluir el color amarillo
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()