from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option("excludeSwitches",
['enable-automation']);

driver = webdriver.Chrome("C:\\Users\\kalmarevelin\\chromedriver.exe", options=chrome_options)
driver.get("http://www.learnwebservices.com/locations/?size=100")

def print_when_lat_greater_than_48(name):
    lat = find_lat_by_name(name)
    if lat > 48:
        print("Szélesség nagyobb mint 48")
    else:
        print("Szélesség kisebb mint 48")

def find_lat_by_name(name):
    wait_xpath = "//tbody/tr"
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, wait_xpath)))
    xpath = "//tr[td[contains(text(), 'name')]]/td[3]".replace("name", name)
    coords = driver.find_element(By.XPATH, xpath).text
    print(coords)
    lat = float(coords[0:coords.index(",")])
    print(lat)
    return lat

def print_when_lat_between(name):
    lat = find_lat_by_name(name)
    if lat < 48.2 and lat < 48.4:
        print("Közé esik")
    else:
        print("Nem esik közé")


print_when_lat_greater_than_48("Ajax")
print_when_lat_greater_than_48("fityiszváros")
print_when_lat_between("Ajax")
