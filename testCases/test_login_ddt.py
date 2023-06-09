from pageObjects.loginPage import Login
from Utilities.readProperties import ReadConfig  # to read data of config file with the help of readProperties.py file
from Utilities.CustomLogger import LogGen      # used for logging the details
from Utilities import XLUTILS
from time import sleep
class Test_001_DDT_login():
    base_url = ReadConfig.getApplicationURL()
    path = r"C:\Users\Asus\PycharmProjects\new_nop_commerce\TestData\Book1.xlsx"
    logger = LogGen.loggen()  # This will return the logger object returned from loggen static method in LogGen class
                                # present in CustomLogger file

    def test_login(self, setup):
        self.logger.info("**************test_login_ddt************")
        self.logger.info("*******************Verifying login TC**********************")
        self.driver = setup
        self.driver.get(self.base_url)
        self.login_obj = Login(setup)
        self.number_row = XLUTILS.getrowcount(self.path, "Sheet1")

        self.lst_status = []
        for row in range(2, 6):

            self.excel_username = XLUTILS.readdata(self.path, "Sheet1", row, 1)
            self.excel_password = XLUTILS.readdata(self.path, "Sheet1", row, 2)
            self.exp_result = XLUTILS.readdata(self.path, "Sheet1", row, 3)

            self.login_obj.set_username(self.excel_username)
            self.login_obj.set_password(self.excel_password)
            self.login_obj.click_login_button()
            sleep(3)
            act_title_after = self.driver.title
            after_login_exp_title = "Dashboard / nopCommerce administration"

            if after_login_exp_title == act_title_after:   # This means LOGIN is Successful
                if self.exp_result == "pass":                        # This means Username and Password is correct
                    self.logger.info("*****************Login TC is Passed********11**************")
                    self.login_obj.click_logout_button()
                    sleep(3)
                    self.lst_status.append("pass")

                elif self.exp_result == "fail":
                    self.logger.info("*****************Login TC is Failed**********************")
                    self.driver.save_screenshot(".\\Screenshots\\" + "test_homepage_title.png")
                    self.lst_status.append("fail")

            elif after_login_exp_title != act_title_after:
                if self.exp_result == "pass":
                    self.logger.info("*****************Login TC is Failed**********************")
                    self.driver.save_screenshot(".\\Screenshots\\" + "test_homepage_title.png")
                    sleep(3)
                    self.lst_status.append("fail")

                elif self.exp_result == "fail":
                    self.logger.info("*****************Login TC is Passed*******12***************")
                    self.lst_status.append("pass")

        if "fail" not in self.lst_status:
            self.logger.info("*********Login DDT is PASSED*********")
            self.driver.quit()
            assert True
        else:
            self.logger.info("*****Login DDT is FAILED******")
            self.driver.quit()
            assert False