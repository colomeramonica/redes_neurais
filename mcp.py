class MCP:

    def __init__(self, w, limiar):
        self.w = []
        self.limiar = limiar
        for i in range(w):
            self.w[i] = w[i]

    def soma(self, x):
        soma = 0
        for i in range(self.w):
            soma += x[i] * self.w[i]

        return soma


    def Y(self, x):
        if (self.soma(x) >= self.limiar):
            return 1
            
        return 0

    