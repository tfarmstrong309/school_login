from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get('https://twitter.com/login')
XPATH_username = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input'
XPATH_password = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input'
XPATH_button = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span'
time.sleep(6)
# Username input line
driver.find_element_by_xpath(XPATH_username).send_keys('OMMITED')
# Password
driver.find_element_by_xpath(XPATH_password).send_keys('OMMITED')
#Login button
driver.find_element_by_xpath(XPATH_button).click()



