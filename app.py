from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import pandas as pd

contatos = pd.read_excel('contatos.xlsx')


print(contatos)

