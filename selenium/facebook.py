from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome("/Users/dnylgmbr/Desktop/basic_python/selenium/webdrivers/chromedriver")
driver.get('https://www.youtube.com')
driver.find_element(By.XPATH,'//body/ytd-app[1]/div[1]/tp-yt-app-drawer[1]/div[2]/div[1]/div[2]/div[2]/ytd-guide-renderer[1]/div[1]/ytd-guide-section-renderer[1]/div[1]/ytd-guide-entry-renderer[2]/a[1]/tp-yt-paper-item[1]').click()
# element = driver.find_element(By.ID, "pass")
