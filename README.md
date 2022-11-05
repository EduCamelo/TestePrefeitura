# inicio
Eu iniciei meu projeto normalmentee, usando o django-admin startproject setup, e fiz as configurações básicas nele (como linguagem, horário, a pasta dos templates,e o app que eu iria utilizar), após isso eu alteirei as urls.py do meu setup para fazer um include(colocar todas os caminhos do meu app especifico de uma vez).

# Criando o App

eu iniciei meu app com o nome de core, criei o modelo de como eu queria minha class(em models.py), fui no admin.py para inserir um comando para que ele registasse essa classe, após isso fiz um makemigrations e migrate para salvar no banco de dados.

# Criando as definições e funções

Na views.py
criei funções para mostrar a página principal, para salvar, editar e deletar os links que o usuário colocou.

# Criando os caminhos

Na urls.py 
Criei as rotas de cada funções para o usuário "visualizar" as páginas

# Criando templates

Criei uma pasta de templates e criei os arquivos HTML(index, update, testelegal) 

# COMO UTILIZAR O PROJETO
primeiro utilize o pip install para baixar o django e o dotenv
após isso é só dar um python manage.py runserver
ir em qualquer navegar dor e digitar o endereço: http://127.0.0.1:8000

E pronto, só utilizar a página.
