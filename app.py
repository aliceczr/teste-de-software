from flask import Flask, render_template, request, redirect, url_for, flash, session
import os 
from datetime import datetime
from models import db, User, Member

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'instance', 'database.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return redirect(url_for('login'))

# Página de cadastro
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'GET':
        return render_template('cadastro.html')  
    try:
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if User.query.filter_by(email=email).first():
            flash("Email já cadastrado!", "error")
            return redirect(url_for('login'))
        
        novo_usuario = User(username=username, email=email, password=password)
        db.session.add(novo_usuario)
        db.session.commit()
        flash("Usuário cadastrado com sucesso!", "success")
        return redirect(url_for('login'))
    except Exception as e:
        print(f"Erro: {e}")
        return "Erro interno no servidor", 500

# Página de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = User.query.filter_by(email=email).first()
        if user and user.password == password:
            session['user_id'] = user.id
            flash("Login bem-sucedido!", 'success')
            return redirect(url_for('management'))
        else:
            flash("Credenciais inválidas!", 'error')
    
    return render_template('login.html')

# Página de perfil
@app.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    return render_template('profile.html', user=user)

# Logout
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("Logout realizado com sucesso!", 'success')
    return redirect(url_for('login'))

@app.route('/management')
def management():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    membros = Member.query.all()
    return render_template('management.html', membros=membros)

# Adicionar membro
@app.route('/adicionar_membro', methods=['GET', 'POST'])
def adicionar_membro():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        nome = request.form['nome']
        cargo = request.form['cargo']
        adicionado_por = User.query.get(session['user_id']).username
        data_adicao = datetime.now().strftime('%d-%m-%Y %H:%M')
        membro = Member(nome=nome, cargo=cargo, adicionado_por=adicionado_por, data_adicao=data_adicao)
        db.session.add(membro)
        db.session.commit()
        flash('Membro adicionado com sucesso!', 'success')
        return redirect(url_for('management'))
    return render_template('adicionar_membro.html')

# Editar membro
@app.route('/editar_membro/<int:id>', methods=['GET', 'POST'])
def editar_membro(id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    membro = Member.query.get_or_404(id)
    if request.method == 'POST':
        membro.nome = request.form['nome']
        membro.cargo = request.form['cargo']
        db.session.commit()
        flash('Membro atualizado com sucesso!', 'success')
        return redirect(url_for('management'))
    return render_template('editar_membro.html', membro=membro)

# Remover membro
@app.route('/remover_membro/<int:id>', methods=['GET','POST'])
def remover_membro(id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    membro = Member.query.get_or_404(id)
    db.session.delete(membro)
    db.session.commit()
    flash('Membro removido com sucesso!', 'success')
    return redirect(url_for('management'))


if __name__ == '__main__':
    app.run(debug=True)

