from app.ext.database import db


class Videos(db.Model):
    __tablename__ = 'videos'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255), nullable=False, unique=True)

    def serializer(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'descricao': self.descricao,
            'url': self.url
        }