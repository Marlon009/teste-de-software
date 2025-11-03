import pytest
import sys
import os

# Adiciona o diretório src ao path para importar o módulo
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from conta_corrente import ContaCorrente

class TestContaCorrente:
    
    def test_deposito_saque_valido(self):
        """Teste 1: Fluxo padrão - depósito seguido de saque válido"""
        conta = ContaCorrente(1000.0, -500.0)
        conta.depositar(200.0)
        assert conta.get_saldo() == 1200.0
        assert conta.sacar(300.0) == True
        assert conta.get_saldo() == 900.0
    
    def test_saque_utilizando_parte_limite(self):
        """Teste 2: Saque que utiliza parte do limite do cheque especial"""
        conta = ContaCorrente(200.0, -500.0)
        assert conta.sacar(400.0) == True
        assert conta.get_saldo() == -200.0
    
    def test_saque_atinge_exatamente_limite(self):
        """Teste 3: Saque que atinge exatamente o limite do cheque especial"""
        conta = ContaCorrente(200.0, -500.0)
        assert conta.sacar(700.0) == True
        assert conta.get_saldo() == -500.0
    
    def test_saque_ultrapassa_limite(self):
        """Teste 4: Saque que ultrapassa o limite (deve falhar e saldo inalterado)"""
        conta = ContaCorrente(200.0, -500.0)
        saldo_inicial = conta.get_saldo()
        assert conta.sacar(800.0) == False
        assert conta.get_saldo() == saldo_inicial
    
    def test_saque_valor_negativo(self):
        """Teste 5a: Tentativa de saque com valor negativo"""
        conta = ContaCorrente(1000.0, -500.0)
        with pytest.raises(ValueError, match="Valor de saque deve ser positivo"):
            conta.sacar(-100.0)
    
    def test_saque_valor_zero(self):
        """Teste 5b: Tentativa de saque com valor zero"""
        conta = ContaCorrente(1000.0, -500.0)
        with pytest.raises(ValueError, match="Valor de saque deve ser positivo"):
            conta.sacar(0.0)
    
    def test_deposito_valor_negativo(self):
        """Teste 5c: Tentativa de depósito com valor negativo"""
        conta = ContaCorrente(1000.0, -500.0)
        with pytest.raises(ValueError, match="Valor de depósito deve ser positivo"):
            conta.depositar(-100.0)
    
    def test_deposito_valor_zero(self):
        """Teste 5d: Tentativa de depósito com valor zero"""
        conta = ContaCorrente(1000.0, -500.0)
        with pytest.raises(ValueError, match="Valor de depósito deve ser positivo"):
            conta.depositar(0.0)
    
    def test_construtor_limite_positivo(self):
        """Teste 5e: Tentativa de criar conta com limite positivo"""
        with pytest.raises(ValueError, match="Limite do cheque especial deve ser zero ou negativo"):
            ContaCorrente(1000.0, 500.0)
    
    def test_construtor_limite_zero(self):
        """Teste adicional: Construtor com limite zero (deve funcionar)"""
        conta = ContaCorrente(1000.0, 0.0)
        assert conta.get_saldo() == 1000.0
        assert conta.sacar(1000.0) == True
        assert conta.get_saldo() == 0.0
    
    def test_construtor_limite_negativo(self):
        """Teste adicional: Construtor com limite negativo (deve funcionar)"""
        conta = ContaCorrente(1000.0, -1000.0)
        assert conta.get_saldo() == 1000.0