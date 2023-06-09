# l = [3, 2, 1, 5, 4, 5, 3, 3, 15, 2]		# 3,2,1,5,4,15
# for ele in l:
# 	if l.count(ele) >= 2:
# 		l.remove(ele)
# print(l)
# def outer(func):
#     def inner(num):
#         a = "+91" + func(num)
#         return a
#     return inner
# @outer
# def func(num):
#     return num
# print(func("7505873700"))
# class employee:
#     def __init__(self, fname, lname, age, pin):
#         self.fname= fname
#         self.lname = lname
#         self.age = age
#         self.pin = pin
#     def __setattr__(self, key, value):
#         if key == "age":
#             if not isinstance(value, int):
#                 raise ValueError("Age should be of integer datatype")
#             if value < 18:
#                 raise ValueError("Employee must be of age greater than 18")
#             super().__setattr__(key, value)
#         elif key == "pin":
#             @property
#             def pin():
#                 return self._pin
#             @pin.setter
#             def pin():
#                 if len(key) < 4:
#                     raise ValueError("pin should be of 4 digits")
#                 self.pin = value
#                 super().__setattr__(key, value)
#         else:
#             super().__setattr__(key, value)
# a = employee("abc", "zxy", 19, 1234)
# print(a.__dict__)
# # sort the list with last name
# names = ['steve jobs', 'bill gates', 'john doe', 'tim cook', 'laura turn']
# f = sorted(names, key= lambda item: item[-1])
# print(f)
# from pageObjects.loginPage import Login
# from pageObjects.search_customerPOM import Search_customer
# from selenium import webdriver
# driver = webdriver.Edge(executable_path=r"D:\Mayank manual project scrum team 2\edgedriver_win64 (2)\msedgedriver.exe")
# from time import sleep
# un = "admin@yourstore.com"
# Login.set_username(un)
# Login.set_password("admin")
# Login.click_login_button()
# Search_customer.clickon_customer_mainmodule()
# Search_customer.click0n_customer_submodule()