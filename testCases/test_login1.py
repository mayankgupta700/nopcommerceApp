import logging

import pytest

from pageObjects.loginPage import Login
from Utilities.readProperties import ReadConfig  # to read data of config file with the help of readProperties.py file
from Utilities.CustomLogger import LogGen      # used for logging the details
class Test_001_login():
    base_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    after_login_exp_title = "Dashboard / nopCommerce administration"

    logger = LogGen.loggen()  # This will return the logger object returned from loggen static method in LogGen class
                                # present in CustomLogger file
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homepage_title(self, setup):
        self.logger.info("***********************Test_001_login***************************")
        self.logger.info("*******Verifying Homepage Title***************************")
        self.driver = setup
        self.driver.get(self.base_url)
        act_title = self.driver.title


        if act_title == "Your store. Login":  # Assert is used show pass or fail status in terminal

            assert True
            self.logger.info("*****************Homepage_Title TC is passed**********************")
        else:
            self.logger.error("*****************Homepage_Title TC is failed**********************")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepage_title.png")
            self.driver.close()
            assert False
    def test_login(self, setup):
        self.logger.info("*******************Verifying login TC**********************")
        self.driver = setup
        self.driver.get(self.base_url)
        self.login_obj = Login(setup)
        self.driver.find_element("id", "Email").clear()
        self.driver.find_element("id", "Email").send_keys("admin@yourstore.com")
        self.driver.find_element("id", "Password").clear()
        self.driver.find_element("id", "Password").send_keys("admin")
        self.driver.find_element("xpath", "//button[.='Log in']").click()
        act_title_after = self.driver.title

        if self.after_login_exp_title == act_title_after:
            self.driver.quit()
            assert True
            self.logger.info("*****************Login TC is Passed**********************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepage_title.png")
            self.driver.close()
            self.logger.error("*****************Login TC is Failed**********************")
            assert False