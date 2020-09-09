from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

#Declare required conditions for testing:
firefox_options = Options()
firefox_options.add_argument('--headless')

#Assign the '--headless' value to the 'firefox-options' that were declared at the beginning, give a path to the geckodriver:
driver = webdriver.Firefox(executable_path="/home/sb/geckodriver", firefox_options=firefox_options)
driver.implicitly_wait(5) #Wait for the element detection on the page

#Open the target url:
driver.get("https://google.com")
print(driver.title, 'website is launched')

#Find the field and type the text to find:
input = driver.find_element_by_name('q')
input.send_keys('SELENIUM PYTHON IS COOL')
print('Keys are sent')

#Click button to start the search:
input.send_keys(Keys.ENTER)
print('Button is clicked on the keyboard')

#Close the browser and stop driver's work:
driver.close()
driver.quit()
print('Misson accomplished')
