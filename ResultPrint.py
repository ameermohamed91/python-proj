import logging  
import re
  
path = '/disk1/eeoFiles'
FilePath= '/disk1/eeoFiles/Log/'
f = open(FilePath+"logfile.txt", "w")
f_text = open(FilePath+"Textlogfile.txt", "a")
f_process = open(FilePath+"Processlogfile.txt", "a")
f_excep = open(FilePath+"Exceptionlogfile.txt", "a")
#Create and configure logger using the basicConfig() function  
logging.basicConfig(filename="/disk1/eeoFiles/log_chk/eeo_logtrans.log",  
               format='%(asctime)s %(message)s',  
               filemode='w')  
logger=logging.getLogger()  
f.write("doc_id\t table_no"+"\t"+"row_no"+"\t"+"col_no"+"\t"+"cell_data"+"\n")
f_text.write("doc_id\t LineData"+"\n")
f_process.write("doc_id \t fil_name \t job_state \t Pages \t createdon \t txn_id"+"\n")



def write_TableData(TablesList):
    table_no=0
    for table in TablesList:
        table_no=table_no+1
        #table_keys=table.keys()
        #print(str(table_keys))
        table_json_val = table["TableJson"]
        #print(str(type(table_json_val)))
        for row_no_val in table_json_val:
            #print("Rows::"+row_no_val)
            row_val_list = table_json_val[row_no_val]
            #print(str(row_val))
            for col_no in row_val_list:
                #print("cols::"+col_no)
                cell_data = row_val_list[col_no]
                f.write(doc_id+"\t"+str(table_no)+"\t"+row_no_val+"\t"+col_no+"\t"+cell_data+"\n")
                #print(row_no_val+"\t"+col_no+"\t"+cell_data)
        print(doc_id + "\t Table Processed..."+str(table_no))
    
def write_LinesData(linesList, doc_id):
    cert_date=""
    for line in linesList:
         #print(str(type(line)))
         #line_keys = line.keys()
         #print(str(line_keys))
         #for x1 in line_keys:
         #    print(x1 + ":: "+ str(type(line[x1])))
         LinesArray_val = line["LinesArray"]
         print("LinesArray_val_size::" + str(len(LinesArray_val)))
         i=0
         for line_val_dic in LinesArray_val:
             line_val = line_val_dic['Line']
             #print(line_val)
             cert_date_found = re.search("^CERTI", line_val, re.IGNORECASE)
            # print("cert_date_found::"+str(cert_date_found))
             if cert_date_found:
                cert_date= line_val
                f_text.write(doc_id+"\t"+cert_date+"\n")
                print("cert_date::"+cert_date)
             i=i+1
               
    print(str(i)+"cert_date::"+cert_date)
    

def get_Resultval(et_sess, doc_id, txn_id):
    df = et_sess.get_result(txn_id)
    f_content = open(FilePath+doc_id+".txt","w")
    f_content.write(str(df))
    f_content.close()
    
    TablesList ={}
    if 'Tables' in df:
        TablesList = df["Tables"]
        write_TableData(TablesList)
    else:
        f_excep.write(doc_id+"Table Object Missing")
        
# =============================================================================
#     linesList ={}
#     if 'Lines' in df:
#         linesList = df["Lines"]   
#         write_LinesData(linesList, doc_id)
#     else:
#         f_excep.write(doc_id+"Line object Missing")
# =============================================================================
        
    #print("Table_size::" + str(len(TablesList)))
    
    
    
            

    
    

from ExtractTable import ExtractTable
et_sess = ExtractTable(api_key="TlISgm88rDeXTB964hpQVnlmWq3vUrqmFNCWNAsA")      


#print(et_sess.view_transactions())
#logger.info(et_sess.view_transactions())

thislist= et_sess.view_transactions()
#print('valuessssss'+str(thislist))
for x in thislist:
    #print(x)
    thisdict = x
    jb_stat = thisdict['JobStatus']
    Pages = thisdict['Pages']
    createdon = thisdict['createdon']
    fil_name = thisdict['request_filename']
    txn_id = thisdict['txn_id']
    doc_id = fil_name.replace(".pdf","");
    f_process.write(doc_id+"\t"+fil_name+"\t"+jb_stat+"\t"+ repr(Pages) +"\t"+repr(createdon)+"\t"+txn_id+"\n")
    print(doc_id+"\t"+fil_name+"\t"+jb_stat+"\t"+ repr(Pages) +"\t"+repr(createdon)+"\t"+txn_id)
    get_Resultval(et_sess, doc_id, txn_id)


f_excep.close()
f_process.close()
f_text.close()
f.close()
    
    

    
    
    