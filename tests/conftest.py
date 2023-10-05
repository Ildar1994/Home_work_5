import pytest
from selene import browser

@pytest.fixture(scope='function', autouse='True')
def browser_managment():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_height = '1200'
    browser.config.window_width = '1800'
    yield
    browser.quit()
