import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class Hello(unittest.TestCase):
    ## Iniciamos
    @classmethod # Decorador para que las distintas paginas corran en una sola pestaña
    def setUpClass(cls):
        # cls.driver = webdriver.Chrome(executable_path=r"./chromedriver.exe")
        cls.driver = webdriver.Edge(executable_path=r"./msedgedriver.exe")
        driver = cls.driver
        driver.implicitly_wait(10) ## espera 10 segundos

    ## Trabajamos
    def test_hello(self):
        driver = self.driver
        driver.get('https://www.google.com')

    def test_wikipedia(self):
        self.driver.get('https://www.wikipedia.org')

    ## Finalizamos
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reports', report_name='report_hello'))
