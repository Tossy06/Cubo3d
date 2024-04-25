from turtle import *

speed(0)



def dibujar_linea(p1, p2, p3, p4):
    penup()
    setpos(p1, p2)
    pendown()
    setpos(p3, p4)
    
def cuadrado(c1):
    
    dibujar_linea(c1[1][0], c1[1][1], c1[2][0], c1[2][1])
    dibujar_linea(c1[2][0], c1[2][1], c1[3][0], c1[3][1])
    dibujar_linea(c1[3][0], c1[3][1], c1[4][0], c1[4][1])
    dibujar_linea(c1[4][0], c1[4][1], c1[1][0], c1[1][1])
    

def vertice1 (x, y, t):
    global c1
    c1 = [[0,0], 
         [x + t/2, y + t/2], 
         [x + t/2, y - t/2],
         [x - t/2, y - t/2],
         [x - t/2, y + t/2],
        ]
    cuadrado(c1)
    
def vertice2 (x, y, t):
    global c2
    c2 = [[0,0], 
         [x + t/2, y + t/2], 
         [x + t/2, y - t/2],
         [x - t/2, y - t/2],
         [x - t/2, y + t/2],
        ]
    cuadrado(c2)
def unir (c1, c2):
    for i in range (1, 5):
        dibujar_linea(c1[i][0], c1[i][1], c2[i][0], c2[i][1])
    
x = 0
y = 0
vertice1(0, 0, 100)
vertice2(x + 25, y + 35, 100)
unir(c1, c2)


mainloop()
    