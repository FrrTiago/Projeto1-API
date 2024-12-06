from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

contas = [
    {"cliente": "Tiago Silva", "saldo": 10.0},
    {"cliente": "Sandro Pereira", "saldo": 10.0},
    {"cliente": "Regina Silva", "saldo": 10.0},
    {"cliente": "Enmily Silva", "saldo": 10.0},
    {"cliente": "Maria Pereira", "saldo": 10.0},
    {"cliente": "Edilson Silva", "saldo": 10.0},
]

@app.route("/contas", methods=["POST"])
def criar_conta():
    """
    Criar uma nova conta
    ---
    parameters:
      - in: body
        name: body
        description: Identificador do cliente para criar uma nova conta
        required: true
        schema:
          type: object
          properties:
            cliente:
              type: string
              example: Novo Cliente
    responses:
      201:
        description: Conta criada com sucesso
        schema:
          type: object
          properties:
            mensagem:
              type: string
            conta:
              type: object
      400:
        description: Erro na solicitação
    """
    dados = request.get_json()
    cliente = dados.get("cliente")

    if not cliente:
        return jsonify({"erro": "O identificador do cliente é obrigatório."}), 400

    if any(conta["cliente"] == cliente for conta in contas):
        return jsonify({"erro": "Já existe uma conta para este cliente."}), 400

    nova_conta = {"cliente": cliente, "saldo": 10.0}
    contas.append(nova_conta)
    return jsonify({"mensagem": "Conta criada com sucesso.", "conta": nova_conta}), 201


@app.route("/contas/<cliente>/creditar", methods=["PUT"])
def creditar_valor(cliente):
    """
    Creditar um valor na conta
    ---
    parameters:
      - in: path
        name: cliente
        type: string
        required: true
        description: Identificador do cliente
      - in: body
        name: body
        description: Valor a ser creditado na conta
        required: true
        schema:
          type: object
          properties:
            valor:
              type: float
              example: 50.0
    responses:
      200:
        description: Valor creditado com sucesso
      400:
        description: Erro de validação ou valor inválido
      404:
        description: Cliente não encontrado
    """
    dados = request.get_json()
    valor = dados.get("valor")

    if not isinstance(valor, (int, float)) or valor <= 0:
        return jsonify({"erro": "Valor inválido para crédito."}), 400

    for conta in contas:
        if conta["cliente"] == cliente:
            conta["saldo"] += valor
            return jsonify({"mensagem": "Valor creditado com sucesso.", "conta": conta}), 200

    return jsonify({"erro": "Cliente não encontrado."}), 404


@app.route("/contas/<cliente>/debitar", methods=["PUT"])
def debitar_valor(cliente):
    """
    Debitar um valor da conta
    ---
    parameters:
      - in: path
        name: cliente
        type: string
        required: true
        description: Identificador do cliente
      - in: body
        name: body
        description: Valor a ser debitado da conta
        required: true
        schema:
          type: object
          properties:
            valor:
              type: float
              example: 20.0
    responses:
      200:
        description: Valor debitado com sucesso
      400:
        description: Saldo insuficiente ou valor inválido
      404:
        description: Cliente não encontrado
    """
    dados = request.get_json()
    valor = dados.get("valor")

    if not isinstance(valor, (int, float)) or valor <= 0:
        return jsonify({"erro": "Valor inválido para débito."}), 400

    for conta in contas:
        if conta["cliente"] == cliente:
            if conta["saldo"] < valor:
                return jsonify({"erro": "Saldo insuficiente."}), 400
            conta["saldo"] -= valor
            return jsonify({"mensagem": "Valor debitado com sucesso.", "conta": conta}), 200

    return jsonify({"erro": "Cliente não encontrado."}), 404


@app.route("/contas/<cliente>", methods=["GET"])
def ver_conta(cliente):
    """
    Consultar detalhes da conta de um cliente
    ---
    parameters:
      - in: path
        name: cliente
        type: string
        required: true
        description: Identificador do cliente
    responses:
      200:
        description: Retorna os detalhes da conta
      404:
        description: Cliente não encontrado
    """
    for conta in contas:
        if conta["cliente"] == cliente:
            return jsonify(conta), 200

    return jsonify({"erro": "Cliente não encontrado."}), 404


@app.route("/contas", methods=["GET"])
def exibir_contas():
    """
    Listar todas as contas cadastradas
    ---
    responses:
      200:
        description: Retorna a lista de contas cadastradas
      404:
        description: Não há contas registradas
    """
    if not contas:
        return jsonify({"mensagem": "Não há contas registradas."}), 404
    return jsonify(contas), 200


if __name__ == "__main__":
    app.run(port=5000, host="localhost", debug=True)