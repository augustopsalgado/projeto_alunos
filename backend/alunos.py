from flask_restx import Namespace,Resource,fields
from werkzeug.security import generate_password_hash,check_password_hash
from models import Aluno
from flask_jwt_extended import JWTManager,create_access_token,create_refresh_token,jwt_required
from flask import Flask,request,jsonify,make_response

aluno_ns=Namespace('aluno',description="Aba com os campos de edição de alunos")


aluno_model=aluno_ns.model(
    "Aluno",
    {
        "id":fields.Integer(),
        "nome_aluno":fields.String(),
        "matricula":fields.String(),
        "email":fields.String()
    }
)





@aluno_ns.route('/listar')
class AlunosResource(Resource):

    @aluno_ns.marshal_list_with(aluno_model)
    def get(self):
        """Lista todos os alunos """

        alunos=Aluno.query.all()


        return alunos

@aluno_ns.route('/criar')
class AlunosResource(Resource):    
    @aluno_ns.expect(aluno_model)
    @jwt_required()
    def post(self):
        """Cria um novo aluno"""
        data=request.get_json()

        nome_aluno=data.get('nome_aluno')

        db_nome_aluno=Aluno.query.filter_by(nome_aluno=nome_aluno).first()

        if db_nome_aluno is not None:
            return jsonify({"message":f"Usuario com o username {nome_aluno} ja existe"})

        new_aluno=Aluno(
            nome_aluno=data.get('nome_aluno'),
            matricula=data.get('matricula'),
            email=data.get('email')
        )

        new_aluno.save()

        return make_response(jsonify({"message":"Aluno criado com sucesso"}),201)



@aluno_ns.route('/<int:id>')
class AlunoResource(Resource):

    @aluno_ns.marshal_with(aluno_model)
    def get(self,id):
        """busca um aluno pela id """
        aluno=Aluno.query.get_or_404(id)

        return aluno


    @aluno_ns.marshal_with(aluno_model)
    @jwt_required()
    def put(self,id):
        """Atualiza um aluno pela id """


        aluno_to_update=Aluno.query.get_or_404(id)

        data=request.get_json()

        aluno_to_update.update(data.get('nome_aluno'),data.get('matricula'),data.get('email'))

        return aluno_to_update


    @aluno_ns.marshal_with(aluno_model)
    @jwt_required()
    def delete(self,id):
        """Deleta um aluno pela id """

        aluno_to_delete=Aluno.query.get_or_404(id)

        aluno_to_delete.delete()

        return aluno_to_delete