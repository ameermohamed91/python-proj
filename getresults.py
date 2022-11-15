import logging  
import re
  
path = '/disk1/eeoFiles'
FilePath= '/disk1/eeoFiles/'
f = open(FilePath+"demofile.txt", "a")
#Create and configure logger using the basicConfig() function  
logging.basicConfig(filename="/disk1/eeoFiles/log_chk/eeo_logtrans.log",  
               format='%(asctime)s %(message)s',  
               filemode='w', force=True)  
logger=logging.getLogger()  

from ExtractTable import ExtractTable
et_sess = ExtractTable(api_key="6CRFKdCa42wEVgGTgF9pVVBDuhewywiAW6eLmsHs")      


df = et_sess.get_result("56ca658cd6128a5405ceb9b0d41fb43c8199cdb822b2bed6a154a311d86eaf6a")
#print(df)
# print("Lines: "+str(df))
# print(df.keys())
# df_keys = df.keys()
# for x in df_keys:
#     print(x + ":: "+ str(type(df[x])))
    
# linesList ={}
# if 'Lines' in df:
#     linesList = df["Lines"]
# else:
#     print("Not found")

# print("Line_ Size::"+str(len(linesList)))
# cert_date=""
# #print(linesList[0])
# # =============================================================================
# # for line in linesList:
# #     print(str(type(line)))
# #     line_keys = line.keys()
# #     print(str(line_keys))
# #     #for x1 in line_keys:
# #     #    print(x1 + ":: "+ str(type(line[x1])))
# #     LinesArray_val = line["LinesArray"]
# #     print("LinesArray_val_size::" + str(len(LinesArray_val)))
# #     i=0
# #     for line_val_dic in LinesArray_val:
# #         line_val = line_val_dic['Line']
# #         #print(line_val)
# #         cert_date_found = re.search("^CERTI", line_val, re.IGNORECASE)
# #        # print("cert_date_found::"+str(cert_date_found))
# #         if cert_date_found:
# #            cert_date= line_val
# #            print("cert_date::"+cert_date)
# #         i=i+1
# #           
# # print(str(i)+"cert_date::"+cert_date)
# # =============================================================================

TablesList ={}
if 'Tables' in df:
    TablesList = df["Tables"]
#print("Table_size::" + str(len(TablesList)))

for table in TablesList:
    table_keys=table.keys()
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
            f.write(row_no_val+"\t"+col_no+"\t"+cell_data+"\n")
            print(row_no_val+"\t"+col_no+"\t"+cell_data)
        

# f.close()
# #print("Pages: "+type(df["Pages"]))
# #print("Pages: "+type(df["Pages"]))
