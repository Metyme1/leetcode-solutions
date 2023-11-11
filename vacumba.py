import math

n= int(input())

for _ in range(n):
    m = int(input())
    x, y = 0,0
    for _ in range(m):
       a, d = map(float, input().split())
       a+=90
       rad = math.radians(a)
       x+= d * math.cos(rad)
       y+= d * math.sin(rad)

    print(f"{x:.6f} {y:.6f}")