from selenium import webdriver
from selenium.webdriver.common.by import By
#import random

driver = webdriver.Chrome("C:\\Users\\kalmarevelin\\chromedriver.exe")
driver.get("http://www.jtechlog.hu/tesztautomatizalas-201909/szorzotabla.html")

first_number = input("Elso szam")
second_number = input("Masodik szam")
def multiply_with_form():
    first_input_field = driver.find_element(By.ID, "a-input")
    first_input_field.send_keys(first_number)
    second_input_field = driver.find_element(By.ID, "b-input")
    second_input_field.send_keys(second_number)
    driver.find_element(By.ID, "calculate-button").click()
    result1 = driver.find_element(By.ID, "result-div").text
    print(result1)
    print(type(result1))
    print(type(int(result1)))
    return result1

def multiply_with_table():
    print("Ügyes vagy!")
    return 2

def multiply():
    result3 = int(first_number) * int(second_number)
    print(result3)
    return result3

result_first = multiply_with_form()
result_second = multiply_with_table()
result_third = multiply()

assert int(result_first) == int(result_third), "false"
