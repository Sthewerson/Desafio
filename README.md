README.md

# Digital Wallet API

## Descrição

Este projeto é uma API de carteira digital construída com Django e Django REST Framework. Ele permite a criação de usuários, gerenciamento de carteiras, transações entre carteiras e histórico de Transações. 

## Requisitos

- Docker
- Docker Compose

## Configuração do Projeto

1. Clonar o Repositório

Clone o repositório para o seu ambiente local:

```bash
git clone https://github.com/Sthewerson/Desafio.git
cd desafio
 ```
2. Construir e Iniciar os Contêineres
Construa e inicie os contêineres Docker:
  ```bash
docker-compose up -d --build    
```

3. Executar as Migrações
Execute as migrações para criar as tabelas no banco de dados:
 ```bash
docker-compose exec django python manage.py makemigrations
docker-compose exec django python manage.py migrate     
```
4. Popular o Banco de Dados (Opcional)
Popule o banco de dados com dados iniciais:
 ```bash
 docker-compose exec django python manage.py populate_db     
```
5. Criar um Superusuário (Opcional)
Crie um superusuário para acessar o painel de administração do Django:
 ```bash
docker-compose exec django python manage.py createsuperuser      
```
6. Como Rodar o Programa
Iniciar o Servidor
Certifique-se de que os contêineres Docker estão em execução:
 ```bash
docker-compose up -d        
```
Acessar a Aplicação
A aplicação estará disponível em http://localhost:8000/.

Acessar o Painel de Administração do Django
Se você criou um superusuário, você pode acessar o painel de administração do Django em http://localhost:8000/admin/ usando as credenciais do superusuário.
Endpoints
1. Obter Token JWT
- Método: POST
- URL: http://localhost:8000/api/token/
- Body: JSON
```bash
{
    "username": "user1",
    "password": "password"
}
```
2. Atualizar Token JWT
- Método: POST
- URL: http://localhost:8000/api/token/refresh/
- Body: JSON
```bash
{
  "refresh": "your_refresh_token"
}
```

3. Criar Usuário

- Método: POST
- URL: http://localhost:8000/api/users/
- Body: JSON
 ```bash
 {
    "username": "user3",
    "password": "password",
    "email": "user3@example.com"
}       
 ```

4. Obter Detalhes do Usuário

- Método: GET
- URL: http://localhost:8000/api/users/<id>/
- Headers:
  
  Authorization: Bearer <your_access_token>

5. Obter Detalhes da Carteira

- Método: GET
- URL: : http://localhost:8000/api/wallets/<id>/
- Headers:
  
  Authorization: Bearer <your_access_token>

6. Adicionar Saldo à Carteira

- Método: POST
- URL: http://localhost:8000/api/wallets/<id>/add_balance/
- Headers:
  
  Authorization: Bearer <your_access_token>
  
  Content-Type: application/json
  
Body: JSON

 ```bash
 {
    "amount": 100.00
}
```
7. Criar Transação

- Método: POST
- URL: http://localhost:8000/api/transactions/
-Headers:

 Authorization: Bearer <your_access_token>
 
 Content-Type: application/json
 
Body: JSON
 ```bash
 {
    "receiver": "user2",
    "amount": 50.00,
    "description": "Payment"
}
```
8. Listar Transações

- Método: GET
- URL: http://localhost:8000/api/transactions/list/
-Headers:

Authorization: Bearer <your_access_token>

9. Histórico de Transações

-Método: GET
-URL: http://localhost:8000/api/transactions/history/?start_date=<YYYY-MM-DD>&end_date=<YYYY-MM-DD>

Headers:

Authorization: Bearer <your_access_token>
