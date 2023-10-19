from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
import pytest


# визначення параметрів командної строки
def pytest_addoption(parser):
    parser.addoption("--browser-mode", action="store", default="headless", choices=["headless", "gui"],
                     help="Browser mode: headless or gui")
    parser.addoption("--window-size", action="store", default="full", choices=["full", "1366"],
                     help="Browser window size: full or 1366 pixels")

# Фікстура для ініціалізації браузера
@pytest.fixture(scope="function")
def browser(request):
    print("\n start Browser")
    browser_mode = request.config.getoption("--browser-mode")
    window_size = request.config.getoption("--window-size")
    
    if browser_mode == "headless":
        options = ChromeOptions()
        options.add_argument("--headless")

    else:
        options = ChromeOptions()

    if window_size == "full":
        options.add_argument("--start-maximized")
    else:
        options.add_argument(f"--window-size={window_size},1366")
    
    browser = webdriver.Chrome(options=options)
    
    yield browser
    print("\n quit Browser")
    browser.quit()













