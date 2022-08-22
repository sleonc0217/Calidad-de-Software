#------------------------------------------#
#Prueba de ingresar al modulo de productos-#
#------------------------------------------#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time


driver=webdriver.Chrome(executable_path=r"C:\DriverDeChrome\chromedriver.exe")
driver.get("http://127.0.0.1:7800/")

try:

    input_field = driver.find_element("id", "productos")
    input_field.send_keys(Keys.ENTER)


    time.sleep(3)
    driver.close()

    print("QP-4 finalizado correctamente...")
    
except:
    print("QP-4 Falló...")







 

 

 
