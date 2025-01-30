from pytest_bdd import scenarios, given, step, parsers
import time
from utils.selenium_driver import locator_type
import pdb


scenarios("/home/ace/Documents/bdd-demo-pytest/bdd_demo/features")


@step(parsers.parse('I open the url "{variable}" in the tab'))
def open_url_on_tab(browser, variable):
    pdb.set_trace()
    print(dir(browser))
    browser.get(variable)


@step(parsers.parse('I launch the given "{browser_type}" browser')) 
def launch_given_browser(browser_type):
    print("browser_type", browser_type)


@step(parsers.parse('I enter the "{value}" having "{locator_type}"="{locator_value}"'))
def enter_value_in_given_locator(browser, value, locator_type, locator_value):
    locator = locator_type(locator_type)
    browser.find_element(locator, locator_value).send_keys(value)


@step(parsers.parse('I click on the "{logical_name}" having "{locator_type}"="{locator_value}"'))
def click_on_given_locator(browser, logical_name, locator_type, locator_value):
    locator = locator_type(locator_type)
    browser.find_element(locator, locator_value).click()


@step(parsers.parse('I wait for "{duration:d}" seconds'))
def wait_for_given_seconds(duration):
    time.sleep(duration)


@step(parsers.parse('I make sure that "{object_name}" is "{object_property}" on page having "{locator_type}"="{locator_value}"'))
def make_sure_element_on_given_locator(browser, object_name, object_property, locator_type, locator_value):
    locator = locator_type(locator_type)
    _element = browser.find_element(locator, locator_value)
    assert _element.is_visible == True, "Not able to see it"
