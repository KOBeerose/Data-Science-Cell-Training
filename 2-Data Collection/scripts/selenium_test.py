#importing all the necessary libaries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import string

url = email = password = ''
# defining the webdriver and config btw this code will be almost the same in all of your selenium scripts
chrome_options = webdriver.ChromeOptions()

# !!! blocking browser notifications !!!
prefs = {"profile.default_content_setting_values.notifications" : 2} 
chrome_options.add_experimental_option("prefs", prefs)

# starting in maximized window
chrome_options.add_argument("start-maximized")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="C:\\Users\\taha_\\Downloads\\chromedriver_win32\\chromedriver.exe")


# this function gets the user info and save them in variables
def get_info(filename): 
    elem_list=["url","email","password"]   # list of expressions preceding the user info
    with open(filename, 'r') as read_obj: 
            for line in read_obj:
                for elem in elem_list:  # Get the value after an expression occurrence
                    if elem in line:
                        # save the value in a variable named according to the expression preceding it
                        globals()[elem] = line.partition(elem+": ")[2].translate({ord(c): None for c in string.whitespace})   

# getting values of the user information
get_info("C:\\Users\\taha_\\OneDrive - ine.inpt.ma\\Coding\\Data Science\\Data-Science-Cell-Training\\Data Collection\\scripts\\Information.txt")
print(url, email, password)
driver.get(url)

mail = driver.find_element_by_name("email")
mail.send_keys(email)

passwrd = driver.find_element_by_name("pass")
passwrd.send_keys(password)


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

# Complete the follwing script to get data about your facebook friends
# driver.quit()