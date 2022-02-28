from Monitor import *
from Teclado import *
from Raton import *
from Computadora import *
from Orden import *


teclado1=Teclado("hp","usb")
raton1=Raton("lenovo","usb")
monitor1=Monitor("samsung",50)
computadora1=Computadora("gamer",monitor1,teclado1,raton1)
computadora2=Computadora("gamer",monitor1,teclado1,raton1)
computadoras1=[computadora1,computadora2]
Orden1=Orden(computadoras1)
print(Orden1)