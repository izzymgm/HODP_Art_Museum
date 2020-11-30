#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 18:22:30 2020

@author: isabellagm
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots()
ax.set(xlim=(-3, 3), ylim = (-3, 3))

a_circle = plt.Circle((.5,-.4), radius=0.3, color='#C63F3F')
b_circle = plt.Circle((0, 0), radius=1, color='#F1D3CF')



ax.add_artist(b_circle)
ax.add_artist(a_circle)


ax.axis("equal")
ax.axis('off')

fig.savefig('circlefinal.png', dpi=300)