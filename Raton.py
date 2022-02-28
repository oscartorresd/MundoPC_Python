from DispositivoEntrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    contadorRatones = 0

    def __init__(self,tipoEntrada, marca):
        Raton.contadorRatones+=1
        self._idRaton = Raton.contadorRatones
        super().__init__(tipoEntrada,marca)


    def __str__(self):
        return f"\nidRaton:[{self._idRaton}\ntipoEntrada:{self._tipoEntrada}\nmarca:{self._marca}]"

if __name__ == "__main__":
    raton1=Raton("usb","logitech")
    print(raton1)
    raton2=Raton("usb","ari")
    print(raton2)