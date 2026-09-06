class No:
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.proximo = None


class ListaDuplamenteLigada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def Imprimir(self):
        n = self.primeiro
        while n:
            print(n.valor, end=" ")
            n = n.proximo
        print()

    def InserirInicio(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        if self.primeiro:
            self.primeiro.anterior = novo
        else:
            self.ultimo = novo
        self.primeiro = novo

    def InserirFinal(self, valor):
        novo = No(valor)
        novo.anterior = self.ultimo
        if self.ultimo:
            self.ultimo.proximo = novo
        else:
            self.primeiro = novo
        self.ultimo = novo

    def InserirMeio(self, valor, posicao):
        n = self.primeiro
        for i in range(posicao - 1):
            if n:
                n = n.proximo
        if not n or not n.proximo:
            self.InserirFinal(valor)
            return
        novo = No(valor)
        novo.anterior = n
        novo.proximo = n.proximo
        n.proximo.anterior = novo
        n.proximo = novo

    def RemoverInicio(self):
        if not self.primeiro:
            return
        self.primeiro = self.primeiro.proximo
        if self.primeiro:
            self.primeiro.anterior = None
        else:
            self.ultimo = None

    def RemoverFinal(self):
        if not self.ultimo:
            return
        self.ultimo = self.ultimo.anterior
        if self.ultimo:
            self.ultimo.proximo = None
        else:
            self.primeiro = None


lista = ListaDuplamenteLigada()
lista.InserirFinal(7)
lista.InserirFinal(14)
lista.InserirFinal(21)
lista.InserirInicio(3)
lista.InserirMeio(50, 2)
lista.Imprimir()
lista.RemoverInicio()
lista.RemoverFinal()
lista.Imprimir()
