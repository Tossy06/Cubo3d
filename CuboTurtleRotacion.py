from turtle import *
import math
import time

speed(0)
delay(0)
tracer(0)  # Desactivar actualizaciones automáticas de la pantalla

def dibujar_linea(p1, p2, p3, p4):
    width(2)  # Ajustar el grosor de las líneas
    penup()
    setpos(p1, p2)
    pendown()
    setpos(p3, p4)

def cuadrado(c1):
    dibujar_linea(c1[1][0], c1[1][1], c1[2][0], c1[2][1])
    dibujar_linea(c1[2][0], c1[2][1], c1[3][0], c1[3][1])
    dibujar_linea(c1[3][0], c1[3][1], c1[4][0], c1[4][1])
    dibujar_linea(c1[4][0], c1[4][1], c1[1][0], c1[1][1])

def vertice1(x, y, t):
    global c1
    c1 = [[0,0], 
         [x + t/2, y + t/2], 
         [x + t/2, y - t/2],
         [x - t/2, y - t/2],
         [x - t/2, y + t/2],
        ]
    cuadrado(c1)
    
def vertice2(x, y, t):
    global c2
    c2 = [[0,0], 
         [x + t/2, y + t/2], 
         [x + t/2, y - t/2],
         [x - t/2, y - t/2],
         [x - t/2, y + t/2],
        ]
    cuadrado(c2)

def unir(c1, c2):
    for i in range(1, 5):
        dibujar_linea(c1[i][0], c1[i][1], c2[i][0], c2[i][1])

# Punto fijo alrededor del cual se va a rotar el cubo
punto_fijo = (0, 0)

# Función para rotar el cubo alrededor del punto especificado
def rotar_cubo():
    global c1, c2
    angulo_rotacion = 0
    while True:
        # Rotación del cubo
        c1_rotado = rotar_cara(c1, angulo_rotacion, punto_fijo)
        c2_rotado = rotar_cara(c2, angulo_rotacion, punto_fijo)
        
        # Dibujar el cubo rotado
        clear()
        cuadrado(c1_rotado)
        cuadrado(c2_rotado)
        unir(c1_rotado, c2_rotado)
        update()  # Actualizar la pantalla
        
        # Ajustar la velocidad de rotación
        angulo_rotacion += 1
        if angulo_rotacion >= 360:
            angulo_rotacion -= 360
        time.sleep(0.01)  # Pausa para suavizar la animación

# Función para rotar una cara del cubo alrededor del punto especificado
def rotar_cara(cara, angulo, punto):
    cara_rotada = []
    for punto_cara in cara:
        punto_rotado = rotar_punto(punto_cara, angulo, punto)
        cara_rotada.append(punto_rotado)
    return cara_rotada

# Función para rotar un punto alrededor de otro punto
def rotar_punto(punto, angulo, punto_fijo):
    x, y = punto
    cx, cy = punto_fijo
    angulo_rad = math.radians(angulo)
    new_x = (x - cx) * math.cos(angulo_rad) - (y - cy) * math.sin(angulo_rad) + cx
    new_y = (x - cx) * math.sin(angulo_rad) + (y - cy) * math.cos(angulo_rad) + cy
    return [new_x, new_y]

# Configuración inicial
x = 0
y = 0
t = 100

vertice1(0, 0, t)
vertice2(x + 25, y + 35, t)

# Iniciar la rotación del cubo
rotar_cubo()
