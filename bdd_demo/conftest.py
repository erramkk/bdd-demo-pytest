import pytest
from utils.selenium_driver import Driver
from pdb import set_trace


@pytest.fixture
def browser():
	driver = Driver().get_browser("chrome")
	set_trace()
	yield driver
	driver.close()

