from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask import jsonify, request
from db import items
import uuid

item_blp= Blueprint("Item", __name__, description="Operações de item")


@item_blp.route('/item')
class Item(MethodView):

    def get(self): 
        return jsonify({"Itens":  list(items.values())}), 200

    def post(self, item_dado): 
         
        item_id = uuid.uuid4().hex

        item_novo = {**item_dado, "id":item_id}

        items[item_id] = item_novo

        return jsonify(item_novo), 201
    
@item_blp.route('/item/<string:id_item>')
class ItemId(MethodView):

    def get(self, id_item):
        try: 
            return jsonify(items[id_item])
        except KeyError: 
            abort(404, message="Item não encontrado")

    def put(self, dado, id_item):
        
        for item in items.values():
            if item['id'] == id_item:
                item.update(dado)
                return jsonify({"item atualizado": item}), 200

        return jsonify({"error": "Item não encontrado"}), 404

    def delete(self, id_item):
        try: 
            items.pop(id_item)
            return jsonify({"message": "Item removido com sucesso"})
        except KeyError: 
            abort(404, message= "Item não encontrado")

    def patch(self, id_item):
        if id_item not in items:
            abort(404, message="Item não encontrado")

        dados_item = request.get_json(silent=True)

        if not isinstance(dados_item, dict) or len(dados_item) == 0:
            abort(400, message="Dados inválidos, nenhum campo enviado para atualização!")

        if "id" in dados_item and dados_item["id"] != id_item:
            abort(400, message="Operação não permitida, não é permitido atualizar o id do item")

        dados_item.pop("id", None)
        items[id_item].update(dados_item)

        return jsonify({"item atualizado": items[id_item]}), 200

    