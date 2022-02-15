import os
from datetime import datetime as dt
import getpass
from tkinter import * 
from tkinter import messagebox

import speedtest
import requests

s = speedtest.Speedtest()

date = dt.today().strftime("%m/%d/%y/ %H:%M")
computer_name = os.uname().nodename
user_name = getpass.getuser()
isp = s.get_config()['client']['isp']
download = round(s.download()/1000000, 2)
upload = round(s.upload()/1000000, 2)

pload = {'date': date, 'computer_name': computer_name, 'user_name': user_name, 'isp': isp, 'download': download, 'upload': upload, 'connection_type': 'TBD'}

r = requests.post('https://inteminer.com/api/api.php', data=pload)

messagebox.showinfo(title="Speedtest recorded", message=f"ISP: {isp}\nDowload: {download} Mbps\nUpload: {upload} Mbps", icon="info")

if r:
  print ("Speedtest successfull. You may now close this window.")
else:
  print("Something went wrong. Please try again.")