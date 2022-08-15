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
    * CORS_ORIGIN_WHITELIST = http://localhost:8080

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
  * /cliente/create
  * /cliente/read
  * /cliente/update
  * /cliente/delete
  * /cliente/add_account
  * /cliente/remove_account
  * /heathz
  * /readiness
   

# Teste do Projeto
* Para executar os testes basta digitar o comando abaixo dentro da pasta do projeto (com as variáveis de ambiente configuradas)
    ```
    python -m pytest
    ```
---



