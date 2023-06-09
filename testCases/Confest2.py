from selenium import webdriver
import pytest
@pytest.fixture()
def setup(browser):
    if browser == "msedgedriver":
        driver = webdriver.Edge(
            executable_path=r"C:\Users\Asus\PycharmProjects\pythonProject2\Drivers\edgedriver_win64\msedgedriver.exe")
        print("Launching Edge Browser............")
    elif browser == "Firefox":
        driver = webdriver.Firefox(r"C:\Users\Asus\PycharmProjects\pythonProject2\Drivers\edgedriver_win64\msedgedriver.exe")
        print("Launching Firefox Browser............")
        return driver
def pytest_addoption(parser):    # This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")