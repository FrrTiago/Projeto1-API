# API de Gerenciamento de Contas Correntes

Esta é uma API REST desenvolvida em Python utilizando o framework Flask para gerenciamento de contas correntes. A API permite criar, visualizar, atualizar e excluir contas, além de realizar operações de crédito e débito.

## Funcionalidades
- **Criar Conta (POST /contas):** Cria uma nova conta com um saldo inicial de R$10,00.
- **Creditar Valor (PUT /contas/<cliente>/creditar):** Adiciona um valor ao saldo da conta do cliente.
- **Debitar Valor (PUT /contas/<cliente>/debitar):** Subtrai um valor do saldo da conta do cliente, se houver saldo suficiente.
- **Ver Conta (GET /contas/<cliente>):** Retorna os detalhes da conta do cliente específico.
- **Ver Saldo (GET /contas/<cliente>/saldo):** Retorna apenas o saldo da conta do cliente.
- **Exibir Contas (GET /contas):** Lista todas as contas cadastradas no sistema.
- **Deletar Conta (DELETE /contas/<cliente>):** Remove uma conta específica com base no identificador do cliente.

## Pré-requisitos
- Python 3.8 ou superior
- Pip (gerenciador de pacotes do Python)

## Instalação
1. Clone este repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd <DIRETORIO_DO_PROJETO>
   ```
3. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   ```
4. Ative o ambiente virtual:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/MacOS:
     ```bash
     source venv/bin/activate
     ```
5. Instale as dependências:
   ```bash
   pip install flask
   ```

## Execução
1. Execute o arquivo principal da aplicação:
   ```bash
   python <NOME_DO_ARQUIVO>.py
   ```
2. A API estará disponível em `http://127.0.0.1:5000`.

## Endpoints
### Criar Conta
**POST** `/contas`
- Corpo da requisição (JSON):
  ```json
  {
    "cliente": "nome_do_cliente"
  }
  ```
- Resposta (201):
  ```json
  {
    "cliente": "nome_do_cliente",
    "saldo": 10.0
  }
  ```

### Creditar Valor
**PUT** `/contas/<cliente>/creditar`
- Corpo da requisição (JSON):
  ```json
  {
    "valor": 100.0
  }
  ```
- Resposta (200):
  ```json
  {
    "cliente": "nome_do_cliente",
    "saldo": 110.0
  }
  ```

### Debitar Valor
**PUT** `/contas/<cliente>/debitar`
- Corpo da requisição (JSON):
  ```json
  {
    "valor": 50.0
  }
  ```
- Resposta (200):
  ```json
  {
    "cliente": "nome_do_cliente",
    "saldo": 60.0
  }
  ```

### Ver Conta
**GET** `/contas/<cliente>`
- Resposta (200):
  ```json
  {
    "cliente": "nome_do_cliente",
    "saldo": 10.0
  }
  ```

### Ver Saldo
**GET** `/contas/<cliente>/saldo`
- Resposta (200):
  ```json
  {
    "saldo": 10.0
  }
  ```

### Exibir Contas
**GET** `/contas`
- Resposta (200):
  ```json
  [
    {
      "cliente": "nome_do_cliente",
      "saldo": 10.0
    }
  ]
  ```

### Deletar Conta
**DELETE** `/contas/<cliente>`
- Resposta (200):
  ```json
  {
    "mensagem": "Conta removida com sucesso."
  }
  ```

## Testes
Utilize ferramentas como [Postman](https://www.postman.com/) ou [cURL](https://curl.se/) para realizar testes nos endpoints da API.

Exemplo de requisição usando cURL:
```bash
curl -X POST http://127.0.0.1:5000/contas -H "Content-Type: application/json" -d '{"cliente": "cliente1"}'
