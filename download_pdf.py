# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 20:13:48 2022

@author: Dell
"""

import requests
file_url = "https://www.amd.com/system/files/documents/2020-eeo-1-consolidated-report.pdf"
print("start")
r = requests.get(file_url, stream = True)

with open("python.pdf","wb") as pdf:
	for chunk in r.iter_content(chunk_size=1024):

		# writing one chunk at a time to pdf file
		if chunk:
			pdf.write(chunk)
print("finish")