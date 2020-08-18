# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 15:38:03 2020

@author: USER
"""

m=float(input('請輸入數學成績:'))
e=float(input('請輸入英文成績:'))
if e>=0 and m>=0 and e<=100 and m<100:
    if m>=90 and e>=90:
        print('恭喜得獎')
    elif m<=60 and e<=60:
        print('挨罰')
    elif m<=60 or e<=60:
        print('再加油')
else:
    print('輸入錯誤')