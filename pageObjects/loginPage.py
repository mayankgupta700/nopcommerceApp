
class Login:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[.='Log in']"

    def __init__(self, setup):
        self.driver = setup
        self.driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    def set_username(self,username):
        self.driver.find_element("id", Login.textbox_username_id).clear()
        self.driver.find_element("id", Login.textbox_username_id).send_keys(username)
    def set_password(self,password):
        self.driver.find_element("id", Login.textbox_password_id).clear()
        self.driver.find_element("id", Login.textbox_password_id).send_keys(password)
    def click_login_button(self):
        self.driver.find_element("xpath", Login.button_login_xpath).click()
    def click_logout_button(self):
        self.driver.find_element("xpath", "//a[.='Logout']").click()

# from selenium import  webdriver
# driver = webdriver.Edge(
#     executable_path=r"D:\Mayank manual project scrum team 2\edgedriver_win64 (2)\msedgedriver.exe")
#
#
# from time import sleep
# a = Login(driver)
# a.set_username("admin@yourstore.com")
# a.set_password("admin")
# a.click_login_button()
# sleep(3)
# a.click_logout_button()
# a.click_hover_login_button()
