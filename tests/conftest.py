import json
import pytest
from selenium import webdriver


@pytest.fixture
def config():
	# Read the file
	with open('config.json') as f:
		config = json.load(f)

	# Assert values are acceptable
	assert config['browser'] in ['firefox', 'safari', 'chrome']
	assert isinstance(config['implicit_wait'], int)
	assert config['implicit_wait'] > 0

	# Return config so it can be used
	return config




#@pytest.fixture(params=[webdriver.Chrome, webdriver.Safari, webdriver.Firefox], ids=['Chrome', 'Safari', 'Firefox'])
@pytest.fixture(params=[webdriver.Chrome], ids=['Chrome'])
def browser(request):
	driver = request.param
	driver = driver()
	driver.implicitly_wait(5)
	yield driver
	driver.quit()