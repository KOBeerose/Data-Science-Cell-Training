from selenium import webdriver


chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(executable_path = "C:\\Users\\taha_\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.get("https://www.facebook.com/")


email_field = driver.find_element_by_id("email")
email_field.send_keys("test@gmail.com")

pass_field = driver.find_element_by_id("pass")
pass_field.send_keys("test@gmail.com")

button = driver.find_element_by_name("login")
button.click()


