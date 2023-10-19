from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.chrome.options import Options as ChromeOptions
import time
import pytest

link1 = "https://casenik.com.ua/"


@pytest.fixture(autouse=True)
def all_print():
    print("Autouse print")

class TestPage1():
    @pytest.mark.casenik
    def test_number1(self, browser):
        browser.get(link1)
        view_all = browser.find_element(By.CLASS_NAME, "view-all")
        view_all.click()
        print("Show page all new products")
        wait = WebDriverWait(browser, 100)
        time.sleep(10)
        prod = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[@href='product/gidrogelevaya-broneplenka-plenka-smartex-xiaomi-redmi-go']")))
        prod.click()

    @pytest.mark.mathe
    def test_number2_asert(self):
        result = 5 + 7
        expected_result = 12
        assert result == expected_result, f"Result ({result}) does not correspond ({expected_result})"

    @pytest.mark.casenik
    def test_number3(self, browser):
        browser.get(link1)
        element = browser.find_element(By.XPATH, "//a[@href='main/showSale' and contains(@class, 'check-sale')]")
        element.click()

    @pytest.mark.casenik
    def test_number4(self, browser):
        browser.get(link1)
        time.sleep(10)
        link = browser.find_element(By.XPATH, "//div[@class='top_bar_user']")
        link.click()

    @pytest.mark.mathe
    def test_number5_asert(self):
        result = 12 - 10
        expected_result = 2
        assert result == expected_result, f"Result ({result}) does not correspond ({expected_result})"









