from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from datetime import datetime
from tkinter import filedialog
import pygetwindow
import win32gui
import win32ui
from ctypes import windll
from PIL import Image


titles = pygetwindow.getAllTitles()
print(titles) #select the window name from here

image_number = 0
exit_code = True
email = "ritik_srivastava.scsebtech@galgotiasuniversity.edu.in"
Password = "Anumymoon@0509"
url = "https://youtu.be/FHSrEThvtZs"
window_name = "(69) Inaugural Session: Two days National Seminar on NEP 2020: A Gateway to Academic Excellence - YouTube - Google Chrome"

def take_background_ss():
    global image_number, window_name
    hwnd = win32gui.FindWindow(None, window_name)
    # Change the line below depending on whether you want the whole window
    # or just the client area. 
    #left, top, right, bot = win32gui.GetClientRect(hwnd)
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    w = right - left
    h = bot - top

    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

    saveDC.SelectObject(saveBitMap)

    # Change the line below depending on whether you want the whole window
    # or just the client area. 
    #result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 1)
    result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)
    print(result)

    bmpinfo = saveBitMap.GetInfo()
    print(bmpinfo)
    bmpstr = saveBitMap.GetBitmapBits(True)

    im = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)

    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)
    if result == 1:
        #PrintWindow Succeeded
        im.save("./screenshots/screenshot" + str(image_number) + ".png")
        image_number += 1

def automation():
    '''Open the browser -> sign-in to google account through stackoverflow -> redirect to youtube live stream -> take a screenshot -> return'''
    global email
    global Password
    global url
    global exit_code 
    
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
        account = driver.find_element_by_id("avatar-btn")
        print('Iam here')
        account.click()
        time.sleep(2)
        take_background_ss()
    finally:
        driver.quit()
    return

if __name__ == "__main__":
    while(exit_code):
        automation()
        time.sleep(10)
