from mcp import MCP
from neuronio import Neuronio

class Rede_Neural:

    def __init__(self, entradas, res_esperado, pesos_h, pesos_o):
        self.entradas = entradas
        self.res_esperado = res_esperado
        self.pesos_h = pesos_h
        self.pesos_o = pesos_o
        self.taxa_aprendizado = 0.2
        self.h1 = []
        self.h2 = []
        self.delta_h1 = [0, 0, 0]
        self.delta_h2 = [0, 0, 0]
        self.delta_o1 = [0, 0, 0]
        self.delta_o2 = [0, 0, 0]
        self.resultadoN1 = []
        self.resultadoN2 = []
        self.e = 2.7183


    def getMSE(self):
        for (idx, val) in range(self.entradas): # percorrendo as entradas
            neuronio = Neuronio(val, self.pesos_h[0])
            self.h1 = neuronio.saida()

            neuronio = Neuronio(val, self.pesos_h[1])
            self.h2 = neuronio.saida()

            u1 = self.pesos_o[0][0] + self.h1[idx] * self.pesos_o[0][1] + self.h2[idx] * self.pesos_o[0][2]
            u2 = self.pesos_o[0][0] + self.h1[idx] * self.pesos_o[1][1] + self.h2[idx] * self.pesos_o[1][2]

            self.resultadoN1 = 1 / (1 + pow(self.e, -u1))
            self.resultadoN2 = 1 / (1 + pow(self.e, -u2))

