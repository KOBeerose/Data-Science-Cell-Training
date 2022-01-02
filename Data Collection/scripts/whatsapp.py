#importing all the necessary libaries
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains




import time

browser = webdriver.Chrome(executable_path="C:\\Users\\taha_\\Downloads\\chromedriver_win32\\chromedriver.exe")
browser.get('https://web.whatsapp.com/')
wait = WebDriverWait(browser, 2000)


target = '"Test"' #group name 
message = "Hello! this is an automated test using selenium" #target msg
working = True
recieved = {'You'}
target_names = set()

def get_grp_menu(target):
    x_arg = ' //span[contains(@title, ' + target +')]'
    target = wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
    target.click()
    menu = browser.find_element_by_xpath("//div[@class='_1QVfy _3UaCz']//div//div[@class='_2cNrC']//div[@class='_26lC3']//span")
    menu.click()
    time.sleep(.5)
    group_inof = browser.find_element_by_xpath("//div[contains(text(),'Group info')]")
    group_inof.click()




def send_msg():
    global working
    global target_names
    JS_ADD_TEXT_TO_INPUT = """
    var elm = arguments[0], name = arguments[1];
    string = "";
    hel = "Hello " + name + "! Here is the takeaway 🗒️ of the last 2 sessions";
    text = [ hel, " " , " " , " -There are different ways to get Data. but the internet 🌐 is the best place." , " - 🕸 Web Scraping is used to acquire Data with libraries like " , "  { " , "   scrapy : [ Fast ,  Hard ,  used in big projects ]  , " , "    beautifulsoup : [ Not fast ,  Easy ,  used in personal projects ]  ,  " , "    selenium : [ Not fast ,  Medium ,  Used for automation] " , "  } " , " -Often in Scraping it is better to use a 🐍 script in 🆚code than jupyter especially if you wanna get Tabnine extension autocomplete 🎩 magic." , " -WTF Pandas 😵 can scrap Data from websites make it a Dataframe!! Hell yeah 🐼 I can " , " -BTW! Dont forget to put your Data in a CSV file!" , " " , "PS: This msg was automatically sent using selenium 😅"];
    for (let i = 0; i < text.length; i++) {
        string += text[i]+"\n";
    };

    elm.value += string;
    elm.dispatchEvent(new Event('change'));
    """
    text = "🌎 🌊 " + u'\u2764'
    i = 0
    while working:
        targets = browser.find_elements_by_xpath("//div[@class='tt8xd2xn dl6j7rsh mpdn4nr2 avk8rzj1']//div//div[@class='_3uIPm WYyr1']//span[@class='ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr']")
        if i == 0 : target_names = set(map(lambda x: x.text ,  targets))
        
        item = targets[i]
        if item.text not in recieved and item.text!= "You":
            name = item.text
            print(name)
            item.click()
            time.sleep(1)

            # Emoji Character
            text = [ "Hello "+name+ "! Here is the takeaway :docu", u'\ue007'," of the last 2 sessions:",
"break",
"break",
" ~ There are different ways to get Data. but the internet :internet", u'\ue007'," is the best place.",
"break",
" ~ :web", u'\ue007' ," Web Scraping is used to acquire Data with libraries like:",
"break",
"  { ",
"break",
"   scrapy : [ Fast, Hard, used in big projects ] ,",
"break",
"    beautifulsoup : [ Not fast, Easy, used in personal projects ] , ",
"break",
"    selenium : [ Not fast, Medium, Used for automation] ",
"break",
"  } ",
"break",
" ~ Often in Scraping it is better to use a :snake", u'\ue007'," script in :vs", u'\ue007'," code than jupyter especially if you wanna get Tabnine extension autocomplete :magici", u'\ue007'," magic.",
"break",
" ~ WTF Pandas :mind", u'\ue007'," can scrap Data from websites make it a Dataframe!! Hell yeah :panda", u'\ue007'," I can ",
"break",
" ~ BTW! Dont forget to put your Data in a CSV file!",
"break",
"break",
"PS: This msg was automatically sent using selenium :sw", u'\ue007']

            """

            for string in text:
                browser.execute_script("arguments[0].innerHTML = '{}'".format(string),name,input_box)
                input_box .send_keys('.')
                input_box .send_keys(Keys.BACKSPACE)
                time.sleep(0.2)
            """

            input_box = browser.find_element_by_xpath("//div[@title = 'Type a message']")
            counter = 0
            for string in text:
                if string == "break":
                    ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).perform()
                    
                else :
                    time.sleep(0.2)
                    input_box.send_keys(string)
                time.sleep(0.5)
            #input_box.send_keys(':emoji' u'\ue007')
            time.sleep(0.5)
            # browser.execute_script(JS_ADD_TEXT_TO_INPUT, input_box, name)
            #input_box .send_keys(Keys.ENTER)

            i+=1
            recieved.add(name)
            print("this is recieved", recieved)
            print("this is target_names thou",target_names)
            if recieved == target_names:
                working = False
                break
            get_grp_menu(target)
            time.sleep(1)
            print(targets)
            print(item)
            '''        for item in targets:
            if item not in recieved:
                name = item.text
                print(name)
                item.click()
                input_box = browser.find_element_by_xpath("//div[@title = 'Type a message']")
                # input_box.send_keys(message + Keys.ENTER)
                break'''
            



get_grp_menu(target)
while bool:
    time.sleep(.5)
    send_msg()
    #browser.close()
    break


# targets = browser.find_elements_by_xpath("//div[@class='tt8xd2xn dl6j7rsh mpdn4nr2 avk8rzj1']//div//div[@class='_3uIPm WYyr1']")
# input_box = browser.find_element_by_class_name('_13NKt copyable-text selectable-text')


'''
for target in targets:#loops runs for 100 times
    print(target)
    x_arg = ' //span[contains(@title, ' + target +')]'
    target = wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
    target.click()
    input_box = browser.find_element_by_xpath("//div[@title = 'Type a message']")
    input_box.send_keys(string + Keys.ENTER)'''