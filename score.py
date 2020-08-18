# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 14:58:28 2020

@author: USER
"""

i=float(input('請輸入成績:'))
if i>=0 and i>=100:
    if i>=90:
        print('等級A')
    elif i>=80:
        print('等級B')
    elif i>=70:
        print('等級c')
    elif i>=60:
        print('等級D')
    else:
        print('等級E')
else:
    print('輸入錯誤')