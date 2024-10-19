import math
from turtle import *

def hearta(k):
    return 15*math.sin(k)**3
def heartb(k):
    return 12*math.cos(k)-5*\
    math.cos(2*k)-2*\
    math.cos(3*k)-\
    math.cos(4*k)
speed(0)
bgcolor("#080202")
for x in range(6000):
    goto(hearta(x)*20,heartb(x)*20)
    for y in range(5):
        color("#FF4191")
    goto(0,0)
done()