import logging  

  
path = '/disk1/eeoFiles'

#Create and configure logger using the basicConfig() function  
logging.basicConfig(filename="/disk1/eeoFiles/log_chk/eeo_logtrans.log",  
               format='%(asctime)s %(message)s',  
               filemode='w')  
logger=logging.getLogger()  

from ExtractTable import ExtractTable
et_sess = ExtractTable(api_key="TlISgm88rDeXTB964hpQVnlmWq3vUrqmFNCWNAsA")      


print(et_sess.view_transactions())
#logger.info(et_sess.view_transactions())

thislist= et_sess.view_transactions()
print('valuessssss'+str(thislist))
for x in thislist:
    #print(x)
    thisdict = x
    jb_stat = thisdict['JobStatus']
    Pages = thisdict['Pages']
    createdon = thisdict['createdon']
    fil_name = thisdict['request_filename']
    txn_id = thisdict['txn_id']
    
    print(fil_name+"\t"+jb_stat+"\t"+ repr(Pages) +"\t"+repr(createdon)+"\t"+txn_id)
    
    
    
    
  #  {'JobStatus': 'Success', 'Pages': 5, 'createdon': 1653390884, 
  #'request_filename': '353441.pdf', 'txn_id': '7c5dd7dd41048c3e9e780a0d668a6f798d3f74375e7c58daae50607ac8dcf08e'}