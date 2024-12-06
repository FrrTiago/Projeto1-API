# API de Gerenciamento de Contas Correntes

Esta é uma API REST simples desenvolvida em Python utilizando Flask, que permite o gerenciamento de contas correntes com operações como criação, consulta, crédito, débito e exclusão.

## Funcionalidades

- **Criar Conta**: Cria uma nova conta para um cliente com saldo inicial de R$10,00.
- **Creditar Valor**: Adiciona um valor ao saldo de uma conta.
- **Debitar Valor**: Subtrai um valor do saldo, se houver saldo suficiente.
- **Consultar Conta**: Retorna os detalhes de uma conta específica.
- **Consultar Saldo**: Retorna apenas o saldo de uma conta específica.
- **Listar Contas**: Exibe todas as contas cadastradas.
- **Excluir Conta**: Remove uma conta do sistema.

## Tecnologias Utilizadas

- Python 3.8+
- Flask
- Flasgger (para documentação Swagger)

---

## Requisitos

- Python 3.8 ou superior
- `pip` instalado para gerenciar pacotes Python

---

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-repositorio/api-contas.git
   cd api-contas
   ```

2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/MacOS
   venv\Scripts\activate      # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

   O arquivo `requirements.txt` deve conter:
   ```
   Flask
   Flasgger
   ```

---

## Execução

1. Execute a aplicação:
   ```bash
   python app.py
   ```

2. Acesse a API no endereço:
   ```
   http://localhost:5000
   ```

3. Acesse a documentação interativa (Swagger):
   ```
   http://localhost:5000/apidocs
   ```

---

## Endpoints da API

### 1. **Criar Conta**
- **URL**: `/contas`
- **Método**: `POST`
- **Corpo da Requisição**:
  ```json
  {
    "cliente": "Nome do Cliente"
  }
  ```
- **Resposta de Sucesso**:
  ```json
  {
    "mensagem": "Conta criada com sucesso.",
    "conta": {
      "cliente": "Nome do Cliente",
      "saldo": 10.0
    }
  }
  ```

---

### 2. **Creditar Valor**
- **URL**: `/contas/<cliente>/creditar`
- **Método**: `PUT`
- **Corpo da Requisição**:
  ```json
  {
    "valor": 50.0
  }
  ```
- **Resposta de Sucesso**:
  ```json
  {
    "mensagem": "Valor creditado com sucesso.",
    "conta": {
      "cliente": "Nome do Cliente",
      "saldo": 60.0
    }
  }
  ```

---

### 3. **Debitar Valor**
- **URL**: `/contas/<cliente>/debitar`
- **Método**: `PUT`
- **Corpo da Requisição**:
  ```json
  {
    "valor": 20.0
  }
  ```
- **Resposta de Sucesso**:
  ```json
  {
    "mensagem": "Valor debitado com sucesso.",
    "conta": {
      "cliente": "Nome do Cliente",
      "saldo": 40.0
    }
  }
  ```

---

### 4. **Consultar Conta**
- **URL**: `/contas/<cliente>`
- **Método**: `GET`
- **Resposta de Sucesso**:
  ```json
  {
    "cliente": "Nome do Cliente",
    "saldo": 10.0
  }
  ```

---

### 5. **Consultar Saldo**
- **URL**: `/contas/<cliente>/saldo`
- **Método**: `GET`
- **Resposta de Sucesso**:
  ```json
  {
    "saldo": 10.0
  }
  ```

---

### 6. **Listar Contas**
- **URL**: `/contas`
- **Método**: `GET`
- **Resposta de Sucesso**:
  ```json
  [
    {"cliente": "Cliente 1", "saldo": 10.0},
    {"cliente": "Cliente 2", "saldo": 15.0}
  ]
  ```

---

### 7. **Excluir Conta**
- **URL**: `/contas/<cliente>`
- **Método**: `DELETE`
- **Resposta de Sucesso**:
  ```json
  {
    "mensagem": "Conta deletada com sucesso."
  }
  ```

---

## Testando a API

Você pode testar a API utilizando ferramentas como:
- [Postman](https://www.postman.com/)
- [Insomnia](https://insomnia.rest/)
- A interface interativa do **Swagger** (`http://localhost:5000/apidocs`)

---

Sinta-se à vontade para usar o projeto e modificá-lo conforme necessário.

---

Se precisar de mais informações ou ajuda, é só entrar em contato! 😊