from flask import Flask, jsonify, request

app = Flask(__name__)

contas = [
    {
        'cliente': 'Tiago Silva',
        'saldo': 10.0
    },

    {
        'cliente': 'Sandro Pereira',
        'saldo': 10.0
    },

    {
        'cliente': 'Regina Silva',
        'saldo': 10.0
    },

    {
        'cliente': 'Enmily Silva',
        'saldo': 10.0
    },

    {
        'cliente': 'Maria Pereira',
        'saldo': 10.0
    },

    {
        'cliente': 'Edilson Silva',
        'saldo': 10.0
    }
]


# Criar Conta
@app.route('/contas', methods=['POST'])
def criar_conta():
    cliente = request.get_json()
    nova_conta = {
        'cliente': cliente,
        'saldo': 10.0
    }
    contas.append(nova_conta)
    return 'Conta criada', 200

# Creditar Valor
@app.route('/contas/<cliente>/creditar', methods=['PUT'])
def creditar_valor(cliente):
    valor = request.get_json()
    for conta in contas:
        if conta['cliente'] == cliente:
            conta['saldo'] += valor
            return 'Valor adicionado ao saldo', 200
    return 'Cliente não encontrado', 404

# Debitar Valor
@app.route('/contas/<cliente>/debitar', methods=['PUT'])
def debitar_valor(cliente):
    valor = request.get_json()
    for conta in contas:
        if conta['cliente'] == cliente:
            if conta['saldo'] < valor:
                return 'Saldo insuficiente', 400
            conta['saldo'] -= valor
            return 'Valor removido do saldo', 200
    return 'Cliente não encontrado', 404

# Ver Conta
@app.route('/contas/<cliente>', methods=['GET'])
def ver_conta(cliente):
    for conta in contas:
        if conta['cliente'] == cliente:
            return jsonify(conta), 200
    return 'Cliente não encontrado', 404

# Ver Saldo
@app.route('/contas/<cliente>/saldo', methods=['GET'])
def ver_saldo(cliente):
    for conta in contas:
        if conta['cliente'] == cliente:
            return jsonify(conta['saldo']), 200
    return 'Cliente não encontrado', 404

# Ver Saldo
@app.route('/contas/<cliente>/saldo', methods=['GET'])
def ver_saldo(cliente):
    for conta in contas:
        if conta['cliente'] == cliente:
            return jsonify(conta['saldo']), 200
    return 'Cliente não encontrado', 404

# Exibir Contas
@app.route('/contas', methods=['GET'])
def exibir_contas():
    if not contas:
        return 'Não há contas registradas', 404
    return jsonify(contas), 200

# Deletar Conta
@app.route('/contas/<cliente>', methods=['DELETE'])
def deletar_conta(cliente):
    for i, conta in contas:
        if conta['cliente'] == cliente:
            del contas[i]
            return 'Conta deletada', 200
    return 'Cliente não encontrado', 404


if __name__ == '__main__':
    app.run(port=500, host='localhost', debug=True)