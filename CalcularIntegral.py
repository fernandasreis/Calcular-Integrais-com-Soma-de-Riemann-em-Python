import sympy as sp

def calcularIntegral(funcao,a,b,n=10000):

    x = sp.symbols('x')

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
        valor = funcao.subs(x, i)

        if hasattr(valor, 'evalf'):       #se for uma expressão sympy
            altura = float(valor.evalf())
        else:                             #se já for número
            altura = float(valor)

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

    return float(S) if not hasattr(S, 'evalf') else float(S.evalf())


#só executa se rodar o arquivo diretamente
if __name__ == "__main__":
    x = sp.symbols('x')
    
    #configuração manual (com exemplo) 
    funcao = 2*x + 3  # ← mude aqui para testar
    a = 0             # ← mude aqui
    b = 5             # ← mude aqui
    
    resultado = calcularIntegral(funcao, a, b)
    print(f"Resultado: {round(resultado, 3)}")
