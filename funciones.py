from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep
from easygui import *
import os

# Crea una instancia del driver y la devuelve
def generarDriver():
    rutaDriver = os.path.join(os.getcwd(),"chromedriver")
    driver = webdriver.Chrome(rutaDriver, chrome_options=Options()) 
    Options().add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/59.0.3071.115 Safari/537.36")
    return driver

# Se loguea con usuario y contraseña en Agendae
def ingresar(driver):
    driver.get('http://service.ssn.gob.ar/kausay/consulta_entidades.php')
    driver.maximize_window()
    aseguradoras = WebDriverWait(driver,30).until(EC.visibility_of_all_elements_located((By.XPATH, '//select[@id="bus_cia"]//option')))
    print(f"Se han encontrado {len(aseguradoras)} elementos")
    for i in range (1, len(aseguradoras)):
        aseguradoras = WebDriverWait(driver,30).until(EC.visibility_of_all_elements_located((By.XPATH, '//select[@id="bus_cia"]//option')))
        aseguradoras[i].click()
        botonOtraConsulta = encontrarElemento(driver, "botonOtraConsulta")
        botonOtraConsulta.click()
        sleep(3)

def paginaAnterior(driver):
    driver.execute_script("window.history.go(-1)")

def encontrarElemento(driver, elemento):
    if (elemento == "botonOtraConsulta"):
        botonOtraConsulta = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@class="btn btn-primary"]'))
            )
        return botonOtraConsulta