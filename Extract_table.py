
import mysql.connector  
import time

from jproperties import Properties

configs = Properties()
project_properties = Properties()

with open('/disk1/Global_Property/SERVER.properties', 'rb') as config_file:
    configs.load(config_file)
    
with open('./config/app-config.properties', 'rb') as proj_config:
    project_properties.load(proj_config)

dbuser_val = configs.get("dbuser").data
dbpwd_val = configs.get("dbpwd").data
ip_val = configs.get("ip").data
database_val = configs.get("database").data
port_val = configs.get("port").data

file_path_val = project_properties.get("file_path").data
query_val = project_properties.get("file_list_query").data
api_key_val = project_properties.get("api_key").data
log_path = project_properties.get("log_path").data
  
#Create the connection object   
myconn = mysql.connector.connect(host = ''+ip_val, user = ''+dbuser_val, passwd = ''+dbpwd_val, port=''+port_val)  
 
path = file_path_val+'/'


#files = os.listdir(path)
 
print("in")
#creating the cursor object  
cur = myconn.cursor(dictionary=True)
dict={}
  
try:  
    dbs = cur.execute(query_val)  
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
    et_sess = ExtractTable(api_key=api_key_val) 
    print(et_sess.check_usage()) 
    
    print(path+"/"+str(ld_doc_id)+".pdf")
    # To process PDF, make use of pages ("1", "1,3-4", "all") params in the read_pdf function
    #table_data = et_sess.process_file(filepath=path+"/"+str(ld_doc_id)+".pdf", output_format="df", pages=page_no)
    time.sleep(5)
    

    print(et_sess.view_transactions())
    