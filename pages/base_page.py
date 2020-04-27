from selenium.common.exceptions import NoSuchElementException
from pages.locators import BasePageLocators


class BasePage():
	def __init__(self, driver, url):
		self.driver = driver
		self.url = url

	def open(self):
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

	def go_to_login_page(self):
		link = self.driver.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
		link.click()

	def should_be_login_link(self):
		assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
