from exts import db

"""
class Aluno:
    id: int primary key
    nome_aluno:str
    matricula:str (text)
    email:str
"""

class Aluno(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    nome_aluno=db.Column(db.String(50),nullable=False,unique=True)
    matricula=db.Column(db.Text(20),nullable=False,unique=True)
    email=db.Column(db.String(80),nullable=False,unique=True)

    def __repr__(self):
        return f"<Aluno {self.nome_aluno} >"


    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self,nome_aluno,matricula,email):
        self.nome_aluno=nome_aluno
        self.matricula=matricula
        self.email=email

        db.session.commit()

#user model

""""
class User:
    id:integer
    username:string
    email:string
    password:string
"""
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(25),nullable=False,unique=True)
    email=db.Column(db.String(80),nullable=False)
    password=db.Column(db.Text(),nullable=False)

    def __repr__(self):
         return f"<User {self.username}>"


    def save(self):
        db.session.add(self)
        db.session.commit()