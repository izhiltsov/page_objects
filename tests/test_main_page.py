
from pages.main_page import MainPage


url = "http://selenium1py.pythonanywhere.com/"



def test_guest_can_go_to_login_page(browser):

	page = MainPage(browser, url)
	page.go_to()
	page.go_to_login_page()
