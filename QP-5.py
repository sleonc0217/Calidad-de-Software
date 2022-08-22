#------------------------------------------#
# Prueba de ingreso de productos-----------#
#------------------------------------------#

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time


driver=webdriver.Chrome(executable_path=r"C:\DriverDeChrome\chromedriver.exe")
driver.get("http://127.0.0.1:7800/")

try:


    login = driver.find_element("id", "login")
    login.send_keys(Keys.ENTER)

    usuario=driver.find_element("id", "username").send_keys("jose@test.com")
    contrasenha=driver.find_element("id", "password").send_keys("123")
    btnEnviar=driver.find_element("id", "enviar").send_keys(Keys.ENTER)

    driver.find_element("id", "dashboard-admin").click()
    driver.find_element("class name", "prod-nav").click()

    driver.find_element("class name", "btn-success").click()

    driver.find_element("id", "nombreP").send_keys("Producto de prueba")
    driver.find_element("id", "img").send_keys("C:\\Users\\sebas\\Desktop\\ProyectoAstull\\src\\main\\resources\\static\\image\\pepsi.png")
    driver.find_element("id", "cantidad").send_keys("5")
    driver.find_element("id", "precio").send_keys("1000")
    driver.find_element("id", "descripcion").send_keys("Esto es un producto de prueba")
    driver.find_element("class name", "btn-primary").click()




    
    time.sleep(3)
    driver.close()

    print("QP-5 finalizado correctamente...")
    



    
except:
    print("QP-5 Falló...")