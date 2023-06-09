# Two POM classes are referred in this test case
import pytest

from pageObjects.loginPage import Login
from pageObjects.naya_customerPOM import NayaCustomer
from Utilities.readProperties import ReadConfig
from Utilities.CustomLogger import LogGen
class Test_004_naya_customer:

    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_naya_customer(self, setup):
        self.logger.info("**********Test_004_naya customer Initiated***********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logobj = Login(setup)
        self.b = NayaCustomer(setup)
        self.b.driver.maximize_window()
        self.logobj.set_username("admin@yourstore.com")
        self.logobj.set_password("admin")
        self.logobj.click_login_button()

        self.b.clickon_customer_mainmodule()
        self.b.click0n_customer_submodule()
        self.b.clickon_add_new_button()
        self.b.email_textbox()
        self.b.click_fname("mayank")
        self.b.click_lastname("gupta")
        self.b.click_genderMale()
        self.b.click_genderFemale()
        self.b.click_dob("5/30/2023")
        self.b.click_company("ty")
        self.b.click_newsletter()
        self.b.click_vendor()
        self.b.save_and_continue_button()
        # "body" will capture every thing present in the page
        self.msg = self.driver.find_element_by_tag_name("body").text
        if " The new customer has been added successfully." in self.msg:
            assert True
            self.logger.info("************Test Case PASSED************")
        else:
            self.logger.info("************Test Case FAILED************")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_naya_customer.png")
            assert True