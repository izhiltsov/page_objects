
from pages.main_page import MainPage
from pages.login_page import LoginPage


url = 'http://selenium1py.pythonanywhere.com/'
login_page = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'



def test_guest_can_go_to_login_page(browser):

	page = MainPage(browser, url)
	page.go_to()
	page.go_to_login_page()
	log_page = LoginPage(browser, login_page)
	log_page.should_be_login_page()
	

def test_guest_should_see_login_link(browser):

    page = MainPage(browser, url)
    page.go_to()
    page.should_be_login_link()




