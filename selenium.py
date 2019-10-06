from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
username = ""
password = ""
browser.get('https://github.com/')

elem = browser.find_element_by_link_text("Sign in")
elem.click()
elem = browser.find_element_by_id("login_field")
elem.send_keys(username)
elem = browser.find_element_by_id("password")
elem.send_keys(password + Keys.RETURN)

browser.implicitly_wait(2)
elem = browser.find_element_by_name("q")
elem.send_keys('hponeview' + Keys.ENTER)

browser.quit()
