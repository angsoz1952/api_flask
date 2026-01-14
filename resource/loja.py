from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask import jsonify, request
import uuid
lojas = {}
from schemas.loja import LojaSchema, LojaSchemaUptade
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models.loja import LojaModel


loja_blp = Blueprint("Loja", __name__, description="Operações relacionadas a loja")

@loja_blp.route('/loja')
class Loja(MethodView): 
    
    @loja_blp.response(200, LojaSchema(many=True))
    def get(self):
         return LojaModel.query.all()


    @loja_blp.arguments(LojaSchema)
    @loja_blp.response(201, LojaSchema)
    def post(self, loja_dado):

        nova_loja = LojaModel(**loja_dado)
        try: 
            db.session.add(nova_loja)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            abort(400, message= "Nome da loja e obrigatório")

        return nova_loja

@loja_blp.route('/loja/<string:id_loja>')
class LojaId(MethodView):

    @loja_blp.response(200, LojaSchema)
    def get(self, id_loja):
        loja = LojaModel.query.get(id_loja)

        if not loja: 
            abort( 404, message= "Loja não encontrada")

        return loja

    @loja_blp.arguments(LojaSchema)
    @loja_blp.response(200, LojaSchema)
    def put(self, dado_novo, id_loja):
        loja = LojaModel.query.get(id_loja)

        if not loja: 
            abort( 404, message= "Loja não encontrada")

        loja.nome = dado_novo["nome"]

        try: 
            db.session.add(loja)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            abort(400, message= "Nome da loja e obrigatório")

        return loja


    @loja_blp.arguments(LojaSchemaUptade)
    @loja_blp.response(200, LojaSchema)
    def patch(self, dados_loja, id_loja):

        loja = LojaModel.query.get(id_loja)

        if not loja: 
            abort( 404, message= "Loja não encontrada")


        if "nome" in dados_loja:
            loja.nome = dados_loja["nome"]

        try: 
            db.session.add(loja)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            abort(400, message= "Nome da loja e obrigatório")

        return loja

    @loja_blp.response(200)
    def delete(self, id_loja):
        loja = LojaModel.query.get(id_loja)

        if not loja: 
            abort( 404, message= "Loja não encontrada")

        db.session.delete(loja)
        db.session.commit()
        return {"message": "Loja removida com sucesso"}