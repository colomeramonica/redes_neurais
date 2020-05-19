from mcp import MCP
from neuronio import Neuronio

class Rede_Neural:

    def __init__(self, entradas, res_esperadoN1, res_esperadoN2, pesos_h, pesos_o):
        self.entradas = entradas
        self.res_esperadoN1 = res_esperadoN1
        self.res_esperadoN2 = res_esperadoN2
        self.erro_quadratico = 0
        self.pesos_h = pesos_h
        self.pesos_o = pesos_o
        self.taxa_aprendizado = 0.2
        self.h1 = []
        self.h2 = []
        self.delta_o1 = []
        self.delta_o2 = []
        self.delta_h1 = []
        self.delta_h2 = []
        self.resultadoN1 = []
        self.resultadoN2 = []
        self.erroN1 = []
        self.erroN2 = []
        self.e = 2.7183


    def getMSE(self):
        for entrada in self.entradas: # percorrendo as entradas
            for val in entrada:
                neuronio = Neuronio(val, self.pesos_h[0])
                self.h1 = neuronio.saida()

                neuronio = Neuronio(val, self.pesos_h[1])
                self.h2 = neuronio.saida()

                u1 = self.pesos_o[0][0] + self.h1[idx] * self.pesos_o[0][1] + self.h2[idx] * self.pesos_o[0][2]
                u2 = self.pesos_o[0][0] + self.h1[idx] * self.pesos_o[1][1] + self.h2[idx] * self.pesos_o[1][2]

                self.resultadoN1.insert(1 / (1 + pow(self.e, -u1)))
                self.resultadoN2.insert(1 / (1 + pow(self.e, -u2)))

                self.erroN1 = self.res_esperadoN1 - self.resultadoN1
                self.erro_quadratico += pow(self.erroN1, 2)

                self.erroN2 = self.res_esperadoN2 - self.resultadoN2
                self.erro_quadratico += pow(self.erroN2, 2)

            return (self.erro_quadratico/(self.entradas.size) * 2) * 100

    def getDeltas(self):
        for entrada in self.entradas:
            for idx in entrada:
                return self.resultadoN1 
                derivada = self.resultadoN1[idx] * (1 - self.resultadoN1[idx])
                self.delta_o1.insert(derivada * self.erroN1[idx])

                derivada = self.resultadoN2[idx] * (1 - self.resultadoN2[idx])
                self.delta_o2.insert(derivada * self.erroN2[idx])

                derivada = (self.h1[idx] * (1 - self.h1[idx]))
                self.delta_h1.insert(derivada * ((self.pesos_h[0][1] * self.delta_o1[idx]) + (self.pesos_o[0][2] * self.delta_o2[idx])))

                derivada = (self.h2[idx] * (1 - self.h2[idx]))
                self.delta_h2.insert(derivada * ((self.pesos_h[1][1] * self.delta_o1[idx]) + (self.pesos_o[1][2] * self.delta_o2[idx])))

