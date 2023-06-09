# For selenium 4.0 or greater version
import selenium.webdriver as webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
edge_driver_path = r"C:\Users\Asus\PycharmProjects\pythonProject2\Drivers\edgedriver_win64\msedgedriver.exe"
edge_service = Service(edge_driver_path)
driver = webdriver.Edge(service=edge_service)
driver.get("https://www.google.com")
