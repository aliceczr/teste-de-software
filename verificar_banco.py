from app import app, db, User, Member

# Configurar o contexto da aplicação
with app.app_context():
    # Verificar usuários
    print("Usuários cadastrados:")
    usuarios = User.query.all()
    for usuario in usuarios:
        print(f"ID: {usuario.id}, Username: {usuario.username}, Email: {usuario.email}")

    # Verificar membros
    print("\nMembros cadastrados:")
    membros = Member.query.all()
    for membro in membros:
        print(f"ID: {membro.id}, Nome: {membro.nome}, Cargo: {membro.cargo}, Adicionado por: {membro.adicionado_por}")