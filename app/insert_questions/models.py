from ..extensions import db

# Modelo do formulário de perguntas
class Questions(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)#nullable, Tem que ser preenchido para prosseguir
    question = db.Column(db.String(255), nullable=False)
