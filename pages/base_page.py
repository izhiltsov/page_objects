from selenium.common.exceptions import NoSuchElementException


class BasePage():
	def __init__(self, driver, url):
		self.driver = driver
		self.url = url

	def go_to(self):
		self.driver.get(self.url)

	def is_element_present(self, how, what):
	    try:
	        self.driver.find_element(how, what)
	    except NoSuchElementException:
	        return False
	    return True

	def get_current_url(self):
		current_url = self.driver.current_url
		return current_url
