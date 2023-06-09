# import selenium.webdriver as webdriver
# from selenium.webdriver.edge.service import Service
from selenium.webdriver import Edge
import pytest

@pytest.fixture()
def setup():
    from selenium import webdriver
    driver = webdriver.Edge(
        executable_path=r"D:\Mayank manual project scrum team 2\edgedriver_win64 (2)\msedgedriver.exe")
    return driver
####################################pytest HTML Reports#########################################
# It is a hook for adding environment info to HTML reports
def pytest_configure(config):
    config._metadata["Project_Name"] = "Nop-Commerce"
    config._metadata["Module_Name"] = "Customers"
    config._metadata["Tester"] = "Mayank"
# It is a hook to delete or modify environment info for html report
# @pytest.mark.optionalhook
# def pytest_metadata(metadat):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)




#     elif browser == "Firefox":
#         firefox_driver_path = webdriver.Firefox(r"C:\Users\Asus\PycharmProjects\pythonProject2\Drivers\edgedriver_win64\msedgedriver.exe")
#         firefox_service = Service(firefox_driver_path)
#         driver = webdriver.Firefox(service=firefox_service)
#         print("Launching Firefox Browser............")
#         return driver
#     else:
#         print("Launching Edge Browser............")
#         edge_driver_path = r"C:\Users\Asus\P(ycharmProjects\pythonProject2\Drivers\edgedriver_win64\msedgedriver.exe"
#         edge_service = Service(edge_driver_path)
#         driver = webdriver.Edge(service=edge_service)
#         return driver
#
#
#     # if browser == "msedgedriver":
#     #     print("Launching Edge Browser............")
#     # elif browser == "Firefox":
#     #     driver = webdriver.Firefox(r"C:\Users\Asus\PycharmProjects\pythonProject2\Drivers\edgedriver_win64\msedgedriver.exe")
#     #     print("Launching Firefox Browser............")
#     #     return driver
# def pytest_addoption(parser):    # This will get the value from CLI/hooks
#     parser.addoption("--browser")
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")




    #
    # edge_driver_path = r"C:\Users\Asus\PycharmProjects\new_nop_commerce\driver_edge\msedgedriver.exe"
    # edge_service = Service(edge_driver_path)
    # driver = webdriver.Edge(service=edge_service)