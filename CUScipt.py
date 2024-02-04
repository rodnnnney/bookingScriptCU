from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import time

print("what month do you want to book, jan = 1 dec = 12 etc")
month =  input()
month_index = int(month) - 1
print("what day do you want to book example 1,12,24,31")
date = input()
date_index = int(date) 
print("what time do you want to start the booking? 11 or 2")
time1 = input()
if time1 == '11':
    time1 =  '//*[@id="eq-time-grid"]/div[2]/div/table/tbody/tr/td[3]/div/div/div/table/tbody/tr[42]/td/div/div[2]/div[6]/a/div/div/div'
if time1 == '2':
    time1 = '//*[@id="eq-time-grid"]/div[2]/div/table/tbody/tr/td[3]/div/div/div/table/tbody/tr[42]/td/div/div[2]/div[13]/a/div/div/div'



firstname = "kahin"
lastname = "ismail"
cmail = "kahinismail@cmail.carleton.ca"
driver = webdriver.Chrome()
driver.get("https://library.carleton.ca/services/study-rooms")
time.sleep(1)
WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.CLASS_NAME,"ml-button"))
)

button = driver.find_element(By.CLASS_NAME,"ml-button")
button.send_keys(Keys.ENTER)
time.sleep(1)
WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/main/div/div/div/div[4]/div[1]/div[1]/div[1]/button[1]"))
)
button = driver.find_element(By.XPATH , "/html/body/div[2]/main/div/div/div/div[4]/div[1]/div[1]/div[1]/button[1]")
button.click()

button_class_name = 'datepicker-switch'
button = driver.find_element(By.CLASS_NAME, button_class_name)
button.click()

button_class_name = 'month'
buttons = driver.find_elements(By.CLASS_NAME, button_class_name)
buttons[month_index].click() 
button_name = 'day'
buttons = driver.find_elements(By.CLASS_NAME, button_name)
buttons[date_index].click()
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, time1))
)
button = driver.find_element(By.XPATH, time1)
button.click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="bookingend_1"]'))
)
button = driver.find_element(By.XPATH,'//*[@id="bookingend_1"]')
button.click()

dropdown = driver.find_element(By.XPATH, '//*[@id="bookingend_1"]')
select = Select(dropdown)

# Get all options in the dropdown
options = select.options

# Select the last option
last_option_index = len(options) - 1
select.select_by_index(last_option_index)

WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.XPATH,'//*[@id="submit_times"]'
))
)
button = driver.find_element(By.XPATH,'//*[@id="submit_times"]'
)

button.click()

WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.XPATH,'//*[@id="terms_accept"]'))
)
button = driver.find_element(By.XPATH,'//*[@id="terms_accept"]')
button.click()

WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.ID,'fname'))
)
button = driver.find_element(By.ID,'fname')
button.send_keys(firstname)
button = driver.find_element(By.ID,'lname')
button.send_keys(lastname)
button = driver.find_element(By.ID,'email')
button.send_keys(cmail)

WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.XPATH,'//*[@id="btn-form-submit"]'
))
)
button = driver.find_element(By.XPATH,'//*[@id="btn-form-submit"]'
)
button.click()

time.sleep(60)

"""
id="fname"
id="lname" 
id="email" 
"""