from selenium import webdriver       
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

#Assign the "--headless" value to the "chrome_options" that were declared at the beginning, give a path of chromedriver
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="/home/sb/chromedriverlinux/chromedriver")

#Open the url
driver.get('https://google.com')
print(driver.title, 'website is launched') #result of running so we could see it in the terminal
time.sleep(5) #Give it a while to download fully

driver.find_element_by_name('q').send_keys('I love Python')
print('Keys are sent')
time.sleep(5)

driver.find_element_by_name('btnK').click()
print('Button clicked')
time.sleep(5)

driver.close()
driver.quit()
print('Mission Accomplished!')
