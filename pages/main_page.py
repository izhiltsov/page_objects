from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class MainPage(BasePage): 

	def go_to_login_page(self):
		element = self.driver.find_element(By.CSS_SELECTOR, '#login_link')
		element.click()

	def should_be_login_link(self):
		assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"

