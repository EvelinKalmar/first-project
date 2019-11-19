from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\\Users\\kalmarevelin\\chromedriver.exe")
driver.get("http://www.learnwebservices.com/locations/server")

coordinates = driver.find_element(By.XPATH, "//tr[td[text() = 'Dobogókő']]/td[3]").text
print(type(coordinates))
city_id = driver.find_element(By.XPATH, "//tr[td[text() = 'Alattyán']]/td[1]").text
print(type(city_id))
city_name = driver.find_element(By.ID, "9277").text
print(type(city_name))

city_int = driver.find_element(By.XPATH, "//tr[td[text() = 'Bakonybánk']]/td[1]").text
print(int(city_int))
print(type(city_int))

city_float = driver.find_element(By.XPATH, "//tr[td[text() = 'Zsámbék']]/td[3]").text
print(float(city_float))
print(type(city_float))
