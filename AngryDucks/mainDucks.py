import math
pi =  3.14159
gravity = 9.80665
while True:
    try:
        heightBegin = float(input())
        p1,p2 = map(int,input().split())
        n = int(input())
        for attempts in range(n):
            angle,vo = map(float,input().split())
            angle = angle * pi / 180
            vox= vo * math.cos(angle)
            voy= vo * math.sin(angle)
            heightMax = (voy**2)/(gravity*2) + heightBegin
            vfy = (2*gravity*heightMax)**0.5
            tv = voy / gravity
            tf = vfy / gravity
            tt = tv + tf
            postionFinal = vox * tt
            print("{:.5f} -> DUCK".format(postionFinal)) if p1 < postionFinal < p2 else print("{:.5f} -> NUCK".format(postionFinal))
    except EOFError:
        break
