import logging  
import mysql.connector  
  
#Create the connection object   
myconn = mysql.connector.connect(host = "10.86.51.13", user = "LD_Engg",passwd = "B8E7B6CA", port="3306")  
  
#creating the cursor object  
cur = myconn.cursor(dictionary=True)  

#Creating an object of the logging  
logger=logging.getLogger()  


"""
dbs = cur.execute("  SELECT * FROM `Corporate_Governance`.`CorpGov_FormLookup`  WHERE form_group<>'Code of Ethics' ;")  
result_set = cur.fetchall()
 
for row in result_set:
    print(row['form_group'])
myconn.close()  

"""
