# -*- coding: utf-8 -*- 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

address = """https://codeup.kr/""" #codeup site

caps = DesiredCapabilities.CHROME
caps['loggingPrefs'] = {'performance':'OFF'}
chrome_options = Options()
chrome_options.add_argument('--log-level=3')
chrome_options.add_argument('--disable-logging')
chrome_options.add_experimental_option('w3c', False)
#option setting

driver = webdriver.Chrome(desired_capabilities=caps, options=chrome_options) #driver setting

sleepTime = 2
try:
    driver.get(address)
    driver.find_element_by_xpath("""//*[@id="navbarNavDropdown"]/ul[2]/li[2]/a""").click()
    driver.find_element_by_xpath("""/html/body/div[2]/form/div[1]/input""").send_keys(input("codeup id ==> "))
    driver.find_element_by_xpath("""/html/body/div[2]/form/div[2]/input""").send_keys(input("codeup pw ==> "))

    driver.find_element_by_xpath("""/html/body/div[2]/form/input""").click()
    
    questionNum = int(input("Question Num ==> "))
    driver.execute_script('window.open("https://codeup.kr/submitpage.php?id={0}");'.format(questionNum))
        
    driver.switch_to_window(driver.window_handles[0])
    while questionNum < 1100:
        driver.get("""https://codeup.kr/problem.php?id={0}""".format(questionNum))
        driver.switch_to_window(driver.window_handles[1])
        driver.get("""https://codeup.kr/submitpage.php?id={0}""".format(questionNum))

        driver.switch_to_window(driver.window_handles[0])
        input()
        questionNum += 1

    
except Exception as e:
    print(e)
finally:
    driver.quit()

