import sympy as sp

x = sp.symbols('x')

#mudar os parâmetros aqui!
funcao = 
a = 
b = 

n = 10000   #número de retângulos usável

T = (b - a) / n #base dos retângulos (iguais para todo o intervalo) 

X = []  #valores dos pontos que dividem as partições + fim e início do intervalo
for i in range(1,n):
    divisao = a + i*T
    X.append(divisao)   
X.insert(0, a)
X.insert(n,b)

C = []     #valores usados para achar alturas de cada retângulo (ponto médio)
for i in range(1,n+1):
    amostra = (X[i-1] + X[i]) / 2
    C.append(amostra)

H = []       #valores das alturas de cada retângulo
for i in C:
    altura = float(funcao.subs(x,i))
    H.append(altura)

A = []         #valores das áreas de cada retângulo 
for altura in H:
    area = altura * T
    A.append(area)

S = 0       #soma das áreas
for area in A:
    S += area

print(f"\n\nÁrea total: {round(S, 3)}\n\n")