from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option("excludeSwitches",
['enable-automation']);

driver = webdriver.Chrome("C:\\Users\\kalmarevelin\\chromedriver.exe", options=chrome_options)
driver.get("http://www.learnwebservices.com/empapp/employees.xhtml")

create = driver.find_element(By.XPATH, "/html/body/div/a").click()
input_name = driver.find_element(By.ID, "create-form:name-input").click()
title = driver.find_element(By.XPATH, "//body/div/h1").click()
message = driver.find_element(By.XPATH, "//span[@class = 'invalid-feedback']").text
print(message)

