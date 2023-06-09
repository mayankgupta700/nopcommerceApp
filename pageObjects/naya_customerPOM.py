import string
import random
from selenium.webdriver.support.ui import Select
from pageObjects.loginPage import Login
class NayaCustomer:
    email_id = "Email"
    first_name_id = "FirstName"
    last_name_id = "LastName"
    gender_male = "Gender_Male"
    gender_female = "Gender_Female"
    dob_id = "DateOfBirth"
    company_id = "Company"
    newsletter_xpath = "(//div[@class='k-multiselect-wrap k-floatwrap'])[1]"
    vendor_id = "VendorId"
    admin_comment_id = "AdminComment"
    cust_roles_textbox_xpath = "//div[@class='k-widget k-multiselect k-multiselect-clearable']"
    cust_roles_admin_xpath = "//li[.='Administrators']"
    cust_roles_forum_xpath = "//li[.='Forum Moderators']"
    cust_roles_guest_xpath = "//li[.='Guests']"
    cust_roles_registered_xpath = "//li[.='Registered']"
    cust_roles_vendor_xpath = "//li[.='Vendors']"
    search_button_id = "search-customers"
    customer_submodule_xpath = "(//i[@class='nav-icon far fa-dot-circle' and //p[.=' Customers']])[13]"
    customer_mainmodule_xpath = "(//i[@class='right fas fa-angle-left '])[4]"
    add_new_button_xpath = "//a[@class='btn btn-primary']"



    def __init__(self, setup):
        self.driver = setup
    def maximize_win(self):
        self.driver.maximize_window()
    def click_menubar_homepage(self):
        self.driver.find_element("xpath", "//i[@class='fa fa-bars']").click()
    def clickon_customer_mainmodule(self):
        self.driver.find_element("xpath", self.customer_mainmodule_xpath).click()
    def click0n_customer_submodule(self):
        self.driver.find_element("xpath", self.customer_submodule_xpath).click()
    def clickon_add_new_button(self):
        self.driver.find_element("xpath", self.add_new_button_xpath).click()
    def email_textbox(self):
        self.email = random_generator() + '@gmail.com'
        self.driver.find_element("id", self.email_id).send_keys(self.email)
    def click_fname(self, fname):
        self.driver.find_element("id", self.first_name_id).send_keys(fname)
    def click_lastname(self, lname):
        self.driver.find_element("id", self.last_name_id).send_keys(lname)
    def click_genderMale(self):
        self.driver.find_element("id", self.gender_male).click()
    def click_genderFemale(self):
        self.driver.find_element("id", self.gender_female).click()
    def click_dob(self, date):
        self.driver.find_element("id", self.dob_id).send_keys(date)
        # 5/30/2023 dob format
    def click_company(self, company):
        self.driver.find_element("id", self.company_id).send_keys(company)
    def click_newsletter(self):
        self.driver.find_element("xpath", self.newsletter_xpath).click()
        # self.driver.find_element("xpath", "//li[.='Test store 2']").click()
    def click_vendor(self):
        dd = self.driver.find_element("xpath", "//select[@id='VendorId']")
        s =Select(dd)
        s.select_by_index(2)
    def save_and_continue_button(self):
        self.driver.find_element("xpath", "//button[@name='save-continue']").click()


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))

# from selenium import webdriver
# driver = webdriver.Edge(executable_path=r"D:\Mayank manual project scrum team 2\edgedriver_win64 (2)\msedgedriver.exe")
# from time import sleep
# a = Login(driver)
# b = NayaCustomer(driver)
# driver.maximize_window()
# a.set_username("admin@yourstore.com")
# a.set_password("admin")
# a.click_login_button()
# sleep(1)
#
# b.clickon_customer_mainmodule()
# b.click0n_customer_submodule()
# b.clickon_add_new_button()
# b.email_textbox()
# b.click_fname("mayank")
# b.click_lastname("gupta")
# b.click_genderMale()
# b.click_genderFemale()
# b.click_dob("5/30/2023")
# b.click_company("ty")
# b.click_newsletter()
# b.click_vendor()
# b.save_and_continue_button()
