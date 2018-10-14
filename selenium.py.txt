from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
username=""
password=""
browser.get('https://github.com/')

#elem = browser.find_element_by_xpath('html/body/div/div[3]/form/div[2]/div[2]/div[1]/div[1]/div[2]/div')  # Find the search box
elem = browser.find_element_by_link_text("Sign in")
elem.click()
elem = browser.find_element_by_id("login_field")
username = input("username - ")
password = input("password - "
elem.send_keys(username)
elem = browser.find_element_by_id("password")
elem.send_keys(password + Keys.RETURN)

browser.implicitly_wait(2)
elem = browser.find_element_by_name("q")
#elem = browser.find_element_by_xpath('//input[@name="q"]')
#elem = browser.find_element_by_css_selector('input.form-control.header-search-input.js-search-site-focus')
#driver.findElement(By.xpath("//input[@id='invoice_supplier_id'])).setAttribute("value", "your value")

elem.send_keys('seleniumhq' + Keys.RETURN)

browser.close()

#browser.quit()"//input[@name='username']"
