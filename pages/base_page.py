


class BasePage():
	def __init__(self, driver, url):
		self.driver = driver
		self.url = url

	def go_to(self):
		self.driver.get(self.url)