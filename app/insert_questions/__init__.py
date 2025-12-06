from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import current_user, logout_user
from .models import Questions
from ..extensions import db

InsertQuestions = Blueprint('InsertQuestions', __name__, template_folder='templates', static_folder='static', static_url_path='/InsertQuestions/static')

@InsertQuestions.before_request
def require_login():
    if not current_user.is_authenticated:
        return redirect(url_for('main.login'))
    
@InsertQuestions.route('/InsertQuestions', methods=['GET', 'POST'])
#cRud Leitura
def read_send():
    tasks = Questions.query.all()
    first_letter = ""
    if current_user.is_authenticated and current_user.username:
        first_letter = current_user.username[0].upper()
    return render_template('InsertQuestions.html', tasks=tasks, first_letter=first_letter) 

#Crud criação (CORRIGIDO PARA MÚLTIPLAS SUBMISSÕES)
@InsertQuestions.route('/create', methods=['POST'])
def create_question():
    # Obtém as listas de todos os títulos e questões enviadas (incluindo os campos dinâmicos)
    titles = request.form.getlist('title[]')
    questions = request.form.getlist('question[]')

    # Itera sobre os pares de título/questão para criar múltiplas entradas no BD
    for title, question in zip(titles, questions):
        # NOTA: O Flask só considera itens não vazios, mas uma verificação extra é boa.
        if title and question:
            new_task = Questions(title=title, question=question)
            db.session.add(new_task)
    
    db.session.commit()
    return redirect("/InsertQuestions")


#crUd Atualizar
@InsertQuestions.route('/update/<int:question_id>', methods=['GET' , 'POST'])
def update_question(question_id):
    task = Questions.query.get(question_id)
    if request.method == 'POST':
        task.title = request.form.get('title', task.title)
        task.question = request.form.get('question', task.question)
        db.session.commit()
        return redirect(url_for('InsertQuestions.read_send'))
    # Se for um método GET, o 'task_to_update' é passado para preencher o formulário.
    tasks = Questions.query.all()
    return render_template('InsertQuestions.html', tasks=tasks, task_to_update=task)

#cruD Delete
@InsertQuestions.route('/delete/<int:question_id>', methods=['POST'])
def delete_question(question_id):
    task = Questions.query.get(question_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect("/InsertQuestions")


@InsertQuestions.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == "POST":
        if 'action' in request.form and request.form['action'] == 'logout':
            logout_user()
            return redirect(url_for('main.login'))
    
    return render_template('perfil.html', user=current_user) 