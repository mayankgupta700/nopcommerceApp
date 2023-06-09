# password must contain at least 8 characters with at least 1 uppercase, 1 lowercase, 1,
# number and a special characters
import csv
class Registration:
    lst = []
    def __init__(self, fname, lname, username, password, phone):
        self.fname = fname
        self.lname = lname
        self.password = password
        self.username = username
        self.phone = phone
        self.Email = f"{self.fname}.{self.lname}@company.com"

        with open("csv_file" , "r+") as file:
                    csv_writer = csv.writer(file)
                    Registration.lst.append(self.fname)
                    Registration.lst.append(self.lname),
                    Registration.lst.append(self.username)
                    Registration.lst.append(self.password)
                    Registration.lst.append(self.Email)
                    csv_writer.writerow(Registration.lst)

    def __setattr__(self, key, value):
         if key == "phone":
             if len(value) != 10:
                 raise ValueError("Number must be of 10 digits")
             if value[0] not in "6789":
                 raise ValueError("Number must start with 6/7/8/9")
             def outer(func):
                 def inner(value):
                     a = func(value)
                     add = "+91" + value
                     return add
                 return inner
             @outer
             def func(value):
                 return value
             s = func(value)
             super.__setattr__(self, key, s)
         elif key == "password":
                if len(value) < 8:
                    raise ValueError("Password length must be atleast 8 characters")
                super().__setattr__(key, value)
         else:
             super.__setattr__(self, key, value)
a = Registration("mayank", "gupta", "username", "123456wR", "9234567890")

class Custom_list():
    def __init__(self):
        self.lst = []
    def append(self,value):
        self.lst += value
        return self.lst
    def pop(self):
        ...
    def index(self):
        ...
    def copy(self):
        ...
a = Custom_list()
print(a.append("5"))
