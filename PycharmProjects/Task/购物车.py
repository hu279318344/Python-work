#!/usr/bin/env python
# encoding: utf-8

"""
@version: Python 2.7
@author: Admin
@license: Apache Licence 
@contact: yang.hu@live.com
@software: PyCharm
@file: 购物车.py
@time: 2017/2/9 14:26
"""

import sys

products = ['Car', 'Iphone', 'Coffee', 'Mac', 'Cloths', 'Bicyle']
pices = [250000, 4999, 35, 9688, 438, 1500]
shop_list = []

while True:
    try:
        salary = int(raw_input("\033[5;31mPleasn input you salary:"))
        break
    except ValueError:
        print 'Please Input a Number ,not string ... ...'

while True:
    print "\033[33;1mThings have in the shop,Pleas Choose one to Buy:"
    for p in products:
        # products_index = products.index(p)
        print "\033[32;1m%s \t%s \033[0m" % (p, pices[products.index(p)])
        # print p,pices[products.index(p)]

    F_choice = raw_input('\033[1;34mPlease input one item to buy:')


    if F_choice == 'quit':
        print "\033[36;1m\nYou have bought these thing: %s \033[0m" % shop_list

        sys.exit()

    if F_choice in products:
        product_price_index = products.index(F_choice)
        product_price = pices[product_price_index]
        print '%s $%s'%(F_choice,product_price)
        if product_price <= salary:
            shop_list.append(F_choice)
            print "Added %s Into Your Shop List" % F_choice
            salary -= product_price
            print "Your Salary left: $", salary
        else:
            if salary < min(pices):
                print "Sorry,Rest of your Salary cannot Buy anything! Byebey"
                print "\033[36;1m\nYou have bought these thing: %s \033[0m" % shop_list
                sys.exit()
            else:
                print "\033[31;1mSorry , You cannot afford thin product,Please thy other ones!\033[0m"

                #print "\033[36;1m\nYou have bought these thing: %s \033[0m" % shop_list
                sys.exit()
