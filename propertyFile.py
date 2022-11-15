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




print(dbuser_val+"::"+dbpwd_val+"::"+ip_val+"::"+database_val+"::"+port_val)
