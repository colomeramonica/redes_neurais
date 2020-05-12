class Neuronio:

    def __init__(self, entradas, pesos):
        self.entradas = entradas
        self.pesos = pesos
        self.e = 2.7183

    def soma(self):
        soma = 0

        for i in range(self.pesos):
            soma += self.entradas[i] * self.pesos[i]

        return soma

    def ativacao(self, u):
        return 1 / (1 + pow(self.e, -u))

    def saida(self):
        return self.ativacao(self.soma())

    