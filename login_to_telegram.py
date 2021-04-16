from selenium import webdriver
from time import sleep

def check(xpath):
    while True:
        try:
            driver.find_element_by_xpath(xpath)
            break
        except:
            pass

def send_key(xpath, key):
    driver.find_element_by_xpath(xpath).send_keys(key)

def click(xpath):
    driver.find_element_by_xpath(xpath).click()

# ---START--- #

# Getting the necessary items
country_name = input("Enter your acountry name: ")
phone_number = input("Enter your phone number(without your area code): ")

# Openning browser
driver = webdriver.Chrome(executable_path='/home/[username]/Desktop/chromedriver')
# Openning Telegram(web version)
driver.get('https://web.telegram.org/#/login')

check('//*[@id="ng-app"]/body/div[1]/div/div[2]/div[2]/form/div[1]/div')
print('Telegram opened!')

sleep(1)

click('//*[@id="ng-app"]/body/div[1]/div/div[2]/div[2]/form/div[1]/div')
check('//*[@id="ng-app"]/body/div[5]/div[2]/div/div/div[2]/div[1]/input')

# Filling in the login form
send_key('//*[@id="ng-app"]/body/div[5]/div[2]/div/div/div[2]/div[1]/input',country_name)
click('//*[@id="ng-app"]/body/div[5]/div[2]/div/div/div[2]/div[2]/div/div[1]/ul/li/a')
send_key('//*[@id="ng-app"]/body/div[1]/div/div[2]/div[2]/form/div[2]/div[2]/input',phone_number)
click('//*[@id="ng-app"]/body/div[1]/div/div[2]/div[1]/div/a')
click('//*[@id="ng-app"]/body/div[5]/div[2]/div/div/div[2]/button[2]')


check('//*[@id="ng-app"]/body/div[1]/div/div[2]/div[2]/form/div[4]/input')

# Getting the security code
security_code = input("Enter security code: ")  

send_key('//*[@id="ng-app"]/body/div[1]/div/div[2]/div[2]/form/div[4]/input',security_code)

check('//*[@id="ng-app"]/body/div[1]/div[2]/div/div[1]/div[2]/div/div[1]/ul/li[1]/a')
print("You have successfully logged in your Telegram account!")

# driver.close()

# --- The end --- #
