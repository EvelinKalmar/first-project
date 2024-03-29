from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option("excludeSwitches",
['enable-automation']);

driver = webdriver.Chrome("C:\\Users\\kalmarevelin\\chromedriver.exe", options=chrome_options)
driver.get("http://www.learnwebservices.com/empapp/employees.xhtml")

create = driver.find_element(By.XPATH, "/html/body/div/a").click()
input_name = driver.find_element(By.ID, "create-form:name-input").click()
title = driver.find_element(By.XPATH, "//body/div/h1").click()

WebDriverWait(driver, 10).until(
    expected_conditions.text_to_be_present_in_element((By.XPATH, "//span[@class = 'invalid-feedback']"),
                                                      "Az alkalmazott nevét meg kell adni!"))
message = driver.find_element(By.XPATH, "//span[@class = 'invalid-feedback']").text
print(message)

