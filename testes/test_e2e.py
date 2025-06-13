from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()


def test_cadastro():
    print("Iniciando teste de cadastro...")
    driver.get("http://127.0.0.1:5000/cadastro")  

    try:
        driver.find_element(By.NAME, "username").send_keys("selenium_user")
        driver.find_element(By.NAME, "email").send_keys("selenium_user@example.com")
        driver.find_element(By.NAME, "password").send_keys("password123")
        driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)  

        time.sleep(5)
        assert "Login" in driver.title  # Verifica se foi redirecionado para a página de login
        print("Teste de cadastro concluído com sucesso!")
    except Exception as e:
        print(f"Erro no teste de cadastro: {e}")
        raise

# Teste E2E: Login de usuário
def test_login():
    print("Iniciando teste de login...")
    driver.get("http://127.0.0.1:5000/login")  
    try:
        driver.find_element(By.NAME, "email").send_keys("selenium_user@example.com")
        driver.find_element(By.NAME, "password").send_keys("password123")
        driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)  

        time.sleep(5)
        assert "Gerenciamento de Membros" in driver.title  
        print("Teste de login concluído com sucesso!")
    except Exception as e:
        print(f"Erro no teste de login: {e}")
        raise

# Teste E2E: Adicionar membro
def test_adicionar_membro():
    print("Iniciando teste de adicionar membro...")
    driver.get("http://127.0.0.1:5000/adicionar_membro")  

    try:
        driver.find_element(By.NAME, "nome").send_keys("Novo Membro Selenium")
        driver.find_element(By.NAME, "cargo").send_keys("Desenvolvedor")
        driver.find_element(By.NAME, "cargo").send_keys(Keys.RETURN)  

        time.sleep(5)
        assert "Gerenciamento de Membros" in driver.title
        print("Teste de adicionar membro concluído com sucesso!")
    except Exception as e:
        print(f"Erro no teste de adicionar membro: {e}")
        raise

# Teste E2E: Editar membro
def test_editar_membro():
    print("Iniciando teste de edição de membro...")
    driver.get("http://127.0.0.1:5000/editar_membro/6")

    try:
        driver.find_element(By.NAME, "nome").clear()
        driver.find_element(By.NAME, "nome").send_keys("Membro Atualizado Selenium")
        driver.find_element(By.NAME, "cargo").clear()
        driver.find_element(By.NAME, "cargo").send_keys("Analista de Dados")
        driver.find_element(By.NAME, "cargo").send_keys(Keys.RETURN)  

        time.sleep(5)
        assert "Gerenciamento de Membros" in driver.title
        print("Teste de edição de membro concluído com sucesso!")
    except Exception as e:
        print(f"Erro no teste de edição de membro: {e}")
        raise

# Teste E2E: Remover membro
def test_remover_membro():
    print("Iniciando teste de remoção de membro...")
    driver.get("http://127.0.0.1:5000/remover_membro/6") 

    try:
        time.sleep(5)  
        assert "Gerenciamento de Membros" in driver.title
        print("Teste de remoção de membro concluído com sucesso!")
    except Exception as e:
        print(f"Erro no teste de remoção de membro: {e}")
        raise

# Teste E2E: Logout
def test_logout():
    print("Iniciando teste de logout...")
    driver.get("http://127.0.0.1:5000/logout")  

    try:
        time.sleep(5) 
        assert "Login" in driver.title  
        print("Teste de logout concluído com sucesso!")
    except Exception as e:
        print(f"Erro no teste de logout: {e}")
        raise

# Executar os testes
if __name__ == "__main__":
    try:
        test_cadastro()
        test_login()
        test_adicionar_membro()
        test_editar_membro()
        test_remover_membro()
        test_logout()
        print("Todos os testes passaram!")
    except AssertionError as e:
        print("Um dos testes falhou:", e)
    finally:
        driver.quit()  