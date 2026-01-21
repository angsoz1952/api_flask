from db import db

class LojaModel(db.Model):
    __tablename__ = "lojas"

    id = db.Column(db.Integer, primary_key= True)
    nome = db.Column(db.String(80), unique=True, nullable=False)

    itens = db.relationship("ItemModel", back_populates="loja", lazy="dynamic", cascade="all, delete-orphan")

    tags = db.relationship("TagModel", back_populates="loja", lazy="dynamic", cascade="all, delete-orphan")