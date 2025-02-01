from pytest_bdd import scenarios, given, step, parsers
import time
import os
from utils.selenium_driver import locator_type
import pdb

FEATURES_PATH = os.path.join(os.path.dirname(__file__), 'features')

# Path for All feature file scenarios
scenarios(FEATURES_PATH)


@step(parsers.parse('I open the url "{variable}" in the tab'))
def open_url_on_tab(driver, variable):
    driver.get(variable)


@step(parsers.parse('I launch the given "{browser_type}" browser')) 
def launch_given_browser(browser_type):
    print("browser_type", browser_type)


@step(parsers.parse('I enter value "{value}" in "{name}" having "{locator}"="{locator_value}"'))
def enter_value_in_given_locator(driver, 
                                 value, 
                                 name, 
                                 locator, 
                                 locator_value):
    web_locator = locator_type(locator)
    driver.find_element(web_locator, locator_value).send_keys(value)


@step(parsers.parse('I click on the "{name}" having "{locator}"="{value}"'))
def click_on_given_locator(driver, 
                           name, 
                           locator, 
                           value):
    web_locator = locator_type(locator)
    driver.find_element(web_locator, value).click()


@step(parsers.parse('I wait for "{duration:d}" seconds'))
def wait_for_given_seconds(duration):
    time.sleep(duration)


@step(parsers.parse('I make sure that "{name}" is "{attribue}" on "{location}" having "{locator}"="{value}"'))
def make_sure_element_on_given_locator(driver, 
                                       name, 
                                       attribue, 
                                       location, 
                                       locator, 
                                       value):
    web_locator = locator_type(locator)
    _element = driver.find_element(web_locator, value)
    assert _element.is_displayed() == True, "Not able to see it"
