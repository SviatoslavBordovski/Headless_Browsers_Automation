from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

#Declare the required conditions for testing:
chrome_options = Options()
chrome_options.add_argument("--headless")

#Assign the '--headless' value to the 'chrome_options' that were declared at the beginning, give a path to the chromedriver:
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="/home/sb/chromedriverlinux/chromedriver")
driver.implicitly_wait(5) #wait for the element detection on the page

#Open the target url:
driver.get('https://google.com')
print(driver.title, 'website is launched') #result of running so we could see it in the terminal

#Find the field and type the text to find:
driver.find_element_by_name('q').send_keys('Python is a programming language')
print('Keys are sent')

#Click to start the search:
driver.find_element_by_name('btnK').click()
print('Button clicked')

#Close the browser and stop driver's work:
driver.close()
driver.quit()
print('Mission Accomplished!')
