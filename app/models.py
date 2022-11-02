from app.ext.database import db


class Videos(db.Model):
    __tablename__ = 'videos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255), nullable=False)