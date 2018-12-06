from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):
    '''
        Tests modeled after 'Test Driven Development with Python'
    '''

    def setUp(self):
        self.browser = webdriver.Firefox(
            executable_path = "D:\\Users\\rwolfsla\\Desktop\\software\\geckodriver.exe"
        )

    def tearDown(self):
        self.browser.quit()


    def test_if_homepage_starts_and_has_content(self):
        '''
            Test in automated browser if homepage boots up, and
            has desired content
        '''
        # Agent navigates to home page and notices a menu bar
        self.browser.get(self.live_server_url)
        self.fail('Browser loaded, next up menu bar')

        # Agent notices menu bar as 'Brand', 'Home', 'Admin'

        # Agent notices H1

        # Agent notices search boxes (adjust for number of facets)

        # Agent notices notices table populated with data

        # Agent notices an export button
