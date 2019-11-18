from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\\Users\\kalmarevelin\\chromedriver.exe")
driver.get("http://www.learnwebservices.com/locations/server")
coordinates = driver.find_element(By.XPATH, "//tr[td[text() = 'Dobogókő']]/td[3]").text
print(type(coordinates))
city_id = driver.find_element(By.NAME, "Alattyán").text
print(type(city_id))
city_name = dirver.find_element(By.ID, "9277").text
print(type(city_name))

