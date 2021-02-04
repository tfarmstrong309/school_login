from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get('https://parents.mtps.com/moorestown/parents')

#Username and Password
m_username = 'OMMITED'
m_password = 'OMMITED'
#XPATH Variables
XPATH_username = '//*[@id="j_username"]'
XPATH_password = '//*[@id="j_password"]'
XPATH_loginbutton = '/html/body/form/div/div[2]/input[1]'
XPATH_ClaireCOVID = '/html/body/table[1]/tbody/tr[2]/td/table[1]/tbody/tr[4]/td[2]/a/span'
XPATH_EleanorCOVID = '/html/body/table[1]/tbody/tr[2]/td/table[1]/tbody/tr[10]/td[2]/a/span'
XPATH_AdamCOVID = '/html/body/table[1]/tbody/tr[2]/td/table[1]/tbody/tr[16]/td[2]/a/span'
XPATH_Verfication = '//*[@id="fldQuestion_48159F9B94B2409BAF899C57039D3759_C3E2410FA55F43CA84D9FA6426910A93"]'
XPATH_Submitbutton = '//*[@id="frmFill"]/p/input'

def select_by_value( webElement, value):
        '''
        This function selects an item given by
        the argument 'value' within the 'WebElement' object
        '''
        options = webElement.find_elements_by_tag_name("option")
        for option in options:
            if option.text == value:
                webElement.click()
                webElement.send_keys(option.text, Keys.RETURN)

time.sleep(3)
# Username input line
driver.find_element_by_xpath(XPATH_username).send_keys(m_username)
# Password
driver.find_element_by_xpath(XPATH_password).send_keys(m_password)
#Login button
driver.find_element_by_xpath(XPATH_loginbutton).click()

time.sleep(3)
# Claire Health Form
driver.find_element_by_xpath(XPATH_ClaireCOVID).click()
select_by_value(driver.find_element_by_xpath(XPATH_Verfication), "Yes")
time.sleep(3)
driver.find_element_by_xpath(XPATH_Submitbutton).click()

time.sleep(3)
# Eleanor Health Form
driver.find_element_by_xpath(XPATH_EleanorCOVID).click()
select_by_value(driver.find_element_by_xpath(XPATH_Verfication), "Yes")
time.sleep(3)
driver.find_element_by_xpath(XPATH_Submitbutton).click()

time.sleep(3)
# Adam Health Form
driver.find_element_by_xpath(XPATH_AdamCOVID).click()
select_by_value(driver.find_element_by_xpath(XPATH_Verfication), "Yes") 
time.sleep(3)
driver.find_element_by_xpath(XPATH_Submitbutton).click()

time.sleep(60)
