from flask import Flask, jsonify, request

obj = Flask(__name__)

# Vetor para armazenar as contas correntes
contas = []

# Rota para criar uma conta
@obj.route('/contas', methods=['POST'])
def criar_conta():
    dados = request.json
    cliente = dados.get('cliente')

    if not cliente:
        return jsonify({"erro": "O identificador do cliente é obrigatório."}), 400

    if any(conta['cliente'] == cliente for conta in contas):
        return jsonify({"erro": "Já existe uma conta para este cliente."}), 400

    conta = {"cliente": cliente, "saldo": 10.0}
    contas.append(conta)
    return jsonify({"mensagem": "Conta criada com sucesso.", "conta": conta}), 201

# Rota para creditar valor na conta
@obj.route('/contas/<cliente>/creditar', methods=['PUT'])
def creditar(cliente):
    dados = request.json
    valor = dados.get('valor')

    if not isinstance(valor, (int, float)) or valor <= 0:
        return jsonify({"erro": "Valor inválido para crédito."}), 400

    conta = next((c for c in contas if c['cliente'] == cliente), None)
    if not conta:
        return jsonify({"erro": "Conta não encontrada."}), 404

    conta['saldo'] += valor
    return jsonify({"mensagem": "Valor creditado com sucesso.", "conta": conta}), 200

# Rota para debitar valor na conta
@obj.route('/contas/<cliente>/debitar', methods=['PUT'])
def debitar(cliente):
    dados = request.json
    valor = dados.get('valor')

    if not isinstance(valor, (int, float)) or valor <= 0:
        return jsonify({"erro": "Valor inválido para débito."}), 400

    conta = next((c for c in contas if c['cliente'] == cliente), None)
    if not conta:
        return jsonify({"erro": "Conta não encontrada."}), 404

    if conta['saldo'] < valor:
        return jsonify({"erro": "Saldo insuficiente."}), 400

    conta['saldo'] -= valor
    return jsonify({"mensagem": "Valor debitado com sucesso.", "conta": conta}), 200

# Rota para ver detalhes de uma conta
@obj.route('/contas/<cliente>', methods=['GET'])
def ver_conta(cliente):
    conta = next((c for c in contas if c['cliente'] == cliente), None)
    if not conta:
        return jsonify({"erro": "Conta não encontrada."}), 404

    return jsonify(conta), 200

# Rota para ver o saldo de uma conta
@obj.route('/contas/<cliente>/saldo', methods=['GET'])
def ver_saldo(cliente):
    conta = next((c for c in contas if c['cliente'] == cliente), None)
    if not conta:
        return jsonify({"erro": "Conta não encontrada."}), 404

    return jsonify({"saldo": conta['saldo']}), 200

# Rota para exibir todas as contas
@obj.route('/contas', methods=['GET'])
def exibir_contas():
    return jsonify(contas), 200

# Rota para deletar uma conta
@obj.route('/contas/<cliente>', methods=['DELETE'])
def deletar_conta(cliente):
    global contas
    conta = next((c for c in contas if c['cliente'] == cliente), None)
    if not conta:
        return jsonify({"erro": "Conta não encontrada."}), 404

    contas = [c for c in contas if c['cliente'] != cliente]
    return jsonify({"mensagem": "Conta deletada com sucesso."}), 200

if __name__ == '__main__':
    obj.run(debug=True)
