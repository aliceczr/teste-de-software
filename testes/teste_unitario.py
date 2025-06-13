import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from validacoes import validar_email, validar_senha

def test_validar_email_valido():
    assert validar_email("teste@example.com") == True

def test_validar_email_invalido():
    assert validar_email("email_invalido") == False

def test_validar_senha_valida():
    assert validar_senha("senha12345") == True

def test_validar_senha_invalida():
    assert validar_senha("123") == False