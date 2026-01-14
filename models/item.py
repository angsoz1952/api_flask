from db import db


class ItemModel(db.Model):
    __tablename__ = "itens"

    id = db.Column(db.Integer, primary_key= True)
    nome = db.Column(db.String, unique=True, nullable=False)
    preco = db.Column(db.Float(precision=2), unique=False, nullable=False)
    loja_id = db.Column(db.Integer, db.ForeignKey('lojas.id'), unique=False,  nullable=False)

    loja = db.relationship("LojaModel", back_populates="itens")