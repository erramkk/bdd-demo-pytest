import pytest
from utils.selenium_driver import Driver
from pdb import set_trace


@pytest.fixture
def driver():
	browser = Driver().get_browser("firefox")
	yield browser
	browser.close()

