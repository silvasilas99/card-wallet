# Card Wallet

    Visão Geral do Projeto:
    
      API minimalista voltada a praticar uso de recursos Flask
    
## Instruções de Utilização: 
      Clone o repositório do projeto
        git clone https://github.com/silvasilas99/card-wallet

      Vá ao diretório onde o projeto se encontra
          cd ./card-wallet

      Instale as dependencias necessárias para a aplicação
          pip install flask flask-restful flask-sqlalchemy

      Entre no interpretador Python 
          python3
      E execute os comandos abaixo
          >>> from main import db
          >>> db.create_all()
          >>> exit()

      Defina o ambiente como de desenvolvimento
          set FLASK_ENV=development

      Inicie o servidor da aplicação
          flask run
          ou python3 main.py
      
      Realize as requisições desejadas utilizando o arquivo "Cards Wallet.postman_collection", contido na raiz do repositório
          E obrigado por testar!!!
