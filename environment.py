from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def before_all(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(20)

def after_all(context):
    context.driver.quit()