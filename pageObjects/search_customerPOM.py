import pytest
from selenium.webdriver.support.ui import Select
import time
from selenium import webdriver
from selenium.webdriver import Edge
# driver = webdriver.Edge(executable_path="")
class Search_customer():
    # Add customer page
    customer_submodule_xpath = "(//i[@class='nav-icon far fa-dot-circle' and //p[.=' Customers']])[13]"
    customer_mainmodule_xpath = "//i[@class='nav-icon far fa-user']"
    add_new_button_xpath = "//a[@class='btn btn-primary']"
    add_new_customer_email_id = "SearchEmail"
    add_new_customer_fname_id = "SearchFirstName"
    add_new_customer_lname_id = "SearchLastName"
    search_button_id = "search-customers"
    # tbl_search_results_xpath = "//table[@role = 'grid']"
    table_xpath = "//table[@id='customers-grid']"  # Complete Table will be highlighted
    table_rows_xpath = "//table[@id='customers-grid']//tbody/tr"  # It will give all the rows
    table_column_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    # dob_drop_down_month_id = "SearchMonthOfBirth"
    # dob_drop_down_day_id = "SearchDayOfBirth"
    # reg_date_from_id = "SearchRegistrationDateFrom"
    # reg_date_to_id = "SearchRegistrationDateTo"
    # last_activity_from_id = "SearchLastActivityFrom"
    # last_activity_to_id = "SearchLastActivityTo"
    # company_id = "SearchCompany"
    # ip_add_id = "SearchIpAddress"

    def __init__(self, setup):
        self.driver = setup
    def click_search_customer_button(self):
        self.driver.find_element("id", self.search_button_id).click()
    def click_menubar_homepage(self):
        self.driver.find_element("xpath", "//i[@class='fa fa-bars']").click()
    def clickon_customer_mainmodule(self):
        self.driver.find_element("xpath", self.customer_mainmodule_xpath).click()
    def click0n_customer_submodule(self):
        self.driver.find_element("xpath", self.customer_submodule_xpath).click()
    def clickon_add_new_button(self):
        self.driver.find_element("xpath", self.add_new_button_xpath).click()
    def add_new_cust_email_txtbx(self,email):
        self.driver.find_element("id", self.add_new_customer_email_id).clear()
        self.driver.find_element("id", self.add_new_customer_email_id).send_keys(email)
    def add_new_customer_fname_txtbx(self,fname):
        self.driver.find_element("id", self.add_new_customer_fname_id).clear()
        self.driver.find_element("id", self.add_new_customer_fname_id).send_keys(fname)
    def add_new_customer_lname_txtbx(self, lname):
        self.driver.find_element("id", self.add_new_customer_lname_id).clear()
        self.driver.find_element("id", self.add_new_customer_lname_id).send_keys(lname)
    def get_numberofrows(self):   # It will give all the rows in the form of a list then we are taking it's length
        return len(self.driver.find_elements("xpath", self.table_rows_xpath))
    def get_numberofcolumns(self):  # It will give all the columns in the form of a list then we are taking it's length
        return len(self.driver.find_elements("xpath", self.table_column_xpath))
    @pytest.mark.regression
    def search_customer_byEmail(self, email):
        flag = False
        for r in range(1,self.get_numberofrows() + 1):
            table = self.driver.find_element("xpath", self.table_xpath)
            emailid = table.find_element("xpath", "//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag
    def search_customer_byname(self, Name):
        flag = False
        for r in range(1,self.get_numberofrows() + 1):
            table = self.driver.find_element("xpath", self.table_xpath)
            name = table.find_element("xpath", "//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag


























    # def clickon_dob_drop_down_month(self):
    #     dd = self.driver.find_element("id", self.dob_drop_down_month_id)
    #     s = Select(dd)
    #     s.select_by_value(10)
    # def clickon_dob_drop_down_day(self):
    #     dd = self.driver.find_element("id", self.dob_drop_down_day_id)
    #     s = Select(dd)
    #     s.select_by_value(9)
    #
    # def reg_date_from_txtbx(self, date):
    #     self.driver.find_element("id", self.reg_date_from_id).send_keys(date)
    #     # 5/30/2023 date format
    # def reg_date_to_txtbx(self, date):
    #     self.driver.find_element("id", self.reg_date_to_id).send_keys(date)
    # def last_activity_from_txtbx(self, date):
    #     self.driver.find_element("id", self.last_activity_from_id).send_keys(date)
    # def last_activity_to_txtbx(self, date):
    #     self.driver.find_element("id", self.last_activity_to_id).send_keys(date)
    # def company_txtbx(self, cname):
    #     self.driver.find_element("id", self.company_id).send_keys(cname)
    # def ip_add_txtbx(self, ip):
    #     self.driver.find_element("id", self.ip_add_id).send_keys(ip)
    #
    # def set_customer_roles(self, role):
    #     self.driver.find_element("xpath", self.cust_roles_textbox_xpath).click()
    #     time.sleep(3)
    #     if role == "Administrators":
    #         self.listitem = self.driver.find_element("xpath", self.cust_roles_admin_xpath)
    #     elif role == "Forum Moderators":
    #         self.listitem = self.driver.find_element("xpath", self.cust_roles_forum_xpath)
    #     elif role == "Guests":
    #         self.driver.find_element("xpath", "(//span[@class='k-select'])[5]").click()
    #         self.listitem = self.driver.find_element("xpath", self.cust_roles_guest_xpath)
    #     elif role == "Registered":
    #         # here user can be Regstered or Guest ANY ONE only
    #
    #         self.listitem = self.driver.find_element("xpath", self.cust_roles_registered_xpath)
    #     elif role == "Vendors":
    #         self.listitem = self.driver.find_element("xpath", self.cust_roles_vendor_xpath)
    #     else:
    #         self.listitem = self.driver.find_element("xpath", self.cust_roles_guest_xpath)
    #     # This is a jscript code below
    #     self.driver.execute_script("arguments[0].click();", self.listitem)


# driver.get("https://admin-demo.nopcommerce.com/Admin/Customer/List")
# a = Addcustomer(driver)

# rows = //table[@id= 'customers-grid']//tbody/tr/td

