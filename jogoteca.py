from typing import List, Dict, Optional
from flask import Flask, render_template, request, redirect, session, flash, url_for

class Jogo:
    """Classe para representar um jogo."""
    def __init__(self, nome: str, categoria: str, console: str) -> None:
        """Inicializa um novo objeto Jogo.

        Args:
            nome (str): Nome do jogo.
            categoria (str): Categoria do jogo.
            console (str): Console onde o jogo é executado.
        """
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1: Jogo = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2: Jogo = Jogo('God of War', 'Hack n Slash', 'PS2')
jogo3: Jogo = Jogo('Mortal Kombat', 'Luta', 'PS2')
lista: List[Jogo] = [jogo1, jogo2, jogo3]

class Usuario:
    """Classe para representar um usuário."""
    def __init__(self, nome: str, nickname: str, senha: str) -> None:
        """Inicializa um novo objeto Usuario.

        Args:
            nome (str): Nome completo do usuário.
            nickname (str): Nome de usuário (apelido).
            senha (str): Senha do usuário.
        """
        self.nome = nome
        self.nickname = nickname
        self.senha = senha

usuario1: Usuario = Usuario("Bruno Divino", "BD", "alohomora")
usuario2: Usuario = Usuario("Camila Ferreira", "Mila", "paozinho")
usuario3: Usuario = Usuario("Guilherme Louro", "Cake", "python_eh_vida")

usuarios: Dict[str, Usuario] = { usuario1.nickname : usuario1,
                                  usuario2.nickname : usuario2,
                                  usuario3.nickname : usuario3 }

app: Flask = Flask(__name__)
app.secret_key = 'alura'

@app.route('/')
def index() -> str:
    """Rota principal que renderiza a lista de jogos."""
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo() -> str:
    """Rota para criar um novo jogo."""
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar() -> str:
    """Rota para criar um novo jogo."""
    nome: str = request.form['nome']
    categoria: str = request.form['categoria']
    console: str = request.form['console']
    jogo: Jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('index'))

@app.route('/login')
def login() -> str:
    """Rota para realizar login."""
    proxima: Optional[str] = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar() -> str:
    """Rota para autenticar o usuário."""
    if request.form['usuario'] in usuarios:
        usuario: Usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado com sucesso!')
            proxima_pagina: Optional[str] = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuário não logado.')
        return redirect(url_for('login'))

@app.route('/logout')
def logout() -> str:
    """Rota para realizar logout."""
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))

app.run(debug=True)
