from behave import *
from selenium.webdriver.common.by import By

@given(u'I am on the homepage')
def step_impl(context):
    context.browser.get("https://www.saucedemo.com/")
    assert(context.browser.title) == "Swag Labs"


@when(u'I fill my credential')
def step_impl(context):
    context.browser.find_element(By.ID,"user-name").send_keys("standard_user")
    context.browser.find_element(By.ID,"password").send_keys("secret_sauce")
    context.browser.find_element(By.ID, "login-button").click()


@then(u'I should be logged in')
def step_impl(context):
    assert(context.browser.find_element(By.ID,"item_4_title_link").text) == "Sauce Labs Backpack"
    

@when(u'I fill wrong email')
def step_impl(context):
    context.browser.find_element(By.ID,"user-name").send_keys("standard_userrr")
    context.browser.find_element(By.ID,"password").send_keys("secret_sauce")
    context.browser.find_element(By.ID, "login-button").click()


@then(u'I should not be logged in')
def step_impl(context):
    assert(context.browser.title) == "Swag Labs"


@then(u'I should see the error message')
def step_impl(context):
      assert(context.browser.find_element(By.XPATH,"//h3[@data-test='error']").text) == "Epic sadface: Username and password do not match any user in this service"
