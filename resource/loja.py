from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask import jsonify, request
import uuid
from db import lojas
from schemas.loja import LojaSchema, LojaSchemaUptade

loja_blp = Blueprint("Loja", __name__, description="Operações relacionadas a loja")

@loja_blp.route('/loja')
class Loja(MethodView): 
    
    @loja_blp.response(200, LojaSchema(many=True))
    def get(self):
         return lojas.values()


    @loja_blp.arguments(LojaSchema)
    @loja_blp.response(201, LojaSchema)
    def post(self, loja_dado):

        loja_id = uuid.uuid4().hex

        loja_nova = {**loja_dado, "id":loja_id}

        lojas[loja_id] = loja_nova

        return jsonify(loja_nova), 201

@loja_blp.route('/loja/<string:id_loja>')
class LojaId(MethodView):

    @loja_blp.response(200, LojaSchema)
    def get(self, id_loja):
        if id_loja not in lojas:
            abort(404, message="Loja não encontrada.")

        try: 
            return jsonify(lojas[id_loja]), 200
        except KeyError: 
            abort(404, message="Loja não encontrada.")

    @loja_blp.arguments(LojaSchema)
    @loja_blp.response(200, LojaSchema)
    def put(self, dado_novo, id_loja):

        if id_loja not in lojas:
            abort(404, message="Loja não encontrada.")

        if "id" in dado_novo:
            if dado_novo["id"] != id_loja:
                abort(400, message="Operação não permitada, não é permitido aatualziar o id da loja")

        if "nome" not in dado_novo or "telefone" not in dado_novo or "cidade" not in dado_novo:
            abort(400, message = "Dados inválidos, nome, telefone  e cidade são obrigatórios")
        
        for loja in lojas.values(): 
            if loja["id"] == id_loja:
                
                loja.update(dado_novo)

                return jsonify({"loja atualizada": loja}), 200

        return jsonify({"erro": "Loja não encontrada"}), 404


    @loja_blp.arguments(LojaSchemaUptade)
    @loja_blp.response(200, LojaSchema)
    def patch(self, dados_loja, id_loja):

        if id_loja not in lojas:
            abort(404, message="Loja não encontrada.")

        if not dados_loja  or len(dados_loja) == 0: 
            abort(400, message="Dados inválido, nenhum campo enviado para atualização!")

        if "id" in dados_loja:
            if dados_loja["id"] != id_loja:
                abort(400, message="Operação não permitada, não é permitido aatualziar o id da loja")


        campos_permitido = {"nome", "cidade", "telefone"}

        campo_enviados = set(dados_loja.keys())

        campos = campo_enviados - campos_permitido

        if campos:
            abort(400, message="Campos inválidos")

        lojas[id_loja].update(dados_loja)

        return jsonify({"loja atualizada": lojas[id_loja]}), 200


    @loja_blp.response(200)
    def delete(self, id_loja):
       
        if id_loja not in lojas:
            abort(404, message="Loja não encontrada.")

        try:
            lojas.pop(id_loja)
            return jsonify({"message": "Loja removida com sucesso"}), 200
        except KeyError: 
            abort(404, message="Loja não encontrada.")