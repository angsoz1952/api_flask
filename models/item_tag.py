from db import db


class ItemTagModel(db.Model):
    __tablename__ = "itens_tags"

    #PK da tabela
    id = db.Column(db.Integer, primary_key=True)

    #FK de item 
    item_id = db.Column(db.Integer, db.ForeignKey("itens.id", ondelete="CASCADE"), nullable= False)

    #FK de tag
    tag_id = db.Column(db.Integer, db.ForeignKey("tags.id", ondelete="CASCADE"), nullable= False)

