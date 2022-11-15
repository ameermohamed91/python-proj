# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 10:29:38 2022

@author: Dell
"""

import os

path = '/disk1/PdfFiles'

# files = os.listdir(path)

# for f in files:
from ExtractTable import ExtractTable
et_sess = ExtractTable(api_key="mAK47Dg5veYvNLoTUT6H7WldpRohKFfVXyQTqEFR") 
print(et_sess.check_usage()) 
  #  table_data = et_sess.process_file(filepath=path+"/"+f, output_format="df", pages="142-154")
    

  #  print(et_sess.view_transactions())