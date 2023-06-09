from time import sleep
from pageObjects.loginPage import Login
import pytest
from pageObjects.search_customerPOM import Search_customer
from Utilities.readProperties import ReadConfig
from Utilities.CustomLogger import LogGen

class Test_003_AddCustomer:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addcustomer(self, setup):
        self.logger.info("********Test_003_Search_Customer**********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.login_obj = Login(setup)
        self.SearchCust_obj = Search_customer(setup)

        self.login_obj.set_username(self.username)
        self.login_obj.set_password(self.password)
        self.login_obj.click_login_button()
        self.logger.info("***********Login Successful*************")

        self.SearchCust_obj.clickon_customer_mainmodule()
        self.SearchCust_obj.click0n_customer_submodule()

        self.SearchCust_obj.add_new_cust_email_txtbx("kiyjcycyhjc676008@gmail.com")

        self.SearchCust_obj.add_new_customer_fname_txtbx("Mayank")
        self.SearchCust_obj.add_new_customer_lname_txtbx("gupta")
        # self.SearchCust_obj.search_customer_byname("Virat Kohli")
        status = self.SearchCust_obj.search_customer_byEmail("urld3r2i@gmail.com")
        self.SearchCust_obj.click_search_customer_button()
        assert True==status
        self.logger.info("**********TC IS PASSED**********")