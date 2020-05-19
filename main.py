from rede import Rede_Neural
from neuronio import Neuronio
from mcp import MCP

entradas = [[1,0,0], [1,0,1], [1,1,0], [1,1,1]]
res_esperado1 = [0,1,1,0]
res_esperado2 = [1,0,0,1]
pesos_h = [[-0.46,-0.7,0.22],[0.10,0.94,0.46]]
pesos_o = [[0.78,-0.22,0.58], [0.78,-0.22,0.58]]

mse = Rede_Neural(entradas, res_esperado1, res_esperado2, pesos_h, pesos_o)
print(mse.getMSE())
print(mse.getDeltas())


