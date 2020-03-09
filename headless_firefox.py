from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

firefox_options = Options() #Assign the options for the webdriver.FirefoxOptions
firefox_options.add_argument('--headless') #Declare running test with option of 'headless' browser
driver = webdriver.Firefox(executable_path="/home/sb/geckodriver", firefox_options=firefox_options) #Geckodriver path
driver.implicitly_wait(5) #Wait for the element detection on the page

driver.get("https://google.com")
print(driver.title, 'website is launched')

input = driver.find_element_by_name('q')
input.send_keys('SELENIUM PYTHON IS COOL')
print('Keys are sent')

input.send_keys(Keys.ENTER)
print('Button is clicked on the keyboard')

driver.close()
driver.quit()

print('Misson accomplished')
