# 🏦 Processador de Transações Bancárias

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Pytest](https://img.shields.io/badge/pytest-7.2.1-green)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)
![Tests](https://img.shields.io/badge/tests-11%20passed-success)

Sistema completo de processamento de transações bancárias com testes automatizados e 100% de cobertura.

## 📋 Sobre o Projeto

Implementação profissional de uma conta corrente digital com todas as regras de negócio, desenvolvida como trabalho acadêmico para a disciplina de Testes no Desenvolvimento de Software.

**Características principais:**
- ✅ Operações de saque e depósito
- ✅ Controle de limite do cheque especial
- ✅ Validações rigorosas de negócio
- ✅ Testes automatizados abrangentes
- ✅ 100% de cobertura de código

## 🏗️ Arquitetura

**Tecnologias:**
- **Linguagem**: Python 3.11+
- **Testes**: Pytest + Pytest-cov
- **Cobertura**: 100% linhas e ramos

## 🧪 Estratégia de Testes

Desenvolvido com **Test-First Approach**, garantindo qualidade desde o início:

### Categorias de Teste
1. **Fluxo Principal** - Operações normais
2. **Casos de Limite** - Boundary value analysis
3. **Testes de Exceção** - Validações de entrada
4. **Estado Persistido** - Consistência de dados

### Métricas de Qualidade
- **11 testes** cobrindo todos os requisitos
- **100% cobertura** de linhas e branches
- **Tempo de execução**: 0.01s
- **Relatórios HTML** automatizados

## 🚀 Como Executar

```bash
# Clonar e acessar o projeto
git clone <url-do-repositorio>
cd bancario

# Configurar ambiente
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Instalar dependências
pip install -r requirements.txt

# Executar testes
pytest

# Gerar relatório de cobertura
pytest --cov=src --cov-report=html --cov-branch

# Abrir relatório
xdg-open htmlcov/index.html  # Linux
