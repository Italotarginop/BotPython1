import time
import pyperclip
from Xpath import xpath

from Function import pesquisar_programa
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

pesquisar_programa('spot')
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
