import ast
import logging  
import os
import re
  
path = '/disk1/eeoFiles/Log'
FilePath= '/disk1/eeoFiles/'
fwrite = open(FilePath+"period_Date.txt", "a")

files = os.listdir(path)
logger=logging.getLogger()  

i=1
for f in files:
    print(i,":::",f)
    i=i+1
i=0
for f in files:
    i=i+1
    with open(path+"/"+f) as f1:
        data = f1.read()
        print(i,"Data type before reconstruction : ", type(data))
        df = ast.literal_eval(data)
        print(f,"Data type after reconstruction : ", type(df))
        df_keys = df.keys()
        for x in df_keys:
            print(x + ":: "+ str(type(df[x])))
            #print("Pages::"+str(df['Pages']))
            
        linesList ={}
        if 'Lines' in df:
            linesList = df["Lines"]
        else:
            print("Not found")

        print("Line_ Size::"+str(len(linesList)))
        cert_date=""
        #print(linesList[0])
        line_count=0
        for line in linesList:
            line_count = line_count+1
            print(str(type(line)))
            line_keys = line.keys()
            print(str(line_keys))
            #for x1 in line_keys:
            #    print(x1 + ":: "+ str(type(line[x1])))
            LinesArray_val = line["LinesArray"]
            print("LinesArray_val_size::" + str(len(LinesArray_val)))
            i=0
            for line_val_dic in LinesArray_val:
                line_val = line_val_dic['Line']
                #print(line_val)
                cert_date_found = re.search("PERIOD", line_val, re.IGNORECASE)
                # print("cert_date_found::"+str(cert_date_found))
                if cert_date_found:
                    cert_date= line_val
                    line_val_next=""
                    if len(LinesArray_val)>(i+1):
                        line_val_dic_next = LinesArray_val[i+1]
                        line_val_next = line_val_dic_next['Line']
                    if re.search(r"\d{4}", cert_date, re.IGNORECASE):
                        print(line_count,"::PERIOD_date::"+cert_date)
                        fwrite.write(f+"\t"+str(line_count)+"\t"+cert_date+"\n")
                    else:
                        print(line_count,"::elsPERIOD_date::"+line_val_next)
                        fwrite.write(f+"\t"+str(line_count)+"\t"+cert_date+' '+line_val_next+"\n")
                    
                thru_found = re.search("THRU", line_val, re.IGNORECASE)
                if thru_found:
                    thru_date= line_val
                    line_val_next = ""
                    if len(LinesArray_val)>(i+1):
                        line_val_dic_next = LinesArray_val[i+1]
                        line_val_next = line_val_dic_next['Line']
                    if re.search(r"\d{4}", cert_date, re.IGNORECASE):
                        print(line_count,"::PERIOD_thru_date::"+thru_date)
                        fwrite.write(f+"\t"+str(line_count)+"\t"+thru_date+"\n")
                    else:
                        print(line_count,"::elsPERIOD_thru_date::"+line_val_next)
                        fwrite.write(f+"\t"+str(line_count)+"\t"+thru_date+' '+line_val_next +"\n")
                    
                    
                i=i+1
                  
       # print(str(i)+"PERIOD_date::"+cert_date)
fwrite.close()        

