from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option("excludeSwitches",
['enable-automation']);

driver = webdriver.Chrome("C:\\Users\\kalmarevelin\\chromedriver.exe",options=chrome_options)
driver.get("http://www.learnwebservices.com/empapp/employees.xhtml")

def search(word):
    query = driver.find_element(By.NAME, "query")
    query.send_keys(word)
    submit = driver.find_element(By.XPATH, ("//html/body/div/form[2]/input[2]")).click()

def deletebyid(id):
    employee_id = driver.find_element(By.XPATH, "/html/body/div/table/tbody/tr[td[a[text() = 'id']]]/td[last()]/form/input[@type = 'submit'").text

def deletebyname():
    delete = driver.find_element(By.CSS_SELECTOR, ("#j_idt21\:0\:j_idt42 > input[type=submit]:nth-child(2)")).click()

def hungarian():
    hun = driver.find_element(By.XPATH, ("/html/body/div/form[1]/a[1]")).click()

def english():
    eng = driver.find_element(By.XPATH, ("/html/body/div/form[1]/a[2]")).click()

def create_employee(name):
    create = driver.find_element(By.XPATH, ("/html/body/div/a")).click()
    input_name = driver.find_element(By.NAME, "create-form:name-input")
    input_name.send_keys(name)
    create_button = driver.find_element(By.ID, "create-form:save-button").click()

def errormessage():
    message = driver.find_element(By.XPATH, ("/html/body/div/form/div[1]/span")).text
    print(message)

def cardnumber(number):
    input_cardnumber = driver.find_element(By.ID, "create-form:card-number-input")
    input_cardnumber.send_keys(number)
    create_button = driver.find_element(By.ID, "create-form:save-button").click()

def create_employee_full(name,number):
    create_employee(name)
    cardnumber(number)

def update_name(new_name):
    driver.find_element(By.XPATH, "/html/body/div/table/tbody/tr[5]/td[1]/a").click()
    input_name = driver.find_element(By.ID, "j_idt11:name")
    #input_name.replace("Emp Loyee", "New Name")
    input_name.clear()
    input_name.send_keys(new_name)
    update_button = driver.find_element(By.NAME, "j_idt11:j_idt12").click()

#search("Jane Doe")
#deletebyname()
#hungarian()
#english()
#create_employee("")
#errormessage()
#create_employee("Emp Loyee")
#cardnumber(12345678)
#create_employee_full("Jet Lee",243212)
update_name("New Name")