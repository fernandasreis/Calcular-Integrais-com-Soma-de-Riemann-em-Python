# Calcular Integrais com Soma de Riemann em Python
Este projeto implementa uma calculadora de integrais definidas usando o método dos retângulos (Soma de Riemann pelo ponto médio), desenvolvido como trabalho complementar para a disciplina de Cálculo Fundamental II na UFC.

Apesar de não ser um código com uma otimização máxima, optei por fazer da forma mais didática possível para a vizualização e compreensão de cada etapa da Soma de Riemann separadamente.

### Funcionalidades

-  Cálculo de integrais definidas 
-  Suporte a diversas funções elementares:
    - Polinômios (x², 3x + 2, etc.)
    - Funções trigonométricas (sin(x), cos(x), tan(x))
    - Funções exponenciais (exp(x), 2^x)
    - Funções logarítmicas (log(x), ln(x))
    - Raízes n-ésimas (sqrt(x), x**(1/3))

### Pré-requisitos para usar

- Python 3.x instalado
- Biblioteca SymPy (`pip install sympy`)

### Como usar
1. **Edite o código diretamente**: Abra o arquivo `CalcularIntegral.py` e modifique os valores nas linhas indicadas:
```python
# Mudar os parâmetros aqui!
funcao =   # ← Edite a função (digite de acordo com o formato da biblioteca SymPy e usando a variável 'x')
a =        # ← Edite o início do intervalo  
b =        # ← Edite o fim do intervalo
```
2. Execute o programa
3. Veja o resultado: o programa calculará e exibirá o valor da área sob o gráfico da função (integral definida)

### Método Utilizado (Soma de Riemann)
1. Divide o intervalo [a, b] em n = 10000 subintervalos
2. Calcula a altura de cada retângulo no ponto médio de cada subintervalo
3. Calcula a área de cada retângulo
4. Soma as áreas de todos os retângulos

### Testes Realizados
O programa foi validado manualmente com os seguintes casos:

• ∫(2x + 3)dx de 0 a 5 → Resultado: 40 ✓

• ∫(x²)dx de 0 a 3 → Resultado: 9 ✓

• ∫(sin(x))dx de 0 a π → Resultado: 2 ✓

• ∫(x)dx de 3 a 1 → Resultado: -4 ✓ (intervalo invertido)

• ∫(exp(x))dx de 0 a 1 → Resultado: e - 1 ≈ 1.718 ✓

## Autora
Fernanda Silveira Reis - Estudante de Engenharia de Computação na UFC
