from math import cos
from math import sin
pi =  3.14159
gravity = 9.80665
heightBegin = float(input())
p1,p2 = map(int,input().split())
n = int(input())
for attempts in range(n):
    angle,vo = map(float,input().split())
    angle = angle * pi / 180
    vox= vo * cos(angle)
    voy= vo * sin(angle)
    heightMax = (voy**2)/(gravity*2)
    vfy = pow(2*gravity*heightMax,1/2)
    tv = voy / gravity
    tf = vfy / gravity
    tt = tv + tf
    postionFinal = vox * tt
    result =  round(postionFinal, 5)

    if (p1 < result < p2):
        print(postionFinal," -> DUCK \n")
    else:
        print(postionFinal," -> NUCK \n")
