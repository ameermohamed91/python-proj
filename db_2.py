
import mysql.connector  
  
#Create the connection object   
myconn = mysql.connector.connect(host = "10.86.51.13", user = "LD_Engg",passwd = "B8E7B6CA", port="3306")  
  
#creating the cursor object  
cur = myconn.cursor(dictionary=True)
  
 
dbs = cur.execute("  SELECT * FROM `Corporate_Governance`.`CorpGov_FormLookup`  WHERE form_group<>'Code of Ethics' ;")  
result_set = cur.fetchall()
 
for row in result_set:
    print(row['form_group'])
myconn.close()  







import mysql.connector  
  
#Create the connection object   
myconn = mysql.connector.connect(host = "10.86.51.13", user = "LD_Engg",passwd = "B8E7B6CA", port="3306")  
  
print("in")
#creating the cursor object  
cur = myconn.cursor(dictionary=True)
dict={}
  
try:  
    dbs = cur.execute("SELECT * FROM `test`.`Extract_EEO` WHERE status = 'pending' ;")  
    results = cur.fetchall()
    #print(results)
    dict = results
    for row in results:
        ld_doc_id = row['ld_doc_id']
        page_no = row['page_no']        
        #print(ld_doc_id , "\t" , page_no)
        

except:  
    myconn.rollback()  

myconn.close()  

print("*************************************")

for row in dict:
    ld_doc_id = row['ld_doc_id']
    page_no = row['page_no']        
    print(ld_doc_id , "\t" , page_no)