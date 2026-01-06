# API Flask — Lojas e Itens

API simples em Flask para cadastrar e gerenciar **lojas** e **itens** via HTTP.

> **Observação importante:** os dados ficam em memória (dicionários Python em `db.py`). Ao reiniciar o servidor, tudo é perdido.

## Requisitos

- Python 3.x

## Instalação

No diretório do projeto:

```bash
pip install -r requirements.txt
```

## Como executar

```bash
python app.py
```

Por padrão o Flask sobe em:

- `http://127.0.0.1:5000`

## Estrutura de dados

A API aceita JSON no corpo das requisições e salva o conteúdo “como vier”, adicionando um campo `id` gerado automaticamente.

- Loja: recebe um JSON (ex.: `{ "nome": "Minha Loja" }`) e adiciona `id`.
- Item: recebe um JSON (ex.: `{ "nome": "Camiseta", "preco": 19.9 }`) e adiciona `id`.

## Endpoints

### Lojas

- `GET /lojas` — lista todas as lojas
- `GET /loja/<id_loja>` — busca loja por id
- `GET /loja?nome=XPTO` — busca loja por nome (querystring obrigatória `nome`)
- `POST /loja` — cria loja
- `PUT /loja/<id_loja>` — atualiza loja por id
- `DELETE /loja/<id_loja>` — remove loja por id

### Itens

- `GET /items` — lista todos os itens
- `POST /items` — cria item
- `GET /item/<id_item>` — busca item por id
- `PUT /item/<id_item>` — atualiza item por id
- `DELETE /item/<id_item>` — remove item por id

## Exemplos (curl)

### Criar uma loja

```bash
curl -X POST http://127.0.0.1:5000/loja \
  -H "Content-Type: application/json" \
  -d "{\"nome\":\"Loja Central\"}"
```

### Listar lojas

```bash
curl http://127.0.0.1:5000/lojas
```

### Buscar loja por id

```bash
curl http://127.0.0.1:5000/loja/<id_loja>
```

### Buscar loja por nome

```bash
curl "http://127.0.0.1:5000/loja?nome=Loja%20Central"
```

### Atualizar loja

```bash
curl -X PUT http://127.0.0.1:5000/loja/<id_loja> \
  -H "Content-Type: application/json" \
  -d "{\"nome\":\"Loja Central (Atualizada)\"}"
```

### Deletar loja

```bash
curl -X DELETE http://127.0.0.1:5000/loja/<id_loja>
```

---

### Criar um item

```bash
curl -X POST http://127.0.0.1:5000/items \
  -H "Content-Type: application/json" \
  -d "{\"nome\":\"Camiseta\",\"preco\":19.90}"
```

### Listar itens

```bash
curl http://127.0.0.1:5000/items
```

### Buscar item por id

```bash
curl http://127.0.0.1:5000/item/<id_item>
```

### Atualizar item

```bash
curl -X PUT http://127.0.0.1:5000/item/<id_item> \
  -H "Content-Type: application/json" \
  -d "{\"preco\":29.90}"
```

### Deletar item

```bash
curl -X DELETE http://127.0.0.1:5000/item/<id_item>
```

## Notas

- Respostas de erro (por exemplo, quando não encontra loja/item) retornam `404` com uma mensagem.
- Como não há validação de schema, você pode adicionar quaisquer campos no JSON; eles serão armazenados e retornados.
