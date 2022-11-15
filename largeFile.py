import logging  
import os
  
path = '/disk1/eeoFiles'
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
    logger.info(f)
    table_data = et_sess.process_file(filepath=path+"/"+f, output_format="df", pages="129-135")
    

    print(et_sess.view_transactions())
    logger.info(et_sess.view_transactions())