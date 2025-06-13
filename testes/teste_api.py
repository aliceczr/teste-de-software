import requests

BASE_URL = "http://127.0.0.1:5000"

def login():
    """Função auxiliar para autenticar o usuário."""
    payload = {"email": "testuser@example.com", "password": "password123"}
    response = requests.post(f"{BASE_URL}/login", data=payload)
    assert response.status_code == 200 or response.status_code == 302
    return response.cookies  

def test_cadastro_endpoint():
    """Teste para o endpoint de cadastro."""
    payload = {"username": "testuser", "email": "testuser@example.com", "password": "password123"}
    response = requests.post(f"{BASE_URL}/cadastro", data=payload)
    assert response.status_code == 200 or response.status_code == 302 
def test_management_endpoint():
    """Teste para o endpoint de management."""
    cookies = login()
    response = requests.get(f"{BASE_URL}/management", cookies=cookies)
    assert response.status_code == 200
    assert "Beatriz" in response.text  

def test_adicionar_membro_endpoint():
    """Teste para o endpoint de adicionar membro."""
    cookies = login()  
    payload = {"nome": "Novo Membro", "cargo": "Desenvolvedor"}
    response = requests.post(f"{BASE_URL}/adicionar_membro", data=payload, cookies=cookies)
    assert response.status_code == 200 or response.status_code == 302
    assert "<form" in response.text

def test_editar_membro_endpoint():
    """Teste para o endpoint de editar membro."""
    cookies = login() 
    membro_id = 1 
    payload = {"nome": "Membro Editado", "cargo": "Gerente"}
    response = requests.post(f"{BASE_URL}/editar_membro/{membro_id}", data=payload, cookies=cookies)
    assert response.status_code == 200 or response.status_code == 302

def test_remover_membro_endpoint():
    """Teste para o endpoint de remover membro."""
    cookies = login()  
    membro_id = 1 
    response = requests.post(f"{BASE_URL}/remover_membro/{membro_id}", cookies=cookies)
    assert response.status_code == 200 or response.status_code == 302