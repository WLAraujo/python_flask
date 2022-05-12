from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

usuarios = {"Wesley" : 21,
            "Andre" : 34}

class Perfil(Resource):
    # Definindo função de get que retorna informações contidas no dicionário
    def get(self, nome):
        return {"nome":nome,"idade":usuarios[nome]}
    # Definindo função post que escreve novo nome no dicionário
    def post(self, nome, idade):
        usuarios[nome] = idade
    
# Configurando o resource e parâmetros que podem ser passados na chamada
api.add_resource(Perfil, "/<string:nome>/<int:idade>/", "/<string:nome>/")

if __name__ == "__main__":
    # Configurar para modo de debug que sempre devolve os logs
    # Só rodar em ambientes de produção
    app.run(debug=True)
    
