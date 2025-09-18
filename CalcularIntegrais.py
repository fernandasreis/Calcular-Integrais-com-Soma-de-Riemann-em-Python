import sympy as sp

x = sp.symbols('x')

#colocar os parâmetros aqui!
funcao = 
a = 
b = 

#número de retângulos usável
n = 10000   

#base dos retângulos (iguais para todo o intervalo)
T = (b - a) / n  

 #valores dos pontos que dividem as partições + fim e início do intervalo
X = [] 
for i in range(1,n):
    divisao = a + i*T
    X.append(divisao)   
X.insert(0, a)
X.insert(n,b)

#valores usados para achar alturas de cada retângulo (ponto médio)
C = []     
for i in range(1,n+1):
    amostra = (X[i-1] + X[i]) / 2
    C.append(amostra)

#valores das alturas de cada retângulo
H = []       
for i in C:
    altura = float(funcao.subs(x,i))
    H.append(altura)

 #valores das áreas de cada retângulo 
A = []        
for altura in H:
    area = altura * T
    A.append(area)

#soma das áreas
S = 0       
for area in A:
    S += area

print(f"\n\nÁrea total: {round(S, 3)}\n\n")
