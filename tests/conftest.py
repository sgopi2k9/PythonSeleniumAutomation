import pytest
from base.webdriverfactory import WebDriverFactory

@pytest.fixture(scope = "class")
def oneTimeSetUp(request, browser):
    baseURL = 'https://learn.letskodeit.com/p/practice'
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    driver.get(baseURL)
    driver.maximize_window()
    driver.implicitly_wait(5)

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

