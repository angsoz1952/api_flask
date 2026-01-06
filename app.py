from flask import Flask, jsonify, request
from flask_smorest import abort
import os
import uuid

from db import lojas, items

app = Flask(__name__)

### Endpoint de lojas

# GET /lojas
@app.get('/lojas')
def get_lojas():
    return jsonify({"Lojas":  list(lojas.values())}), 200


# GET /loja/1
@app.get('/loja/<string:id_loja>')
def get_loja_by_id(id_loja):
    try: 
        return jsonify(lojas[id_loja]), 200
    except KeyError: 
        abort(404, message="Loja não encontrada.")
       

# GET /loja?nome=XPTO
@app.get('/loja')
def get_loja_name():
    nome = request.args['nome']

    for loja in lojas.values():
        if loja['nome'] == nome:
            return jsonify(loja), 200

    abort(404, message="Loja não encontrada")


#POST /loja
## Body > raw > Json
@app.post('/loja')
def criar_loja():
    loja_dado = request.get_json()
    loja_id = uuid.uuid4().hex

    loja_nova = {**loja_dado, "id":loja_id}

    lojas[loja_id] = loja_nova

    return jsonify(loja_nova), 201



#PUT /loja
@app.put('/loja/<string:id_loja>')
def atualizar_loja(id_loja):

    dado_novo = request.get_json()
    
    for loja in lojas.values(): 
        if loja["id"] == id_loja:
            
            loja.update(dado_novo)

            return jsonify({"loja atualizada": loja}), 200

    return jsonify({"erro": "Loja não encontrada"}), 404


#DELETE /loja/<id_loja>
@app.delete('/loja/<string:id_loja>')
def deletar_loja(id_loja):
    try:
        lojas.pop(id_loja)
        return jsonify({"message": "Loja removida com sucesso"}), 200
    except KeyError: 
        abort(404, message="Loja não encontrada.")
    


### Endpoint de itens

# GET /items
@app.get('/items')
def buscar_todos_itens():
    return jsonify({"Itens":  list(items.values())}), 200

#POST /items
@app.post('/items')
def cadastrar_novo_item():
    item_dado = request.get_json()
    item_id = uuid.uuid4().hex

    item_novo = {**item_dado, "id":item_id}

    items[item_id] = item_novo

    return jsonify(item_novo), 201


#GET /item/<string:id_item>
@app.get('/item/<id_item>')
def buscar_item_em_loja( id_item):
    try: 
        return jsonify(items[id_item])
    except KeyError: 
        abort(404, message="Item não encontrado")
    

#DELETE /item/<string:id_item>
@app.delete('/item/<string:id_item>')
def deletar_item( id_item):
    try: 
        items.pop(id_item)
        return jsonify({"message": "Item removido com sucesso"})
    except KeyError: 
        abort(404, message= "Item não encontrado")



#PUT /item/<string:id_item>
@app.put('/item/<string:id_item>')
def atualizar_item(id_item):

    dado = request.get_json()

    for item in items.values():
        if item['id'] == id_item:
           item.update(dado)
           return jsonify({"item atualizado": item}), 200

    return jsonify({"error": "Item não encontrado"}), 404


if __name__ == "__main__":
    app.run(debug=True)