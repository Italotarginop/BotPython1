#FunctionsSpotify
import pyautogui
import time

# Pressionar a tecla do Windows e digitar o programa
def pesquisar_programa(nome_programa):
    pyautogui.press('win')
    time.sleep(0.5)  # Pequena pausa para garantir que o menu Iniciar esteja aberto
    pyautogui.write(nome_programa)
    time.sleep(0.5)  # Pequena pausa para garantir que o texto tenha sido digitado
    pyautogui.press('enter')

# Esperar a imagem aparecer
def esperar_imagem_aparecer(nome_imagem, timeout=10):
    while timeout > 0:
        image_location = pyautogui.locateOnScreen(nome_imagem, confidence=0.99)
        if image_location is not None:
            return image_location
        time.sleep(1)
        timeout -= 1
    return False

# Clicar na imagem se encontrada
def clicar_imagem_se_encontrada(nome_imagem, timeout=10):
    image_location = esperar_imagem_aparecer(nome_imagem, timeout)
    if image_location:
        time.sleep(0.5)
        pyautogui.click(image_location)

def clicar_direito_se_encontrada(nome_imagem, timeout=10):
    image_location = esperar_imagem_aparecer(nome_imagem, timeout)
    if image_location:
        time.sleep(0.5)
        pyautogui.rightClick(image_location)



def rolar_barra_para_baixo(pixels):
    pyautogui.scroll(-pixels)

def pesquisar_musica(artista_nome,musica_nome):
    pyautogui.write(artista_nome + musica_nome)
    