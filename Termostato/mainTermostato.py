t = int(input())  # Cantidad de veces que va a calcular
result = []
for i in range(t):
    l,r,x = map(int,input().split())
    a,b = map(int,input().split())
    if a == b:
        result.append(0)
    elif abs(a - b) >= x:
        result.append(1)
    elif r - max(a,b) >= x or min(a, b) - l >= x:
        result.append(2)
    elif r - min(a, b) >= x and max(a,b) - l >= x:
        result.append(3)
    else:
        result.append(-1)
for temp in result:
    print(temp)