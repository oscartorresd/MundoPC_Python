class Orden:
    contadorOrdenes = 0

    def __init__(self,compuadoras):
        Orden.contadorOrdenes += 1
        self._idOrden = Orden.contadorOrdenes
        self._computadoras=compuadoras

    def agregarComputadora(self, computadora):
        self._computadoras.append(computadora)

    @property
    def computadora(self):
        return self._computadora

    @computadora.setter
    def computadora(self, computadora):
        self._computadora = computadora

    def __str__(self):
        computadoras_str=""
        for computadora in self._computadoras:
            computadoras_str+=computadora.__str__()
        return f"\n[idOrden: {self._idOrden} \nComputadora:{computadoras_str}]"
