from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

MAX_WAIT = 10


class NewVisitorTest(LiveServerTestCase):
    '''
        Tests modeled after 'Test Driven Development with Python'
    '''

    def setUp(self):
        self.browser = webdriver.Firefox(
            executable_path="D:\\Users\\rwolfsla\\Desktop\\software\\geckodriver.exe"
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

        # Agent notices menu bar as 'Brand', 'Home', 'Admin'
        brand = self.browser.find_element(By.XPATH,
                                          '//div[@class="navbar-header"]/a')

        # make sure the brand is in navbar-brand
        brand_attrib = brand.get_attribute("class")
        self.assertEqual(brand_attrib, 'navbar-brand')
        self.assertEqual(brand.text, 'AV Database')

        homeadmin = self.browser.find_elements_by_xpath(
            '//ul[@class="nav navbar-nav"]/li')
        home = homeadmin[0]
        admin = homeadmin[1]
        self.assertEqual(home.text, 'Home')
        self.assertEqual(admin.text, 'Admin')

        # Agent notices H1
        h1 = self.browser.find_element(By.XPATH, '//h1')
        self.assertEqual(h1.text, 'Audio Visual Data')

        # Agent notices search boxes (adjust for number of facets)
        self.fail('Set up tables')

        # Agent notices notices table populated with data

        # Agent notices an export button

    def test_API_endpoints(self):
        '''
            Make sure API enpoints are correct
        '''
        # agent accesses API and ensures it can be filled out
        self.browser.get(self.live_server_url+'/api')

        # find field titles and fill in.
        count = 0
        for x in range(13):
            count += 1
            xpath_field = f'/html/body/div/div[2]/div/div[3]/div/div[1]/form/fieldset/div[{str(count)}]/div/input'
            xpath_title = f'/html/body/div/div[2]/div/div[3]/div/div[1]/form/fieldset/div[{str(count)}]/label'

            found_title = self.browser.find_element(By.XPATH, xpath_title)
            self.browser.find_element(
                By.XPATH, xpath_field).send_keys(found_title.text)


        submit = '/html/body/div/div[2]/div/div[3]/div/div[1]/form/fieldset/div[14]/button'
        self.browser.find_element(By.XPATH,
                                  submit).click()

        # agent navigates to json data
        self.browser.find_element(By.XPATH,
                                  '/html/body/div/div[2]/div/div[1]/form[1]/fieldset/div/button').click()
        self.browser.find_element(By.XPATH,
                                  '/html/body/div[1]/div[2]/div/div[1]/form[1]/fieldset/div/ul/li[1]/a').click()

        # confirms page properly redirects
        self.assertEqual(self.browser.current_url.split('/api/')[1],
                         '?format=json')
