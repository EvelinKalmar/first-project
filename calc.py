from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\\Users\\kalmarevelin\\chromedriver.exe")
#driver = webdriver.Chrome()
driver.get("https://evelinkalmar.github.io/first-project/")
#driver.find_element(By.ID, "a-input").send_keys("1")

first_number = input("Elso szam")
second_number = input("Masodik")
first_input_field = driver.find_element(By.ID, "a-input")
first_input_field.send_keys(first_number)
#first_input_field.screenshot("first-input.png")
second_input_field = driver.find_element(By.ID, "b-input")
second_input_field.send_keys(second_number)
#driver.find_element(By.ID, "b-input").send_keys("1")
driver.find_element(By.ID, "submit-button").click()
result = driver.find_element(By.ID, "result-input").get_attribute("value")
#print(result)
driver.save_screenshot("result.png")
expected = int(first_number) + int(second_number)
print(expected)
print(result)
print(type(expected))
print(type(result))
assert int(result) == expected



header_text = driver.find_element(By.ID, "//h1").text
print (header_text)
assert header_text == "Számológép"

# megjegyzés -> önmagát kell leírnia, nem kell megjegyzés, legyen beszédes neve minden változónak, kisbetűvel, betűnek kell az első karakterének lennie
# foglalt szavakat nem használhatunk -> pl. True -> kulcsszó






