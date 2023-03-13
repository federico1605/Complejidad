'''
Este codigo es la solucion para el reto de beecrown de Angry duck's
se soluciono con fomrulas basicas de fisica cinematica, de forma
que se respetaron la logica de la parte fisica, se entregaron datos basicos 
para los calculo como lo fue el pi y la gravedad.
'''
import math
pi =  3.14159
gravity = 9.80665
while True:
    try:
        heightBegin = float(input()) 
        p1,p2 = map(int,input().split()) #Acotacion de la ciudad
        n = int(input()) # Numeros de intentos.
        for attempts in range(n):
            angle,vo = map(float,input().split())
            angle = angle * pi / 180 # Se pasa el angulo a radianes para mantener todo en el mismo sistema de unidades
            vox= vo * math.cos(angle) 
            voy= vo * math.sin(angle)
            heightMax = (voy**2)/(gravity*2) + heightBegin
            vfy = (2*gravity*heightMax)**0.5
            tv = voy / gravity #Tiempo de vuelo
            tf = vfy / gravity #Tiempo de bajada
            tt = tv + tf #Tiempo total
            postionFinal = vox * tt
            print("{:.5f} -> DUCK".format(postionFinal)) if p1 < postionFinal < p2 else print("{:.5f} -> NUCK".format(postionFinal))
    except EOFError:
        break
