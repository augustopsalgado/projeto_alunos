# projeto_alunos
 Projeto da matéria Arquitetura de Software Aplicada

Para executar o programar basta executar o comando pipenv shell para entrar no ambiente virtual e depois executar o comando python3 run.py
Todos os endpoints podem ser acessados pelo swagger na rota -> http://127.0.0.1:5000/docs

os endpoints são os seguintes 

localhost:5000/auth/signup - para criar um usuario administrador no formato JSON
ex:
{
        "username":"Joao2",
        "email":"joao2@hotmail.com",
        "password":"password"
    }
localhost:5000/auth/login - para efetuar o login que fornecerá dois tipos de tokens 
e para logar 
{
	"username":"Augusto",
	"password":"password"
}

endpoints do CRUD

localhost:5000/aluno/criar - cria um novo aluno no formato JSON
{
  "nome_aluno": "Miguel4",
  "matricula": "003",
  "email": "miguel@email.com"
}

localhost:5000/aluno/"ID" - deleta um aluno pela id informada 
ex: localhost:5000/aluno/1

localhost:5000/aluno/1 - atualiza um aluno no formato JSON
ex:{
	"aluno":"teste3",
	"matricula":"003",
	"email":"teste3@email.com"
	
}


localhost:5000/aluno/listar - lista todos os alunos cadastrados 

localhost:5000/aluno/"ID" - lista um aluno pela ID
ex: localhost:5000/aluno/3