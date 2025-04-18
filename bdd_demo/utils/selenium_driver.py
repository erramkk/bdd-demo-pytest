from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.chrome.service import Service as chromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeType
from selenium.webdriver.firefox.service import Service as firefoxService
from selenium.webdriver.firefox.options import Options as firefox_options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


class Driver:
	""" docstring for ClassName """

	def get_browser(self, browser_type):

		if browser_type.lower() == "chrome":
			options = chrome_options()
			options.add_argument("--disable-dev-shm-using") 
			options.add_argument("--headless=new")
			driver = webdriver.Chrome(
				service=chromeService(ChromeDriverManager().install()),
				options=options
				)
		elif browser_type.lower() == "firefox":
			options = firefox_options()
			# firefox_profile = FirefoxProfile()
			# firefox_profile.set_preference("javascript.enabled", False)
			# options.profile = firefox_profile
			driver = webdriver.Firefox(
				# service=firefoxService(GeckoDriverManager().install()),
				service=firefoxService(executable_path='/snap/bin/firefox.geckodriver'),
				options=options,
				)
		else:
			driver = webdriver.Chrome()

		return driver


def locator_type(loc_type):
	if loc_type.lower() == "xpath":
		return By.XPATH
	elif loc_type.lower() == "css":
		return By.CSS_SELECTOR
	else:
		return By.XPATH
