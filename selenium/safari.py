from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


user_name = "0545296962"
password = "4545801"
driver = webdriver.Safari()
driver.get('https://www.facebook.com/login')
element = driver.find_element(By.ID, "email")
element.send_keys(user_name)
element = driver.find_element(By.ID, "pass")
element.send_keys(password)
element.send_keys(Keys.RETURN)
element.close()