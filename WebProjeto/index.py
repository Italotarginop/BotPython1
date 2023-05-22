import time
import pyperclip
import pyautogui
from Xpath import xpath

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def pesquisar_programa(nome_programa):
    pyautogui.press('win')
    time.sleep(0.5)  # Pequena pausa para garantir que o menu Iniciar esteja aberto
    pyautogui.write(nome_programa)
    time.sleep(0.5)  # Pequena pausa para garantir que o texto tenha sido digitado
    pyautogui.press('enter')

# Instalação e configuração do WebDriver para o Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())

# Acessar o site Speedtest
driver.get("https://www.speedtest.net/pt")

wait = WebDriverWait(driver, 10)
elemento_xpath = wait.until(EC.visibility_of_element_located((By.XPATH, xpath['botoes']['iniciar'])))
elemento_xpath = driver.find_element(By.XPATH, xpath['botoes']['iniciar'])
elemento_xpath.click()
wait = WebDriverWait(driver, 120)
elemento2_classe = wait.until(EC.visibility_of_element_located((By.XPATH, xpath['botoes']['fim'])))
# elementoFim_xpath = wait.until(EC.visibility_of_element_located((by.XPATH, ""))) >>btn-server-select
# Fechar o navegador
time.sleep(2)
# Capturar o texto do elemento
elemento = driver.find_element(By.XPATH, xpath['dados']['log'])
texto = elemento.text
# textoLog 
with open("logVelocidade.txt", "a+") as arquivo_log:
    arquivo_log.write(f'{texto}\n\n')
'''
pyperclip.copy(texto)
driver.quit()

pyautogui.press('win')
time.sleep(0.5)
pyautogui.write('bloco')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.keyDown('ctrl')
pyautogui.press('v')
pyautogui.keyUp('ctrl')
'''


'''from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Instalação e configuração do WebDriver para o Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())

# Acessar o site
driver.get("https://www.exemplo.com")

# Procurar um elemento por ID
elemento_id = driver.find_element(By.ID, "id_do_elemento")

# Procurar um elemento por classe
elemento_classe = driver.find_element(By.CLASS_NAME, "nome_da_classe")

# Procurar um elemento por XPath
elemento_xpath = driver.find_element(By.XPATH, "//div[@id='exemplo']")

# Procurar um elemento por seletor CSS
elemento_css = driver.find_element(By.CSS_SELECTOR, "h1.titulo")

# Procurar um elemento por link de texto
elemento_link_text = driver.find_element(By.LINK_TEXT, "Texto do link")

# Procurar um elemento por parte do link de texto
elemento_partial_link_text = driver.find_element(By.PARTIAL_LINK_TEXT, "Parcial do texto do link")

# Fechar o navegador
driver.quit()
'''