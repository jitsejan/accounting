from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Safari()
driver.get("https://global.americanexpress.com/activity/range?from=2020-01-01&to=2021-12-31")