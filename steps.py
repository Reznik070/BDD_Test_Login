from behave import *

from time import sleep

@given('user is on homepage')
def step_homepage(context):
    context.driver.get("http://automationpractice.com/index.php")

@when('login_link is clicked')
def step_impl(context):
     context.driver.find_element_by_xpath("//*[@id='header']/div[2]/div/div/nav/div[1]/a").click()
     sleep(3)


@when('email is entered')
def step_impl(context):
    emil = context.driver.find_element_by_css_selector("#email")
    emil.send_keys("akemzo07@hotmail.com")

@when('password is entered')
def step_impl(context):
    password = context.driver.find_element_by_css_selector("#passwd")
    password.send_keys("rocker07")
    sleep(2)

@when('login_button is clicked')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='SubmitLogin']").click()


@then('user is logged_in')
def step_impl(context):
    current_page = context.driver.page_source

    if "MY ACCOUNT" in current_page:
        print("User logged in successfully")
    else:
        print("Login failed")

    sleep(6)

