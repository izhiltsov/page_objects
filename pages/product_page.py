import math

from selenium.common.exceptions import NoAlertPresentException 

from pages.base_page import BasePage
from pages.locators import ProductPageLocators



class ProductPage(BasePage):
	"""docstring for ProductPage"""
	def add_to_cart(self):
		button = self.driver.find_element(*ProductPageLocators.ADD_TO_CART)
		button.click()


	def solve_quiz_and_get_code(self):
	    alert = self.driver.switch_to.alert
	    x = alert.text.split(" ")[2]
	    answer = str(math.log(abs((12 * math.sin(float(x))))))
	    alert.send_keys(answer)
	    alert.accept()
	    try:
	        alert = self.driver.switch_to.alert
	        alert_text = alert.text
	        print(f"Your code: {alert_text}")
	        alert.accept()
	    except NoAlertPresentException:
	        print("No second alert presented")
