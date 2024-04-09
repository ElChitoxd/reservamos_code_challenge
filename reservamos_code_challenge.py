from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import time
import getopt,sys

driver = None
first_name = "Jhon"
last_name = "Doe"
email = "Jhon@reservamos.com"
phone_number = "8115010101"
card_number = "2222 4000 7000 0005"
cvv_number = "737"
expiration_date = "03/30"
departure_button_xpath = (By.XPATH,"//*[@id='txtorigin-desktop']")
departure_element_xpath = (By.XPATH, "//div[contains(text(), 'Cdmx')]")
destination_element_xpath = (By.XPATH, "//div/p[contains(text(), 'León')]")
day_element_xpath = (By.XPATH, "//td/div[@class='picker__day picker__day--infocus']")
search_button_xpath = (By.XPATH, "//button[text()='Buscar']")
choose_trip_array_buttons_xpath = (By.XPATH, "//div[@class='matrix-action']/button")
choose_seat_number_array_buttons_xpath = (By.XPATH, "//div[@class='seats-layout-bus-space']/button")
continue_button_xpath = (By.XPATH, "//button[@class='main-button  ']")
passenger_first_name_field_xpath = (By.XPATH, "//input[contains(@id,'firstName')]")
passenger_last_name_field_xpath = (By.XPATH, "//input[contains(@id,'lastName')]")
passenger_email_field_xpath = (By.XPATH, "//input[contains(@id,'email')]")
use_same_info_checkbox_xpath = (By.XPATH, "//span[@class='css-7w7wvt-D']")
passenger_number_field_xpath = (By.XPATH, "//input[@id='phone']")
select_visa_card_xpath = (By.XPATH, "//button[@class='css-14dhpkf-D']")
card_number_field_xpath = (By.XPATH, "//input[contains(@id,'CardNumber')]")
expiry_date_field_xpath = (By.XPATH, "//input[contains(@id,'ExpiryDate')]")
cvv_number_field_xpath = (By.XPATH, "//input[contains(@id,'SecurityCode')]")
holder_name_field_xpath = (By.XPATH, "//input[contains(@id,'holderName')]")
confimation_message_xpath = (By.XPATH, "//*[text()='¡Muchas gracias!']")
secondAssert = (By.XPATH, "//*[contains(text(),'horario')]")
thirdAssert = (By.XPATH, "//*[contains(text(),'Tu viaje de ida')]")
quadAssert = (By.XPATH, "//*[contains(text(),'identificación')]")
fifthAssert = (By.XPATH, "//*[contains(text(),'comprador')]")
    
    
def clickElement(driver, xpath, timeout):
    WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(xpath)).click()
    
def sendKeys(driver, xpath, timeout, text):
    element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(xpath))
    element.clear()
    element.send_keys(text)
    
def getText(driver, xpath, timeout):
    element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(xpath))
    return element.text
    
def getElements(driver, xpath, timeout):
    elements = WebDriverWait(driver, timeout).until(EC.presence_of_all_elements_located(xpath))
    return elements
    
def selectRandomElement(driver, xpath, timeout):
    myElements = getElements(driver, xpath, timeout)
    randomIndex = random.randint(0, len(myElements)-1)
    myElements[randomIndex].click()
    
def isElementDisplayed(driver, xpath, timeout):
    element  =WebDriverWait(driver, timeout).until(EC.presence_of_element_located(xpath))

def test_RollBits(mode="headfull", driverType="chrome"):
    if driverType in "chrome":
        options = webdriver.ChromeOptions()
        service = Service(executable_path="./drivers/chromedriver.exe")
        if mode in "headless":
            options.add_argument("--headless")
        else:
            options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=service, options=options)
    else:
        options = webdriver.EdgeOptions()
        if mode in "headless":
            options.add_argument("--headless")
        else:
            options.add_argument("--start-maximized")
        service = Service(executable_path="./drivers/msedgedriver.exe")
        driver = webdriver.Edge(service=service, options=options)
    driver.get("https://roll-bits.reservamos-saas.com/")
    assert "Las mejores opciones para tus viajes" in driver.title
    clickElement(driver,departure_button_xpath,30)
    clickElement(driver,departure_element_xpath,30)
    clickElement(driver,destination_element_xpath,30)
    clickElement(driver,day_element_xpath,30)
    clickElement(driver,search_button_xpath,30)
    selectRandomElement(driver, choose_trip_array_buttons_xpath, 30)
    selectRandomElement(driver, choose_seat_number_array_buttons_xpath, 30)
    clickElement(driver,continue_button_xpath,30)
    sendKeys(driver,passenger_first_name_field_xpath,30,first_name)
    sendKeys(driver,passenger_last_name_field_xpath,30, last_name)
    sendKeys(driver,passenger_email_field_xpath,30, email)
    clickElement(driver,continue_button_xpath,30)
    time.sleep(15)
    clickElement(driver,use_same_info_checkbox_xpath,30)
    sendKeys(driver,passenger_number_field_xpath,30, phone_number)
    clickElement(driver,select_visa_card_xpath,30)
    driver.switch_to.frame(0)
    sendKeys(driver,card_number_field_xpath,30, card_number)
    driver.switch_to.default_content()
    driver.switch_to.frame(1)
    sendKeys(driver,expiry_date_field_xpath,30, expiration_date)
    driver.switch_to.default_content()
    driver.switch_to.frame(2)
    sendKeys(driver,cvv_number_field_xpath,30, cvv_number)
    driver.switch_to.default_content()
    sendKeys(driver,holder_name_field_xpath,30, first_name + " " + last_name)
    clickElement(driver,continue_button_xpath,30)
    thanksMessage = getText(driver,confimation_message_xpath,30)
    assert "¡Muchas gracias!" in thanksMessage
    
if __name__ == "__main__":
    """ argumentList = sys.argv[1:]
    
    # Options
    options = "hfec:"
    
    # Long options
    long_options = ["Headless", "Full", "Edge","Chrome"]
    mode = ""
    driverType = ""
    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)
        
        # checking each argument
        for currentArgument, currentValue in arguments:
    
            if currentArgument in ("-h", "--Headless"):
                mode = "headless"
                
            elif currentArgument in ("-f", "--Full"):
                mode = "full"
            elif currentArgument in ("-e", "--edge"):
                driverType = "edge"
            elif currentArgument in ("-c", "--Chrome"):
                driverType = "chrome"
                
    except getopt.error as err:
        # output error, and return with an error code
        print (str(err))
    print(sys.argv) """
    test_RollBits()