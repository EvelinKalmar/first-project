from selenium import webdriver
from selenium.webdriver.common.by import By
import random

driver = webdriver.Chrome("C:\\Users\\kalmarevelin\\chromedriver.exe")
driver.get("http://www.jtechlog.hu/tesztautomatizalas-201909/szorzotabla.html")

#first_number = input("Elso szam")
#second_number = input("Masodik")
first_input_field = driver.find_element(By.ID, "a-input")
first_input_field.send_keys(random.randint(1, 10))
second_input_field = driver.find_element(By.ID, "b-input")
second_input_field.send_keys(random.randint(1, 10))
driver.find_element(By.ID, "calculate-button").click()

result = driver.find_element(By.ID, "result-div").text
print(result)
print(type(result))
print(type(int(result)))
