#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 14:52:34 2020

@author: isabellagm
"""

 

"""

female percentage by year imported from excel:

2008 female=97 total=410 24%
2009 female=13 total=62 21%
2010 female=64 total=150 43%
2011 female=10 total=49 20%
2012 female=16 total=103 16%
2013 female=25 total=260 10%
2014 female=11 total=72 15%
2015 female=31 total=99 31%
2016 female=25 total=240 10%
2017 female=16 total=457 4%
2018 female=17 total=202 8%
"""



import matplotlib
import matplotlib.pyplot as plt


plt.plot([2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020], [24, 21, 43, 20, 16, 10, 15, 31, 10, 4, 8, 9, 22], color='#C63F3F', linewidth='3')

plt.xlabel("Year", fontfamily='Helvetica', color='#717171')
plt.ylabel('% of Work Purchased Created by Women', fontfamily='Helvetica', color='#717171')
plt.title("  ", fontfamily='Helvetica', color='#717171')


ax = plt.subplot(111)
ax.plot()

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)


plt.grid()
plt.rcParams['grid.color'] = "#717171"

ax.grid(color='#717171', linewidth=.3)

plt.savefig('linegraphfinal.png', dpi=300)

plt.show()




