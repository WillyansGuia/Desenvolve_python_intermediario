from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from .models.models import User
from .alquimias import create_user, create_post, get_timeline

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    posts = None
    if current_user.is_authenticated:
        posts = get_timeline()
    return render_template('index.html', user=current_user if current_user.is_authenticated else None, posts=posts)

@bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        profile_pic = request.form.get('profile_pic')
        bio = request.form.get('bio')

        if not username or not email or not password:
            flash('Preencha username, email e password')
            return redirect(url_for('main.cadastro'))

        if User.query.filter((User.username==username)|(User.email==email)).first():
            flash('Usuário ou email já existe')
            return redirect(url_for('main.cadastro'))

        user = create_user(username, email, password, profile_pic, bio)
        login_user(user)
        flash('Conta criada e logado com sucesso')
        return redirect(url_for('main.index'))

    return render_template('cadastro.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash('Logado com sucesso')
            return redirect(url_for('main.index'))
        flash('Usuário ou senha inválidos')
        return redirect(url_for('main.login'))
    return render_template('login.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Desconectado')
    return redirect(url_for('main.index'))

@bp.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    if request.method == 'POST':
        body = request.form.get('body')
        if not body:
            flash('Post vazio não permitido')
            return redirect(url_for('main.post'))
        create_post(body, current_user)
        flash('Post criado')
        return redirect(url_for('main.index'))
    return render_template('post.html')
