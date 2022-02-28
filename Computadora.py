from Monitor import *
from Teclado import *
from Raton import *


class Computadora:
    contadorComputadoras=0
    def __init__(self,nombre, monitor,teclado,raton):
        Computadora.contadorComputadoras+=1
        self._idComputadora=Computadora.contadorComputadoras
        self._nombre=nombre
        self._monitor=monitor
        self.teclado=teclado
        self.raton=raton
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre=nombre
    def __str__(self):
        return f"""\n\nidComputadora:{self._idComputadora}\nnombre:{self._nombre} 
        \nmonitor:{self._monitor}
        \nteclado:{self.teclado}
        \nraton:{self.raton}"""

if __name__ == "__main__":
    teclado1=Teclado("hp","usb")
    raton1=Raton("lenovo","usb")
    monitor1=Monitor("samsung",50)
    computadora1=Computadora("gamer",monitor1,teclado1,raton1)
    print(computadora1,computadora1)