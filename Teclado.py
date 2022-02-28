from DispositivoEntrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contadorTeclados = 0

    def __init__(self,tipoEntrada, marca):
        Teclado.contadorTeclados += 1
        self._idTeclado = Teclado.contadorTeclados
        super().__init__(tipoEntrada,marca)


    def __str__(self):
        return f"\nidTeclado:[{self._idTeclado}\nmarca:{self._marca}\ntipoEntrada:{self._tipoEntrada}]"

if __name__ == "__main__":
    teclado1=Teclado("usb","lenovo")
    print(teclado1)
    teclado2 = Teclado("linea", "hp")
    print(teclado2)