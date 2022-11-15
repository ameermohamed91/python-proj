# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 18:02:30 2022

@author: Dell
"""

import os

path = '/disk1/Global_Property'

files = os.listdir(path)

for f in files:
   print(f)