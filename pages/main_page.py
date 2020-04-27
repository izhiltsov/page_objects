

from pages.base_page import BasePage
from pages.locators import MainPageLocators

class MainPage(BasePage): 

	def go_to_login_page(self):
		element = self.driver.find_element(*MainPageLocators.LOGIN_LINK)
		element.click()

	def should_be_login_link(self):
		assert self.is_element_present(*MainPageLocators.LOGIN_LINK), 'Login link is not presented'

