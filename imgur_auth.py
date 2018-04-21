from imgurpython import ImgurClient

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

id=''
secret=''
username = ''
password = ''

##client = ImgurClient(client_id, client_secret)
##items = client.gallery()
#print(items)

####for items in items:
####    print(items.link)
####    print(items.title)
####    print(items.views)

def auth():
    client_id=id
    client_secret=secret
    imgur_username = username
    imgur_password = password
    client = ImgurClient(client_id, client_secret)
    auth_url = client.get_auth_url('pin')
    print(auth_url)
    #driver = webdriver.Firefox(executable_path='C:\Users\krawat\AppData\Local\Programs\Python\Python36\Scripts\geckodriver.exe')
    driver = webdriver.Firefox(executable_path='C:\\Users\\krawat\\AppData\\Local\\Programs\\Python\\Python36\\Scripts\\geckodriver.exe')
    driver.get(auth_url)
    username = driver.find_element_by_xpath('//*[@id="username"]')
    password = driver.find_element_by_xpath('//*[@id="password"]')
    username.clear()
    username.send_keys(imgur_username)
    password.send_keys(imgur_password)
    driver.find_element_by_name("allow").click()

    timeout = 5
    try:
        element_present = EC.presence_of_element_located((By.ID, 'pin'))
        WebDriverWait(driver, timeout).until(element_present)
        pin_element = driver.find_element_by_id('pin')
        pin = pin_element.get_attribute("value")
    except TimeoutException:
        print("Timed Out ")

    driver.close()
    print(pin)
    
    credentials = client.authorize(pin, 'pin')
    client.set_user_auth(credentials['access_token'], credentials['refresh_token'])
    print('authentication successfull')        
    return client   


if __name__=="__main__":
    auth()
