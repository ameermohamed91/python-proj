import logging  

from jproperties import Properties

configs = Properties()
project_properties = Properties()

with open('/disk1/Global_Property/SERVER.properties', 'rb') as config_file:
    configs.load(config_file)
    
with open('./config/app-config.properties', 'rb') as proj_config:
    project_properties.load(proj_config)
    

api_key_val = project_properties.get("api_key").data
log_path = project_properties.get("log_path").data


FilePath= log_path
f = open(FilePath+"logfile.txt", "w")
f_text = open(FilePath+"Textlogfile.txt", "a")
f_process = open(FilePath+"Processlogfile.txt", "a")
f_excep = open(FilePath+"Exceptionlogfile.txt", "a")


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
        
    #print("Table_size::" + str(len(TablesList)))
    
    
        

from ExtractTable import ExtractTable
et_sess = ExtractTable(api_key=api_key_val)      


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
    
    

    
    
    