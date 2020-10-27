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
    #levantar pluma
    up()
    #se dirige a la primera posición
    goto(start.x, start.y)
    #baja la pluma para empezar a dibujar
    down()
    #rellenar área de color
    begin_fill()
    #Se dibujan 4 lineas con 90° de diferencia
    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circles(start, end):
    "Draw circle from start to end."
    #levantar pluma
    up()
    #se dirige a la primera posición
    goto(start.x, start.y)
    #baja la pluma para empezar a dibujar
    down()
    #rellenar área de color
    begin_fill()
    #funcion para crear circulo de radio (end.x-start.x)
    circle(end.x-start.x)
    end_fill()

def rectangle(start, end):
    "Draw rectangle from start to end."
    #levantar pluma
    up()
    #se dirige a la primera posición
    goto(start.x, start.y)
    #baja la pluma para empezar a dibujar
    down()
    #rellenar área de color
    begin_fill()
    
    #se repite dos veces para completar el rectángulo
    for count in range(2):
        #se mueve y dibuja la distancia entre el punto final y el inicial en x
        forward(end.x - start.x)
        #gira un ángulo de 90°
        left(90)
        #se mueve y dibuja la distancia entre el punto final y el inicial en y
        forward(end.y - start.y)
        #gira un ángulo de 90°
        left(90)
   
   #termina de dibujar     
    end_fill()

def triangle(start, end):
    "Draw triangle from start to end."
    #levantar pluma
    up()
    #se dirige a la primera posición
    goto(start.x, start.y)
    #baja la pluma para empezar a dibujar
    down()
    #rellenar área de color
    begin_fill()
    #se mueve y dibuja la distancia entre el punto final e inicial en x
    for count in range(3):
        forward(end.x - start.x)
        left(120)
        
    end_fill()
        

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']
#Se indican los puntos de start y end
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
#Se crea la ventana de dibujo
state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
#Declaración de los colores y formas
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('cyan'), 'C')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circles), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
