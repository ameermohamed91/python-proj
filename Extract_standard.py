import logging  
import os
import time
  
path = '/disk1/eeoFiles/ToProcess'
#Create and configure logger using the basicConfig() function  
logging.basicConfig(filename="/disk1/eeoFiles/log_chk/eeo_logpy.log",  
               format='%(asctime)s %(message)s',  
               filemode='w', force=True)  

files = os.listdir(path)
logger=logging.getLogger()  

for f in files:
    from ExtractTable import ExtractTable
    et_sess = ExtractTable(api_key="mAK47Dg5veYvNLoTUT6H7WldpRohKFfVXyQTqEFR") 
    print(et_sess.check_usage())
    print(path+"/"+f)
    logger.info(f)
    # To process PDF, make use of pages ("1", "1,3-4", "all") params in the read_pdf function
    #table_data = et_sess.process_file(filepath=path+"/"+f, output_format="df", pages="all")
    table_data = et_sess.process_file(filepath=path+"/"+f, output_format="df", pages="23")
    time.sleep(2)
    

    print(et_sess.view_transactions())
    logger.info(et_sess.view_transactions())