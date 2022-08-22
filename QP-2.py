#------------------------------------------#
# Prueba de el inicio de sesión en la web.-#
#------------------------------------------#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time


driver=webdriver.Chrome(executable_path=r"C:\DriverDeChrome\chromedriver.exe")
driver.get("http://127.0.0.1:7800/")

try:

    input_field = driver.find_element("id", "login")
    input_field.send_keys(Keys.ENTER)

    usuario=driver.find_element("id", "username").send_keys("test@test.com")
    contrasenha=driver.find_element("id", "password").send_keys("123")
    btnEnviar=driver.find_element("id", "enviar").send_keys(Keys.ENTER)


    time.sleep(3)
    driver.close()

    print("QP-2 finalizado correctamente...")
    
except:
    print("QP-2 Falló...")


