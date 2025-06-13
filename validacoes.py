import re

def validar_email(email):
    
    if not isinstance(email, str):
        return False
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(padrao, email) is not None

def validar_senha(senha):
   
    return isinstance(senha, str) and len(senha) >= 8