# Desafio programação - BHub

# Ambiente de desenvolvimento
* Python 3.7
* MySQL Server 8.0.17 
  * O mesmo deverá estar instalado, no ar e com um usuário com permissões de DDL e DML.
* PyCharm 2021.1.2

# Instalação
* Clonar o repositório 
  * https://github.com/grmagalhaes/desafio_bhub.git
* Criar um venv e habilitá-lo
* Instalar as dependências (django, mysql, etc). Rodar dentro da pasta do repo.
    * pip -r requirements.txt
* Configurar as informações de conexão com a base de dados do arquivo settings.py como variáveis de ambiente:  
    * DB_ENGINE = classe do banco de dados (ex: django.db.backends.mysql)
    * DB_NAME = nome do banco de dados (ex: desafio_bhub)
    * DB_USER = usuário do banco de dados com permissão de criação de objetos (ex: bhub)
    * DB_PASS = senha do usuário do banco  'USER': 'desafio',
    * DB_HOST = hostname do servidor do banco de dados (ex: localhost)
    * DB_PORT = porta do banco de dados (ex: 3306)

* Configurar o CORS_ORIGIN (variável de ambiente):
    * CORS_ORIGIN_WHITELIST = http://localhost:8000

#### *** TODAS AS VARIÁVEIS ACIMA DEVEM ESTAR SETADAS NO SHELL *** 
  
* Para criar o banco (ex. em MySQL) e dar acesso ao usuário os seguintes comandos devem ser executados:
    *  mysql -u root -p < CAMINHO_DO_PROJETO/script_db/create_db.sql
    ```
    * caso o mysql seja usado de outro host o script deverá ser alterado para o hostname do servidor de BD.
    * o script já dá permissão para a criação do banco de teste (test_desafio no caso)
    ```
    
* Executar os comandos dentro da pasta do porjeto para atualizar e migrar o esquema a partir do Django para o MySQL (ou outro DB)
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

# Execução do Projeto
* Para executar o projeto basta digitar o comando abaixo dentro da pasta interna "project"
    ```
    python manage.py runserver
    ```
* O projeto estará disponível em http://localhost:8000/
* O modo DEBUG ficará ligado em função do propósito do desafio

# Funcionamento do Projeto
* O Desafio está detalhado no PDF em /bhub (Desafio - BHub.pdf)  
* Endpints criados
  * v1/cliente/create
  * v1/cliente/read
  * v1/cliente/update
  * v1/cliente/delete
  * v1/client/list
  * v1/cliente/add_account
  * v1/cliente/remove_account
  * /heathz
  * /readiness
   

# Teste do Projeto
* Para executar os testes basta digitar o comando abaixo dentro da pasta do projeto (com as variáveis de ambiente configuradas)
    ```
    python -m pytest
    ```
  
# Collection do POSTMAN
* Está na pasta postman na raiz do projeto (collection e environment)
* 
# Open API 
* Está na pasta openapi na raiz do projeto (openapi.yml)
---

# Melhorias

* Inclusão de oauth2 com classe de authenticação em cada BO
* Testes do DockerFile e docker-compose
* Deploy em cloud (AWS)
* Enriquecer mais os testes unitários
* Colocar mais validadores de campos
* O endpoint /client/list poderia ter paginação e mostrar as contas
* Mmelhorar o Logger



