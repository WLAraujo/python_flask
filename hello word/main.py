from flask import Flask
from flask_restful import Api, Resource

# Abaixo criamos um app usando flask e o encapsulamos dentro de uma API
app = Flask(__name__)
api = Api(app)

# Vamos criar uma classe "resource" de HelloWorld
# O fato de ser um "resource" faz com que essa classe seja capaz de conter métodos
# com métodos como get e post
class HelloWorld(Resource):
    # Definindo função de get que retorna um dicionário
    def get(self):
        return {"dados":"Hello World"}
    # Definindo função com método post
    def post(self):
        return {"dados":"post"}
        
# Após criarmos a classe precisamos configurar ela como um Resource
# Também configuramos a chave associada ao Resource
api.add_resource(HelloWorld, "/helloworld")

if __name__ == "__main__":
    # Configurar para modo de debug que sempre devolve os logs
    # Só rodar em ambientes de produção
    app.run(debug=True)