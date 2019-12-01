from datetime import datetime, date
from sqlite3.dbapi2 import Date

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option("excludeSwitches",
['enable-automation']);

driver = webdriver.Chrome("C:\\Users\\kalmarevelin\\chromedriver.exe", options=chrome_options)
driver.get("http://www.learnwebservices.com/locations/?size=100")


def click_on_create_location():
    driver.find_element(By.ID, "create-location-link").click()


def wait_for_name_input():
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(
            (By.ID, "location-name")
        )
    )
    return driver.find_element(By.ID, "location-name")


def wait_for_coords_input():
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(
            (By.ID, "location-coords")
        )
    )
    return driver.find_element(By.ID, "location-coords")

def create_name():
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    location_name = 'Ajax_' + str(timestamp)
    return location_name


def type_location_name():
    location_name = create_name()
    driver.find_element(By.ID, "location-name").send_keys(location_name)

def type_coords(coord1, coord2):
    driver.find_element(By.ID, "location-coords").send_keys(coord1, ",", coord2)


def create_new_location():
    driver.find_element(By.XPATH, "//*[@id='location-form']/input[1]").click()

def location_has_created():
    WebDriverWait(driver, 10).until(
        expected_conditions.text_to_be_present_in_element((By.ID, "message-div"),
                                                              "Location has created"))
    message = driver.find_element(By.ID, "message-div").text
    print(message)


def wait_for_location_in_table():
    location_name = create_name()
    WebDriverWait(driver, 10).until(
        expected_conditions.text_to_be_present_in_element((By.ID, "locations-table"),
                                                          "Ajax_"))


def assert_coords():
    coords = driver.find_element(By.XPATH, "//tr[td[contains(text(), 'Ajax_')]]/td[3]").text
    print(type(coords))
    #assert coords == 10.0, 10.0


def blank_name_message():
    WebDriverWait(driver, 10).until(
        expected_conditions.text_to_be_present_in_element((By.ID, "message-div"),
                                                              "must not be blank"))
    message = driver.find_element(By.ID, "message-div").text
    print(message)


def blank_coord_message():
    WebDriverWait(driver, 10).until(
        expected_conditions.text_to_be_present_in_element((By.ID, "message-div"),
                                                              "invalid coordinates"))
    message = driver.find_element(By.ID, "message-div").text
    print(message)

def invalid_coord_message():
    WebDriverWait(driver, 10).until(
        expected_conditions.text_to_be_present_in_element((By.ID, "message-div"),
                                                              "invalid coordinates"))
    message = driver.find_element(By.ID, "message-div").text
    print(message)

def click_on_cancel():
    driver.find_element(By.ID, "create-cancel-button").click()


click_on_create_location()
wait_for_name_input()
wait_for_coords_input()
create_name()
type_location_name()
type_coords(10, 10)
create_new_location()
location_has_created()
wait_for_location_in_table()
assert_coords()

#click_on_create_location()
#wait_for_name_input()
#wait_for_coords_input()
#type_coords(11, 11)
#create_new_location()
#blank_name_message()
#click_on_cancel()

click_on_create_location()
wait_for_name_input()
wait_for_coords_input()
create_name()
type_location_name()
create_new_location()
blank_coord_message()
click_on_cancel()

click_on_create_location()
wait_for_name_input()
wait_for_coords_input()
create_name()
type_location_name()
type_coords(10,  10)
invalid_coord_message()

