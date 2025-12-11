from flask import Flask, jsonify, request

app = Flask(__name__)

lojas = [ 
    {
        "id": 1,
        "nome": "Loja A",
        "items": [
            {
                "nome": "Cadeira",
                "preco": 19.99
            },
            {
                "nome": "Faca",
                "preco": 29.99
            }
        ]
    }, 
    {
        "id": 2,
        "nome": "Loja B",
        "items": [
            {
                "nome": "Mesa",
                "preco": 59.99
            }, 
            {
                "nome": "Garfo",
                "preco": 9.99
            }, 
            {
                "nome": "notebook",
                "preco": 1999.99
            }
        ]
    }
]

# GET /lojas
@app.get('/lojas')
def get_lojas():
    return jsonify({"Lojas": lojas}), 200


# GET /loja/1
@app.get('/loja/<int:id>')
def get_loja_by_id(id):

    for loja in lojas: 
        if loja["id"] == id:
            return jsonify(loja), 200

    return jsonify({"erro": "Loja não encontrada"}), 404


# GET /loja?nome=XPTO
@app.get('/loja')
def get_loja_name():
    nome = request.args['nome']

    for loja in lojas:
        if loja['nome'] == nome:
            return jsonify(loja), 200

    return jsonify({"erro": "Loja não encontrada"}), 404


#POST /loja
## Body > raw > Json
@app.post('/loja')
def criar_loja():

    dado = request.get_json()

    if not dado: 
        return jsonify({"erro": "Dado não enviado"}), 400

    if "nome" not in dado: 
        return jsonify({"erro": "O campo 'nome' é obrigatório"}), 400

    if "id" not in dado: 
        return jsonify({"erro": "O campo 'id' é obrigatório"}), 400

    
    nova_loja = {
        "id": dado['id'],
        "nome": dado['nome'],
        "items": []
    }

    lojas.append(nova_loja)

    return jsonify(nova_loja), 201


#PUT /loja
@app.put('/loja/<int:id_loja>')
def atualizar_loja(id_loja):

    dado_novo = request.get_json()

    if 'nome' not in dado_novo: 
        return jsonify({"erro": "O campo 'nome' é obrigatório"}), 400
    
    for loja in lojas: 
        if loja["id"] == id_loja:
            
            loja['nome'] = dado_novo['nome']

            return jsonify({"loja atualizada": loja}), 200

    return jsonify({"erro": "Loja não encontrada"}), 404


#DELETE /loja/<id_loja>
@app.delete('/loja/<int:id_loja>')
def deletar_loja(id_loja):

    loja_remove = None

    for loja in lojas:
        if loja['id'] ==  id_loja:
            loja_remove = loja
    
    if loja_remove is None:
        return jsonify({"erro": "Loja não encontrada"}), 404

    lojas.remove(loja_remove)

    return jsonify({"message": "Loja removida com sucesso"}), 200


if __name__ == "__main__":
    app.run(debug=True)