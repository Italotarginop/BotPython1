class Alunos:
	def __init__(self, nome , matricula, email, nota1 = "a fazer", nota2 = "a fazer"):
		self.nome = nome
		self.matricula = matricula
		self.email = email
		self.nota1 = nota1
		self.nota2 = nota2

class Professores:
	def __init__(self, codigo, disciplinas, turmas):
		self.codigo = codigo
		self.disciplinas = disciplinas
		self.turmas = turmas

class Secretaria_funcoes:
	def __init__(self, gerarBoleto, funcao1, funcao2, funcao3):
		self.gerarBoleto = gerarBoleto
		self.funcao1 = funcao1
		self.funcao2 = funcao2
		self.funcao3 = funcao3

Joao = Alunos("João",20230525, "jaozinho@gmail.com", "7")
Claudio = Alunos("Claudio", 20230505, "email.@email.com")

print(Joao.email,Joao.nome)
print(Claudio.nome)
print("olá",Joao.nome,"sua nota é:",Joao.nota1)