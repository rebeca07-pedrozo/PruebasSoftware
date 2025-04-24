import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--start-maximized")

service = Service("C:/Users/USUARIO/OneDrive/Documentos/5toSemestre/ProgramacionII/chromeDriver/chromedriver.exe")

driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("http://localhost:5173/#/login")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )
    driver.find_element(By.NAME, "email").send_keys("juanp-marqueza@unilibre.edu.co")
    driver.find_element(By.NAME, "password").send_keys("12345678")

    driver.find_element(By.XPATH, "//button[contains(text(),'Iniciar')]").click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("#/upload")
    )

    upload_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
    )
    upload_input.send_keys(r"C:/Users/USUARIO/OneDrive/Documentos/5toSemestre/IngenieriadeSoftwareIII/Doc pruebas/TC1_carga_exitosa.xlsx")

    time.sleep(2)  

    driver.find_element(By.XPATH, "//button[contains(text(),'Cargar')]").click()

    time.sleep(5)  

finally:
    driver.quit()
