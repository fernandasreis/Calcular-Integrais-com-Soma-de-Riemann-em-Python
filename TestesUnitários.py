import unittest
from CalcularIntegral import calcularIntegral
import sympy as sp
import math

class TestIntegral(unittest.TestCase):
    
    
    def teste1_polinomio(self):
        """Testa ∫(x² + 2x + 1) dx de 0 a 2 = 8.666"""
        x = sp.symbols('x')
        resultado = calcularIntegral(x**2 + 2*x + 1, 0, 2)
        self.assertAlmostEqual(resultado, 8.666, places=1)
        print(f"Polinômio passou: ∫(x² + 2x + 1) dx de 0 a 2 = {resultado:.4f}")
    
    def teste2_intervalo_invertido(self):
        """Testa ∫(x) dx de 3 a 1 = -4"""
        x = sp.symbols('x')
        resultado = calcularIntegral(x, 3, 1)
        self.assertAlmostEqual(resultado, -4.0, places=2)
        print(f"Intervalo invertido passou: ∫(x) dx de 3 a 1 = {resultado:.3f}")
    
    def teste3_função_linear(self):
        """Testa ∫(2x + 3) dx de 0 a 5 = 40"""
        x = sp.symbols('x')
        resultado = calcularIntegral(2*x + 3, 0, 5)
        self.assertAlmostEqual(resultado, 40.0, places=1)
        print(f"Função linear passou: ∫(2x + 3) dx de 0 a 5 = {resultado:.3f}")
    
    def teste4_funcao_trigonometrica(self):
        """Testa ∫(sin(x)) dx de 0 a π = 2"""
        x = sp.symbols('x')
        resultado = calcularIntegral(sp.sin(x), 0, sp.pi)
        self.assertAlmostEqual(resultado, 2.0, places=2)
        print(f"Função trigonométrica (seno) passou: ∫(sin(x)) dx de 0 a π = {resultado:.4f}")
    
    def teste5_funcao_exponencial(self):
        """Testa ∫(e^x) dx de 0 a 1 = e - 1 ≈ 1.718"""
        x = sp.symbols('x')
        resultado = calcularIntegral(sp.exp(x), 0, 1)
        esperado = math.e - 1
        self.assertAlmostEqual(resultado, esperado, places=2)
        print(f"Função exponencial passou: ∫(e^x) dx de 0 a 1 = {resultado:.4f}")
    
    def teste6_funcao_logaritmica(self):
        """Testa ∫(ln(x)) dx de 1 a e = 1"""
        x = sp.symbols('x')
        resultado = calcularIntegral(sp.log(x), 1, math.e)
        self.assertAlmostEqual(resultado, 1.0, places=2)
        print(f"Função logarítmica passou: ∫(ln(x)) dx de 1 a e = {resultado:.4f}")
    
    def teste7_funcao_raiz_quadrada(self):
        """Testa ∫(√x) dx de 0 a 4 = 16/3 ≈ 5.333"""
        x = sp.symbols('x')
        resultado = calcularIntegral(sp.sqrt(x), 0, 4)
        self.assertAlmostEqual(resultado, 5.333, places=2)
        print(f"Função raiz quadrada passou: ∫(√x) dx de 0 a 4 = {resultado:.4f}")
    
    def teste8_soma_funcoes(self):
        """Testa ∫(sin(x) + x²) dx de 0 a π/2 ≈ 2.291"""
        x = sp.symbols('x')
        resultado = calcularIntegral(sp.sin(x) + x**2, 0, sp.pi/2)
        self.assertAlmostEqual(resultado, 2.291, places=2)  # ← Valor CORRIGIDO
        print(f"Soma de funções passou: ∫(sin(x) + x²) dx de 0 a π/2 = {resultado:.4f}")
    
    def teste9_quociente(self):
        """Testa ∫(1/(1 + x)) dx de 0 a 1 = ln(2) ≈ 0.693"""
        x = sp.symbols('x')
        resultado = calcularIntegral(1/(1 + x), 0, 1)
        self.assertAlmostEqual(resultado, 0.693, places=2)
        print(f"Quociente passou: ∫(1/(1 + x)) dx de 0 a 1 = {resultado:.4f}")
    
    def teste10_composicao_funcoes(self):
        """Testa ∫(sin(x²)) dx de 0 a 1 ≈ 0.310"""
        x = sp.symbols('x')
        resultado = calcularIntegral(sp.sin(x**2), 0, 1)
        self.assertAlmostEqual(resultado, 0.310, places=2)
        print(f"Composição de funções passou: ∫(sin(x²)) dx de 0 a 1 = {resultado:.4f}")

if __name__ == '__main__':
    unittest.main()