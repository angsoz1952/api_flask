from flask import Flask, jsonify, request

app = Flask(__name__)

lojas = [ 
    {
        "id": 1,
        "nome": "Loja A",
        "cidade": "Marica",
        "imagem"
        "items": [
            {
                "id": "loja-a-1",
                "nome": "Cadeira",
                "preco": 19.99
            },
            {
                "id": "loja-a-2",
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
                "id": "loja-b-1",
                "nome": "Mesa",
                "preco": 59.99
            }, 
            {
                "id": "loja-b-2",
                "nome": "Garfo",
                "preco": 9.99
            }, 
            {
                "id": "loja-b-3",
                "nome": "notebook",
                "preco": 1999.99
            }
        ]
    }
]


### Endpoint de lojas

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

### Endpoint de itens

# GET /loja/<id_loja>/items
@app.get('/loja/<int:id_loja>/items')
def buscar_itens_loja(id_loja):

    for loja in lojas:
        if loja['id'] == id_loja:
            return jsonify({"items": loja['items']}), 200
    
    return jsonify({"erro": "Loja não encontrada"}), 404

#GET /loja/<int:id_loja>/item/<id_item>
@app.get('/loja/<int:id_loja>/item/<id_item>')
def buscar_item_em_loja(id_loja, id_item):

    for loja in lojas:
        if loja['id'] == id_loja:

            for item in loja['items']:
                if item['id'] == id_item:

                    return jsonify({"item": item}), 200
                
            return  jsonify({"erro": "Item não encontrado!"})

    return jsonify({"error": "Loja não encontrada!"}), 404

#POST /loja/<int:id_loja>/item
@app.post('/loja/<int:id_loja>/item')
def cadastrar_produto_loja(id_loja):
    for loja in lojas: 
        if loja['id'] == id_loja:

            dado = request.get_json()

            if dado['preco_produto'] < 0: 
                return jsonify({"error": "O preço do produto não pode ser negativo!"}), 400

            if len(dado['nome_produto'] )<= 0: 
                return jsonify({"error": "O nome do produto não pode ser vazio!"}), 400

            novo_item = { 
                "id": dado['id_produto'],
                "nome": dado['nome_produto'],
                "preco": dado['preco_produto'],
            }

            loja['items'].append(novo_item)
            return jsonify({"Item adicionado": novo_item}), 201

    return jsonify({"error": "Loja não encontrada!"}), 404

#DELETE /loja/<int:id_loja>/item/<id_item>
@app.delete('/loja/<int:id_loja>/item/<id_item>')
def deletar_item(id_loja, id_item):
    for loja in lojas:
        if loja['id'] == id_loja:

            for item in loja['items']:
                if item['id'] == id_item:
                    loja['items'].remove(item)
                    return jsonify({"message": "Item removido com sucesso!"})

            return  jsonify({"erro": "Item não encontrado!"})

    return jsonify({"error": "Loja não encontrada!"}), 404

#PUT /loja/<int:id_loja>/item/<id_item>
@app.put('/loja/<int:id_loja>/item/<id_item>')
def atualizar_item(id_loja, id_item):

    dado = request.get_json()

    for loja in lojas:
        if loja['id'] == id_loja:

            for item in loja['items']:
                if item['id'] == id_item: 

                    item['nome'] = dado['nome_prod']
                    item['preco'] = dado['preco_prod']

                    return {
                        "message": "Item atualizado com sucesso!", 
                        "item": item
                    }, 200

    return jsonify({"error": "Loja não encontrada"}), 404

@app.get('/loja/pesquisa/<key>/<value>')
@app.post('/loja/pesquisa')
def pesquisar(key, value):

    for loja in lojas: 
       if value in loja[key]:
            return jsonify({"loja":  loja}), 200

    return jsonify({"Erro": "Loja não encontrar"}), 404


@app.get('/header_request')
def verificar_cliente():
    agente = request.headers.get('User-agent')
    host = request.headers.get('Host')
    content_type= request.headers.get("Content-type")
    token_autenticacao =  request.headers.get("Autorization")
    cokies = request.headers.get('Cookies')


    return jsonify({
        "User-agent": agente,
        "Host": host,
        "Content-type": content_type,
        "Autorization": token_autenticacao
    }), 200


@app.get('/request/<param>')
def verificar_request(param):

    return jsonify(
        {
            "path": request.path,
            "url_completa": request.url,
            "base_url": request.base_url,
            "endpoint": request.endpoint,
            "metodo": request.method,
            "query_parametro": dict(request.args),
            "path_completo": request.full_path,
            "parametro": param

        }
    )



if __name__ == "__main__":
    app.run(debug=True)