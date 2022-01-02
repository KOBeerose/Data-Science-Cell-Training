from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = webdriver.ChromeOptions()

prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("start-maximized")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="C:\\Users\\taha_\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.get("https://www.facebook.com/")

mail = driver.find_element_by_name("email")
mail.send_keys("tahaelghabi@gmail.com")

passwrd = driver.find_element_by_name("pass")
passwrd.send_keys("emmm")


log = driver.find_element_by_name("login")
log.click()

time.sleep(.5)


driver.get("http://facebook.com/profile.php")

time.sleep(.5)

'''l2= driver.find_element_by_xpath("//div[@class='sej5wr8e']")
driver.execute_script("arguments[0].scrollIntoView(true);", l2)
time.sleep(0.5)

button = driver.find_element_by_xpath("//div[@class='rq0escxv l9j0dhe7 du4w35lb j83agx80 pfnyh3mw i1fnvgqd gs1a9yip owycx6da btwxx1t3']")
button.click()'''

driver.get(driver.current_url+"friends")


# driver.quit()