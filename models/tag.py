from db import db


class TagModel(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=True, nullable= False)

    # uma loja -> muitas tags
    loja_id = db.Column(db.Integer, db.ForeignKey('lojas.id'), unique=False,  nullable=False)
    loja = db.relationship("LojaModel",back_populates="tags")

    
    itens = db.relationship("ItemModel", secondary="itens_tags", back_populates="tags", passive_deletes=True)



