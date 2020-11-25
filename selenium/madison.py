import unittest
from selenium import webdriver

class Hello(unittest.TestCase):
    ## Iniciamos
    @classmethod # Decorador para que las distintas paginas corran en una sola pestaña
    def setUpClass(cls):
        # cls.driver = webdriver.Chrome(executable_path=r"./chromedriver.exe")
        cls.driver = webdriver.Edge(executable_path=r"./msedgedriver.exe")
        driver = cls.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(20)

    ## Trabajamos
    def test_search_id(self):
        driver = self.driver
        search_field = driver.find_element_by_id('search')

    def test_search_name(self):
        search_field = self.driver.find_element_by_name('q')

    def test_search_class(self):
        search_field = self.driver.find_element_by_class_name('input-text')

    def test_search_button(self):
        search_field = self.driver.find_element_by_class_name('search-button')

    def test_count_images_banner(self):
        banner_list = self.driver.find_element_by_class_name('promos')
        banners = banner_list.find_element_by_tag_name('img')
        # print('----- TYPE -----',type(banners))
        self.assertEqual(3, len(banners))

    def test_xpath(self):
        promo = self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[4]/a/img')

    def test_css(self):
        css = self.driver.find_element_by_css_selector('div.header-minicart span.icon')

    ## Finalizamos
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
