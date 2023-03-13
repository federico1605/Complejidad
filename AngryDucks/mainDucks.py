'''
Este codigo es la solucion para el reto de beecrown de Angry duck's
se soluciono con fomrulas basicas de fisica cinematica, de forma
que se respetaron la logica de la parte fisica, se entregaron datos basicos 
para los calculo como lo fue el pi y la gravedad.
'''
from math import cos
from math import sin
pi =  3.14159
gravity = 9.80665
heightBegin = float(input()) 
p1,p2 = map(int,input().split()) #Acotacion de la ciudad
n = int(input()) # Numeros de intentos.
for attempts in range(n):
    angle,vo = map(float,input().split())
    angle = angle * pi / 180 # Se pasa el angulo a radianes para mantener todo en el mismo sistema de unidades
    vox= vo * cos(angle) 
    voy= vo * sin(angle)
    heightMax = (voy**2)/(gravity*2)
    vfy = pow(2*gravity*heightMax,1/2)
    tv = voy / gravity #Tiempo de vuelo
    tf = vfy / gravity #Tiempo de bajada
    tt = tv + tf #Tiempo total
    postionFinal = vox * tt
    result =  round(postionFinal, 5)

    if (p1 < result < p2):
        print(postionFinal," -> DUCK \n")
    else:
        print(postionFinal," -> NUCK \n")
