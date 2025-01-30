from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.chrome.service import Service as chromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeType
from selenium.webdriver.common.by import By


class Driver:
	""" docstring for ClassName """

	def get_browser(self, browser_type):

		if browser_type.lower() == "chrome":
			options = chrome_options()
			options.add_argument("--disable-dev-shm-using") 
			# options.add_argument("--remote-debugging-port=9222")
			driver = webdriver.Chrome(
				service=chromeService(ChromeDriverManager().install()),
				options=options)
		elif browser_type.lower() == "firefox":
			driver = webdriver.Firefox()
		else:
			driver = webdriver.Chrome()

		return driver


def locator_type(locator_type):
	if locator_type.lower() == "xpath":
		return By.XPATH
	elif locator_type.lower() == "css":
		return By.CSS_SELECTOR
	else:
		return By.XPATH
