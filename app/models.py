from app.ext.database import db


class Videos(db.Model):
    __tablename__ = 'videos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(50))
    descricao = db.Column(db.String(255))
    url = db.Column(db.String(255))

    def serializer(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'descricao': self.descricao,
            'url': self.url
        }