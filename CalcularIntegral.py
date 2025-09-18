import sympy as sp

def calcularIntegral(funcao,a,b,n=10000):

    x = sp.symbols('x')

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
        valor = funcao.subs(x, i)

        if hasattr(valor, 'evalf'):  # Se for uma expressão sympy
            altura = float(valor.evalf())
        else:         # Se já for número
            altura = float(valor)

        H.append(altura)

    A = []         #valores das áreas de cada retângulo 
    for altura in H:
        area = altura * T
        A.append(area)

    S = 0       #soma das áreas
    for area in A:
        S += area

    return float(S) if not hasattr(S, 'evalf') else float(S.evalf())


# Só executa se rodar o arquivo diretamente
if __name__ == "__main__":
    x = sp.symbols('x')
    
    # Configuração manual (com exemplo) 
    funcao = 2*x + 3  # ← Mude aqui para testar
    a = 0             # ← Mude aqui
    b = 5             # ← Mude aqui
    
    resultado = calcularIntegral(funcao, a, b)
    print(f"Resultado: {round(resultado, 3)}")