import logging  
import os
import time
  
path = '/disk1/eeoFiles/ToProcess/310416.pdf'

from ExtractTable import ExtractTable
et_sess = ExtractTable(api_key="TlISgm88rDeXTB964hpQVnlmWq3vUrqmFNCWNAsA") 
print(et_sess.check_usage())

# To process PDF, make use of pages ("1", "1,3-4", "all") params in the read_pdf function
#table_data = et_sess.process_file(filepath=path+"/"+f, output_format="df", pages="all")
table_data = et_sess.process_file(filepath=path, output_format="df", pages="2")
time.sleep(2)


print(et_sess.view_transactions())
