# FunctionTarefas
import pyautogui as batata
import time
import keyboard

def esperar_imagem_aparecer(nome_imagem,timeout=10):
    while True:
        if (not timeout):
            return False
        image_location = batata.locateOnScreen(nome_imagem, confidence=0.99)
        if image_location is not None:
           return image_location
        time.sleep(1)
        timeout = timeout - 1
        

def clicar_imagem_se_encontrada(nome_imagem,timeout=10):
    try:
        image_location = esperar_imagem_aparecer(nome_imagem,timeout)
        time.sleep(0.5)
        batata.click(image_location)
    except:
        print(nome_imagem)

def escrever(texto, presses=1):
    keyboard.write(texto, delay=0.01)
    for x in range(presses):
        keyboard.press_and_release('enter')

def escrever_tarefa():
    escrever('Titulo da tarefa: ')
    escrever(r' Descrição')
    escrever('- ',0)
    batata.keyDown('ctrl')
    batata.press('v')
    batata.keyUp('ctrl')
    batata.press('enter', presses=2)
    escrever('De: ')
    escrever('Fonte: ',presses=2)