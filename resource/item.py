from flask_smorest import Blueprint, abort
from flask.views import MethodView

from db import db
from models.item import ItemModel
from schemas.item import ItemSchema, ItemSchemaUpdate

from sqlalchemy.exc import SQLAlchemyError

item_blp = Blueprint("Item", __name__, description="Operações de item")


@item_blp.route('/item')
class Item(MethodView):

    @item_blp.response(200, ItemSchema(many=True))
    def get(self): 
        return ItemModel.query.all()

    @item_blp.arguments(ItemSchema)
    @item_blp.response(201, ItemSchema)
    def post(self, item_dado): 
        item = ItemModel(**item_dado)
        
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            abort(500, message="Erro ao criar item")

        return item
    

@item_blp.route('/item/<int:id_item>')
class ItemId(MethodView):

    @item_blp.response(200, ItemSchema)
    def get(self, id_item):
        return ItemModel.query.get_or_404(id_item)

    @item_blp.arguments(ItemSchemaUpdate)
    @item_blp.response(200, ItemSchema)
    def put(self, dado, id_item):
        item = ItemModel.query.get_or_404(id_item)
        
        item.nome = dado.get("nome", item.nome)
        item.preco = dado.get("preco", item.preco)
        
        try:
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            abort(500, message="Erro ao atualizar item")

        return item

    def delete(self, id_item):
        item = ItemModel.query.get_or_404(id_item)
        
        db.session.delete(item)
        db.session.commit()
        
        return {"message": "Item removido com sucesso"}

    @item_blp.arguments(ItemSchemaUpdate)
    @item_blp.response(200, ItemSchema)
    def patch(self, dados_item, id_item):
        item = ItemModel.query.get_or_404(id_item)

        if dados_item.get("nome"):
            item.nome = dados_item["nome"]
        if dados_item.get("preco"):
            item.preco = dados_item["preco"]

        try:
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            abort(500, message="Erro ao atualizar item")

        return item

    