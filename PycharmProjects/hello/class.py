#!/usr/bin/env python
# encoding: utf-8

"""
@version: Python 3.6
@author: Admin
@license: Apache Licence 
@contact: yang.hu@live.com
@software: PyCharm
@file: class.py
@time: 2017/3/7 10:07
类的初始化
"""



"""
class dog:
    def __init__(self,name):
        print("Hello Dog!")
        self.Name = name
    def sayname(self):
        print("Hello My name is Baibei %s" %  self.Name)


animal = dog("doudou")

if __name__ == '__main__':
    animal.sayname()
else:
    print("This program can only run the machine")
"""

"""
类的绑定
"""
class Person: #父类
    def __init__(self,Type,Sex,Age,Name):
        self.race = Type,
        self.sex = Sex,
        self.age = Age,
        self.name = Name,
    def talk(self,msg=0):
        self.msg = msg,
        if self.msg != 0:
            print(self.name,'Saying:',self.msg)
        else:
            print('My Name is %s' % self.name)
p = Person('Black','Female','24','Susan')
# #p.talk()
p.talk('Hello, My name is %s' % p.name)

class person_info(Person): #子类
    def __init__(self,Type,Sex,Age,Name,nation,work,salary):
        Person.__init__(self,Type,Sex,Age,Name) #继承父类的变量
        self.country = nation,
        self.job = work,
        self.salary = salary,
    def tell(self):
        print ( '''%s  perssonal information:
                        Name : %s
                        Age  : %s
                        Sex  : %s
                        Coun: %s
                        Work : %s
                        Salary: %s
               '''  % (self.name , self.name , self.age , self.sex , self.country , self.job , self.salary))

T = person_info('Black','Female','24','Susan','China','IT','han')
T.tell()

p.talk('Hai')
p = Person('Black','Female','24','yanghu')

p.talk('Hello, My name is %s' % p.name)