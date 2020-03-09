from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

#Assign the "--headless" value to the "chrome_options" that were declared at the beginning, give a path of chromedriver
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="/home/sb/chromedriverlinux/chromedriver")
driver.implicitly_wait(5) #Wait for the element detection on the page

#Open the url
driver.get('https://google.com')
print(driver.title, 'website is launched') #result of running so we could see it in the terminal

driver.find_element_by_name('q').send_keys('I love Python')
print('Keys are sent')

driver.find_element_by_name('btnK').click()
print('Button clicked')

driver.close()
driver.quit()
print('Mission Accomplished!')
