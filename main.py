from flask import Flask, jsonify, request

app = Flask(__name__)

contas = [
    {"cliente": "Tiago Silva", "saldo": 10.0},
    {"cliente": "Sandro Pereira", "saldo": 10.0},
    {"cliente": "Regina Silva", "saldo": 10.0},
    {"cliente": "Enmily Silva", "saldo": 10.0},
    {"cliente": "Maria Pereira", "saldo": 10.0},
    {"cliente": "Edilson Silva", "saldo": 10.0},
]

# Criar Conta
@app.route("/contas", methods=["POST"])
def criar_conta():
    dados = request.get_json()
    cliente = dados.get("cliente")

    if not cliente:
        return jsonify({"erro": "O identificador do cliente é obrigatório."}), 400

    if any(conta["cliente"] == cliente for conta in contas):
        return jsonify({"erro": "Já existe uma conta para este cliente."}), 400

    nova_conta = {"cliente": cliente, "saldo": 10.0}
    contas.append(nova_conta)
    return jsonify({"mensagem": "Conta criada com sucesso.", "conta": nova_conta}), 201


# Creditar Valor
@app.route("/contas/<cliente>/creditar", methods=["PUT"])
def creditar_valor(cliente):
    dados = request.get_json()
    valor = dados.get("valor")

    if not isinstance(valor, (int, float)) or valor <= 0:
        return jsonify({"erro": "Valor inválido para crédito."}), 400

    for conta in contas:
        if conta["cliente"] == cliente:
            conta["saldo"] += valor
            return jsonify({"mensagem": "Valor creditado com sucesso.", "conta": conta}), 200

    return jsonify({"erro": "Cliente não encontrado."}), 404


# Debitar Valor
@app.route("/contas/<cliente>/debitar", methods=["PUT"])
def debitar_valor(cliente):
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


# Ver Conta
@app.route("/contas/<cliente>", methods=["GET"])
def ver_conta(cliente):
    for conta in contas:
        if conta["cliente"] == cliente:
            return jsonify(conta), 200

    return jsonify({"erro": "Cliente não encontrado."}), 404


# Ver Saldo
@app.route("/contas/<cliente>/saldo", methods=["GET"])
def ver_saldo(cliente):
    for conta in contas:
        if conta["cliente"] == cliente:
            return jsonify({"saldo": conta["saldo"]}), 200

    return jsonify({"erro": "Cliente não encontrado."}), 404


# Exibir Contas
@app.route("/contas", methods=["GET"])
def exibir_contas():
    if not contas:
        return jsonify({"mensagem": "Não há contas registradas."}), 404
    return jsonify(contas), 200


# Deletar Conta
@app.route("/contas/<cliente>", methods=["DELETE"])
def deletar_conta(cliente):
    global contas
    for i, conta in enumerate(contas):
        if conta["cliente"] == cliente:
            del contas[i]
            return jsonify({"mensagem": "Conta deletada com sucesso."}), 200

    return jsonify({"erro": "Cliente não encontrado."}), 404


if __name__ == "__main__":
    app.run(port=5000, host="localhost", debug=True)