class No:
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.proximo = None


class ListaDuplamenteLigada:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def Imprimir(self):
        if self.inicio == None:
            print("lista vazia")
            return
        atual = self.inicio
        texto = ""
        while atual != None:
            texto = texto + str(atual.valor) + " "
            atual = atual.proximo
        print(texto)

    def InserirFinal(self, valor):
        novo = No(valor)
        if self.inicio == None:
            self.inicio = novo
            self.fim = novo
        else:
            novo.anterior = self.fim
            self.fim.proximo = novo
            self.fim = novo

    def InserirInicio(self, valor):
        novo = No(valor)
        if self.inicio == None:
            self.inicio = novo
            self.fim = novo
        else:
            novo.proximo = self.inicio
            self.inicio.anterior = novo
            self.inicio = novo

    def InserirMeio(self, valor, posicao):
        if self.inicio == None:
            self.InserirFinal(valor)
            return
        atual = self.inicio
        contador = 0
        while contador < posicao and atual.proximo != None:
            atual = atual.proximo
            contador = contador + 1
        if atual == self.fim:
            self.InserirFinal(valor)
            return
        novo = No(valor)
        depois = atual.proximo
        novo.anterior = atual
        novo.proximo = depois
        atual.proximo = novo
        depois.anterior = novo

    def RemoverInicio(self):
        if self.inicio == None:
            print("lista vazia")
            return
        if self.inicio == self.fim:
            self.inicio = None
            self.fim = None
            return
        self.inicio = self.inicio.proximo
        self.inicio.anterior = None

    def RemoverFinal(self):
        if self.fim == None:
            print("lista vazia")
            return
        if self.inicio == self.fim:
            self.inicio = None
            self.fim = None
            return
        self.fim = self.fim.anterior
        self.fim.proximo = None


lista = ListaDuplamenteLigada()
lista.InserirFinal(10)
lista.InserirFinal(20)
lista.InserirFinal(30)
lista.InserirInicio(5)
lista.InserirMeio(99, 1)
lista.Imprimir()
lista.RemoverInicio()
lista.RemoverFinal()
lista.Imprimir()
