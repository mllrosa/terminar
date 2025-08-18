from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
# A chave secreta é necessária para usar a 'session'. Mantenha-a segura e complexa.
app.secret_key = 'uma_chave_secreta_muito_segura_e_longa_aqui'

# --- ROTA PARA A TELA 1: CARREGAMENTO ---
@app.route('/')
def tela_carregamento():
    return render_template('tela1_carregamento.html')

# --- ROTA PARA A TELA 2: LOGIN ---
@app.route('/login', methods=['GET', 'POST'])
def tela_login():
    if request.method == 'POST':
        # Pega os dados enviados pelo formulário
        nome = request.form.get('nome_operador')
        codigo = request.form.get('codigo_acesso')
        
        # Simulação de validação. No nosso protótipo, sempre aceitamos se os campos não estiverem vazios.
        if nome and codigo:
            # Armazena o nome do jogador na 'session' para usar em outras páginas.
            session['nome'] = nome.upper()
            return redirect(url_for('tela_briefing'))
        else:
            # Se algum campo estiver vazio, envia uma mensagem de erro.
            erro = "Erro: todos os campos devem ser preenchidos para evitar punição disciplinar."
            return render_template('tela2_login.html', erro=erro)

    # Se o método for GET, simplesmente renderiza a página de login.
    return render_template('tela2_login.html')

# --- ROTA PARA A TELA 3: BRIEFING (vamos criar essa depois, mas a rota já está aqui) ---
@app.route('/briefing')
def tela_briefing():
    # Pega o nome do jogador da 'session'
    nome = session.get('nome', 'Dr(a). [CLASSIFICADO]')
    return render_template('tela3_briefing.html', nome=nome)

if __name__ == '__main__':
    app.run(debug=True)