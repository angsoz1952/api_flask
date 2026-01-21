from flask_smorest import Blueprint, abort
from flask.views import MethodView
from models.loja import LojaModel
from models.tag import TagModel
from models.item import ItemModel

from db import db

from sqlalchemy.exc import SQLAlchemyError

from schemas.tag import TagSchema, TagAndItemSchema

tag_blp = Blueprint("Tag", __name__, description = 'Operações relacionadas a tags')



@tag_blp.route('/loja/<int:id_loja>/tag')
class TagInLoja(MethodView):

    @tag_blp.response(200, TagSchema(many=True))
    def get(self, id_loja):
        loja = LojaModel.query.get_or_404(id_loja)
        return loja.tags.all()

    @tag_blp.arguments(TagSchema)
    @tag_blp.response(201, TagSchema)
    def post(self, tag_dado, id_loja):
        # Verifica se a loja existe
        LojaModel.query.get_or_404(id_loja)
        
        tag = TagModel(**tag_dado, loja_id=id_loja)
        try: 
            db.session.add(tag)
            db.session.commit()
        except SQLAlchemyError: 
            db.session.rollback()
            abort(500, message="Erro ao adicionar tag na loja")

        return tag


@tag_blp.route('/tag/<int:id_tag>')
class Tag(MethodView):

    @tag_blp.response(200, TagSchema)
    def get(self, id_tag):
        return TagModel.query.get_or_404(id_tag)
    

    def delete(self, id_tag):
        tag = TagModel.query.get_or_404(id_tag)
        
        db.session.delete(tag)
        db.session.commit()
        return {"message": "Tag removida com sucesso!"}
    

@tag_blp.route('/item/<int:item_id>/tag/<int:tag_id>')
class LinkTagToItem(MethodView):

    @tag_blp.response(201, TagSchema)
    def post(self, item_id, tag_id):
        item = ItemModel.query.get_or_404(item_id)
        tag = TagModel.query.get_or_404(tag_id)

        # Verifica se item e tag pertencem à mesma loja
        if item.loja_id != tag.loja_id:
            abort(400, message="Item e Tag devem pertencer à mesma loja.")

        item.tags.append(tag)

        try: 
            db.session.add(item)
            db.session.commit()

        except SQLAlchemyError: 
            db.session.rollback()
            abort(500, message="Erro ao adicionar tag ao item")

        return tag 


    @tag_blp.response(200, TagAndItemSchema)
    def delete(self, item_id, tag_id):
        item = ItemModel.query.get_or_404(item_id)
        tag = TagModel.query.get_or_404(tag_id)

        item.tags.remove(tag)

        try: 
            db.session.add(item)
            db.session.commit()

        except SQLAlchemyError: 
            db.session.rollback()
            abort(500, message="Erro ao deletar tag do item")

        return { 
            "message": "Item removido da tag com sucesso",
            "item": item,
            "tag": tag
        }