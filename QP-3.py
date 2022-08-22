#------------------------------------------#
#Crear una cuenta en la web----------------#
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

    #Ingresamos a crear cuenta
    btnCrear=driver.find_element("id", "crearCuenta")
    btnCrear.send_keys(Keys.ENTER)

    #Llenamos los datos
    nombre=driver.find_element("id", "idNombre").send_keys("nomPrueba")
    apellido1=driver.find_element("id", "id1erA").send_keys("ape1Prueba")
    apellido2=driver.find_element("id", "idSegA").send_keys("ape2Prueba")
    email=driver.find_element("id", "idCorreo").send_keys("prueba@prueba.com")
    telefono=driver.find_element("id", "idTelefono").send_keys("88888888")
    password=driver.find_element("id", "contrasena").send_keys("123")
    activo=driver.find_element("id", "active").clear()
    activo=driver.find_element("id", "active").send_keys("true")
    credito=driver.find_element("id", "idCredito").send_keys("10000")   
    btnRegistro=driver.find_element("id", "btnRegistro").send_keys(Keys.ENTER)




    time.sleep(3)
    driver.close()


    print("QP-3 finalizado correctamente...")



except:
    print("QP-3 Falló...")

