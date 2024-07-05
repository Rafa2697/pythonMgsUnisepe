from selenium import webdriver
import webbrowser
from time import sleep

# Abrir a página com o webbrowser
webbrowser.open('https://web.whatsapp.com/')

# Esperar alguns segundos para que a página carregue completamente
sleep(5)

# Criar instância do driver do Chrome
driver = webdriver.Chrome()

# Obter todas as guias abertas
todas_as_guias = driver.window_handles

# Alternar para a última guia aberta (que é a guia do webbrowser)
ultima_guia = todas_as_guias[-1]
driver.switch_to_window(ultima_guia)

# Localizar o botão que você deseja clicar
botao = driver.find_element_by_id('meu-botao')

# Clicar no botão
botao.click()
