from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user_name = "YOUR EMAILED"
password = "YOUR PASSWORD"
driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
element = driver.find_element("Email")
element.send_keys(user_name)
element = driver.find_element("password")
element.send_keys(password)
element.send_keys(Keys.RETURN)
element.clear()