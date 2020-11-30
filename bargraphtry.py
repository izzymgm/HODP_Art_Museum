#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 23:04:36 2020

@author: isabellagm
"""

import matplotlib
import matplotlib.pyplot as plt

plt.grid()
plt.rcParams['grid.color'] = "#717171"


plt.bar(['male artists',  'female artists'], [.24, .44], color= ['#C63F3F', '#760000', '#760000'], linewidth='3', zorder=3)
plt.xlabel("", fontfamily='Helvetica', color='#717171')
plt.ylabel('Average Number of Exhibitions per Object', fontfamily='Helvetica', color='#717171')
plt.title("  ", fontfamily='Helvetica', color='#717171')


ax = plt.subplot(111)
ax.plot()

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)




ax.grid(color='#717171', linewidth=.3)
ax.grid(zorder=0)

plt.savefig('bargraphfinal.png', dpi=300)

plt.show()



