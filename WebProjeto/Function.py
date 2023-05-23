import pyautogui
import time

#Funções

#pesquisar e executar programa no menu iniciar
def pesquisar_programa(nome_programa):
    pyautogui.press('win')
    time.sleep(0.5)  # Pequena pausa para garantir que o menu Iniciar esteja aberto
    pyautogui.write(nome_programa)
    time.sleep(0.5)  # Pequena pausa para garantir que o texto tenha sido digitado
    pyautogui.press('enter')

