from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class MainPage(BasePage): 

	def go_to_login_page(self):
		login_element = self.driver.find_element(By.CSS_SELECTOR, '#login_link')
		login_element.click()