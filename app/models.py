from app.ext.database import db


class Video(db.Model):
    __tablename__ = 'videos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey("categorias.id"), default=1)

    def __repr__(self) -> str:
        return f'<Video {self.titulo}>'



class Categoria(db.Model):
    __tablename__ = 'categorias'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(50), nullable=False)
    cor = db.Column(db.String(50), nullable=False)
    videos = db.relationship("Video", backref="categoria")