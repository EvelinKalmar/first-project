from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\\Users\\kalmarevelin\\chromedriver.exe")
#driver = webdriver.Chrome()
driver.get("https://evelinkalmar.github.io/first-project/")
driver.find_element(By.ID, "a-input").send_keys("1")
driver.find_element(By.ID, "b-input").send_keys("1")
driver.find_element(By.ID, "submit-button").click()
result = driver.find_element(By.ID, "result-input").get_attribute("value")
print(result)
assert result == "2"



header_text = driver.find_element(By.ID, "//h1").text
print (header_text)
assert header_text == "Számológép"





