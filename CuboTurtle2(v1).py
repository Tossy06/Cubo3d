from turtle import *

speed(0)

def dibujar_linea(p1, p2, p3, p4):
    penup()
    setpos(p1, p2)
    pendown()
    setpos(p3, p4)


def dibujar_cubo(t, ejeX, ejeY):
    dibujar_linea(t/4 + ejeX, t/4 + ejeY, t/2 + ejeX, t/2 + ejeY) # de 1 a 2
    dibujar_linea(ejeX - t/2 , t/4 + ejeY, ejeX - t/4 , t/2 + ejeY ) # de 6 a 7
    dibujar_linea(ejeX - t/4 , t/2 + ejeY, t/2 + ejeX, t/2 + ejeY ) # de 7 a 2
    dibujar_linea(ejeX - t/2 , t/4 + ejeY, t/4 + ejeX, t/4 + ejeY) # de 6 a 1
    dibujar_linea(t/4 + ejeX, t/4 + ejeY, t/4 + ejeX, ejeY - t/4) # de 1 a 4
    dibujar_linea(t/2 + ejeX, t/2 + ejeY, t/2 + ejeX, ejeY - t/20) # de 2 a 3
    dibujar_linea(t/2 + ejeX, ejeY - t/20, t/4 + ejeX, ejeY - t/4 ) # de 3 a 4
    dibujar_linea(ejeX - t/2 , t/4 + ejeY, ejeX -t/2, ejeY - t/4) # de 6 a 5
    dibujar_linea(ejeX - t/2, ejeY - t/4, t/4 + ejeX, ejeY - t/4 ) #de 5 a 4
    dibujar_linea(ejeX - t/4 , t/2 + ejeY, ejeX - t/4 , ejeY - t/20 ) # de 7 a 8
    dibujar_linea(ejeX - t/2, ejeY - t/4, ejeX - t/4 , ejeY - t/20 ) # de 5 a 8
    dibujar_linea( ejeX - t/4 , ejeY - t/20, t/2 + ejeX, ejeY - t/20 ) # de 8 a 3
dibujar_cubo(100, 0, 0)

mainloop()