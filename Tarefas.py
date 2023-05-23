import time
import pyautogui as batata
from FunctionTarefas import clicar_imagem_se_encontrada, escrever, esperar_imagem_aparecer, escrever_tarefa

class Notepad: 
    def __init__(self):
        self.arquivo = ""
        self.texto = ""
    def set_arquivo(self, arquivo):
        self.arquivo=arquivo
    def set_texto(self, texto):
        self.texto=texto
    def escrever_tarefa(self, arquivo, texto):
        self.set_arquivo(arquivo)
        self.set_texto(texto)
        with open(self.arquivo , "a+") as arquivo_log:
            arquivo_log.write(f'{self.texto}')

Notepad().escrever_tarefa("arquivo.txt","pergunta")


'''
clicar_imagem_se_encontrada('win.png')
time.sleep(1)
clicar_imagem_se_encontrada('not.png')
time.sleep(1)
escrever_tarefa()
batata.keyDown('shift')
clicar_imagem_se_encontrada('fire.png')
batata.keyUp('shift')
time.sleep(3)

clicar_imagem_se_encontrada('bitrix.png')

esperar_imagem_aparecer('bwaLogo.png')
time.sleep(1)
clicar_imagem_se_encontrada('notifBitrix0.png')
clicar_imagem_se_encontrada('notifBitrix.png')


'''