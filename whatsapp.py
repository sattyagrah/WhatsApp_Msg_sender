# Not suitable for incognito mode or private browsing this time
# I recommend login once to the WhatsApp web before using this script
# This script is suitable only for Indian WhatsApp Number yet

from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\Lenovo\Downloads\chromedriver_win32\chromedriver.exe") 
driver.maximize_window()

mobile_number = input("Enter a valid WhatsApp number : ")
mg = input("Write your message here : ")
if (len(mobile_number)>10):
  print("Invalid WhatsApp number! Kindly try again")
else:
  driver.get('https://api.whatsapp.com/send?phone=91' + mobile_number + '&lang=en')
  driver.find_element_by_id("action-button").click()
  time.sleep(5)
  driver.find_element_by_xpath("//a[contains(text(),'use WhatsApp Web')]").click()
  time.sleep(20)

  #This is the time when the user need to scan the QR code of WhatsApp web from their phone.

  driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]").send_keys(mg)
  driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button/span").click()

  time.sleep(2)
  driver.quit()
