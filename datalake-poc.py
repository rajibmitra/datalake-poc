
from azure.datalake.store import core, lib, multithread
import adal
import logging, pprint, uuid, time
import pandas as pd 



subscriptionId = 'subscriptionId'
adlsAccountName = 'adlsAccountName'
adlCreds = lib.auth(tenant_id='tenent_id', resource = 'https://datalake.azure.net/')


adlsFileSystemClient = core.AzureDLFileSystem(adlCreds, store_name=adlsAccountName)


with adlsFileSystemClient.open('cars.csv', 'rb') as f:
    df = pd.read_csv(f) 

df['Model'].to_csv('model.csv')


# send the model.csv over ftp 

import ftplib
session = ftplib.FTP('server.address.com','USERNAME','PASSWORD')
file = open('model.csv','rb')                  # file to send
session.storbinary('STOR model.csv', file)     # send the file
file.close()                                    # close file and FTP
session.quit()
