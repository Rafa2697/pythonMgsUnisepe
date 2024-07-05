
import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui
import os 
from selenium import webdriver

webbrowser.open('https://web.whatsapp.com/')
sleep(20)

driver = webdriver.Chrome()
# Obter todas as guias abertas
todas_as_guias = driver.window_handles

ultima_guia = todas_as_guias[-1]
driver.switch_to_window(ultima_guia)

# Ler planilha e guardar informações sobre nome, telefone e data de vencimento
workbook = openpyxl.load_workbook('contatos.xlsx')
pagina_contatos = workbook['Sheet1']

for linha in pagina_contatos.iter_rows(min_row=2):
    # nome, telefone, vencimento
    nome = linha[0].value
    telefone = linha[1].value
    texto = linha[3].value
    
    
    mensagem = f'Olá {nome}, {texto}'

    # Criar links personalizados do whatsapp e enviar mensagens para cada cliente
    # com base nos dados da planilha
    try:
        link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
        webbrowser.open(link_mensagem_whatsapp)
        sleep(10)
        campo_mensagem = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div')
        botao_enviar = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')

        sleep(5)
        pyautogui.hotkey('ctrl','w')
        sleep(5)
    except:
        print(f'Não foi possível enviar mensagem para {nome}')
        with open('erros.csv','a',newline='',encoding='utf-8') as arquivo:
            arquivo.write(f'{nome},{telefone}{os.linesep}')
    

        raise