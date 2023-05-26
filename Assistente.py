# Classe assistente
from Tarefas import Notepad
from Spotify import Spotify
import webbrowser

def abrir_arquivo_no_chrome(caminho_arquivo):
    url = caminho_arquivo
    webbrowser.get('chrome').open(url)

class Assistente ():
    def __init__(self, nome, funcao , solicitacao):
        self.nome = nome 
        self.funcao = funcao
        self.solicitacao = solicitacao
    def query(self):
        #return('Eu sou ' + self.nome + ' seu assistente virtual.' + 'minha função é ' + self.funcao)
        return ( f"Eu sou {self.nome} seu assistente virtual. Minha função é {self.funcao}. {self.solicitacao}" )
        
class Tarefa ():
    def __init__(self, titulo, texto):
        self.titulo = titulo
        self.texto = texto

# Criando dois assistentes
Assistente1 = Assistente('Pedro','abrir seu spotify e criar uma playlist','')
Assistente2 = Assistente('Laura','salvar e organizar suas tarefas', 'qual a tarefa ou lembrete que você gostaria de agendar?')
Assistente3 = Assistente('Vinícius','Abrir Prompts do CHATGPT','')
# Criar aqui um seletor
'''
perguntar: Qual assistente gostaria de usar assistente: 1, 2 ou 3?
if 1, Query1
if 2, Query2
if 3, Query3 > função de abrir arquivo index.html em ..ProjetoFrontGPT
'''
escolha = input('qual assistente você gostaria de ultilizar? 1-Spotify ; 2-Tarefas ; 3-Prompts do ChatGPT; Responda: 1,2 ou 3')
# Query
if escolha == "1":
    print(Assistente1.query())
    spotify = Spotify()
    spotify.criar_playlist()
    
if escolha == "2":
    print(Assistente2.query())
    respostatexto = input('sua resposta: ')
    print("qual o título do lembrete/tarefa? ")
    respostatitulo = input('sua resposta: ')
    Tarefa1 = Tarefa(respostatitulo,respostatexto)
    #
    print(f"{Tarefa1.titulo} será salvo em uma nova nota na área de trabalho.")
    notepad = Notepad()
    notepad.escrever_tarefa(f"{respostatitulo}.txt",respostatexto)
if escolha == "3":
    caminho_arquivo = 'caminho/do/arquivo.html'
    abrir_arquivo_no_chrome(r'.\ProjetoFrontGPT\index.html') 
    # Interação no Console
# Criar
