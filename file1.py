# # l = ["hello", "instagram", "yahoo"]
# # s = {}
# # d = lambda item:(item[0], item)
# # a = dict(map(d,l))
# # print(a)
# class employee():
#     def __init__(self, fname, lname, age, mobile, pin):
#         self.fname = fname
#         self.lname  =lname
#         self.age = age
#         self.mobile = mobile
#         self.pin = pin
#
#     def __setattr__(self, key, value):
#         if key == "age":
#             if not isinstance(value, int):
#                 raise ValueError("Datatype for age should be always integer")
#             if value < 18:
#                 raise ValueError("Employee should be adult")
#             super().__setattr__(key, value)
#         elif key == "mobile":
#             def outer(func):
#                 def inner(value):
#                     add = "+91" + value
#                     return add
#                 return inner
#             @outer
#             def func(value):
#                 return value
#             s = func(value)
#             super().__setattr__(key, s)
#         elif key == "pin":
#             @property
#             def pin(self):
#                 return self._pin
#             @pin.setter
#             def pin():
#                 if len(self.pin)<0:
#                     raise ValueError("pin must be of four digits")
#                 self.pin = value
#         else:
#             super().__setattr__(key, value)
# a = employee("may", "jun", 22, "6767676776", 1234)
# print(a.__dict__)
num = 5
f = 0
for i in range(2, num):
    if num % i == 0:
        f = 1
        break
    else:
        f = 0
if f == 0:
    print("s")
else:
    print("n")
















