# cook your dish here
import math
for _ in range(int(input())):
    c,r=map(int,input().split())
    mvc=math.ceil(c/9)
    mvr=math.ceil(r/9)
    if mvr<=mvc:
        print(1,mvr)
    else:
        print(0,mvc)