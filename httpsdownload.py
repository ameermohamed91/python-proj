# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 20:31:40 2022

@author: Dell
"""

import requests
# Define the remote file to retrieve
print("Start")
remote_url = 'https://www.amd.com/system/files/documents/2020-eeo-1-consolidated-report.pdf'
# Define the local filename to save data
local_file = 'local_copy.pdf'
# Make http request for remote file data
data = requests.get(remote_url)
# Save file data to local copy
with open(local_file, 'wb') as file:
    file.write(data.content)
print("end")