
import mysql.connector  
import logging  
import os
import time
  
#Create the connection object   
myconn = mysql.connector.connect(host = "10.86.51.13", user = "LD_Engg",passwd = "B8E7B6CA", port="3306")  
 
path = '/disk1/eeoFiles'
#Create and configure logger using the basicConfig() function  
logging.basicConfig(filename="/disk1/eeoFiles/log_chk/eeo_logpy.log",  
               format='%(asctime)s %(message)s',  
               filemode='w', force=True)  

files = os.listdir(path)
logger=logging.getLogger()  
 
print("in")
#creating the cursor object  
cur = myconn.cursor(dictionary=True)
dict={}
  
try:  
    dbs = cur.execute("SELECT * FROM `test`.`Extract_EEO` WHERE status = 'pending'and row_id>116 and ld_doc_id!=359193 ;")  
    results = cur.fetchall()
    #print(results)
    dict = results
        

except:  
    myconn.rollback()  

myconn.close()  

print("*************************************")

for row in dict:
    ld_doc_id = row['ld_doc_id']
    page_no = row['page_no']        
    print(ld_doc_id , "\t" , page_no)
    from ExtractTable import ExtractTable
    et_sess = ExtractTable(api_key="TlISgm88rDeXTB964hpQVnlmWq3vUrqmFNCWNAsA") 
    print(et_sess.check_usage()) 
    
    # To process PDF, make use of pages ("1", "1,3-4", "all") params in the read_pdf function
    table_data = et_sess.process_file(filepath=path+"/"+str(ld_doc_id)+".pdf", output_format="df", pages=page_no)
    time.sleep(5)
    

    print(et_sess.view_transactions())
    logger.info(et_sess.view_transactions())