from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui


titles = pygetwindow.getAllTitles()
print(titles) #select the window name from here

image_number = 0
exit_code = True
email = 'User email'
Password = "user password"
url = "https://youtu.be/FHSrEThvtZs"
def automation():
    '''Open the browser -> sign-in to google account through stackoverflow -> redirect to youtube live stream -> take a screenshot -> return'''
    global email
    global Password
    global url
    global exit_code
    global image_number
    
    driver = webdriver.Chrome(executable_path = "./chromedriver.exe")
    driver.get("https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent")
    
    signin = driver.find_element_by_class_name("s-btn__google")
    signin.send_keys(Keys.ENTER)
    inputElement = driver.find_element_by_tag_name("input")
    inputElement.send_keys(email)
    inputElement.send_keys(Keys.ENTER)
    time.sleep(2)
    password = driver.find_element_by_class_name("Xb9hP")from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui

image_number = 0
exit_code = True
email = "ritik_srivastava.scsebtech@galgotiasuniversity.edu.in"
Password = "Anumymoon@0509"
url = "https://youtu.be/FHSrEThvtZs"
def automation():
    '''Open the browser -> sign-in to google account through stackoverflow -> redirect to youtube live stream -> take a screenshot -> return'''
    global email
    global Password
    global url
    global exit_code
    global image_number
    
    driver = webdriver.Chrome(executable_path = "./chromedriver.exe")
    driver.get("https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent")
    
    signin = driver.find_element_by_class_name("s-btn__google")
    signin.send_keys(Keys.ENTER)
    inputElement = driver.find_element_by_tag_name("input")
    inputElement.send_keys(email)
    inputElement.send_keys(Keys.ENTER)
    time.sleep(2)
    password = driver.find_element_by_class_name("Xb9hP")
    password = password.find_element_by_tag_name("input")
    password.send_keys(Password)
    password.send_keys(Keys.ENTER)
    time.sleep(3)
    driver.get(url)
    try:
        time.sleep(30)
        driver.implicitly_wait(10)
        account = driver.find_element_by_id("avatar-btn")
        print('Screenshot taken')
        account.click()
        time.sleep(2)
        driver.get_screenshot_as_file(str(image_number)+".png")
        image_number+=1
    finally:
        driver.quit()
    return

if __name__ == "__main__":
    while(exit_code):
        automation()
        time.sleep(15*60)

    password = password.find_element_by_tag_name("input")
    password.send_keys(Password)
    password.send_keys(Keys.ENTER)
    time.sleep(3)
    driver.get(url)
    try:
        time.sleep(30)
        driver.implicitly_wait(10)
        account = driver.find_element_by_id("avatar-btn")
        print('Iam here')
        account.click()
        time.sleep(2)
        driver.get_screenshot_as_file(str(image_number)+".png")
        image_number+=1
    finally:
        driver.quit()
    return

if __name__ == "__main__":
    while(exit_code):
        automation()
        time.sleep(15*60)
