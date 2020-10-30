"""
Landon Buell
29 october 2020
"""

import numpy as np
import os
import sys
import zipfile
import string

if __name__ == "__main__":

    zipPath = "C:\\Users\\Landon\\Documents\\GitHub\\Buell-CS417-Fall2020\\Lab14\\Lab14\\archive.zip"
    txtPath = "C:\\Users\\Landon\\Documents\\GitHub\\Buell-CS417-Fall2020\\Lab14\\Lab14\\archiveTXT.txt"
    expPath = "C:\\Users\\Landon\\Documents\\GitHub\\Buell-CS417-Fall2020\\Lab14"

    data = np.fromfile(txtPath,dtype=int,sep="")
    
    file = open(txtPath,mode='r',encoding='Cp437')
    lines = file.readlines()
    file.close()

    """
    lowerCase = list(string.ascii_lowercase)
    upperCase = list(string.ascii_uppercase)

    Zip = zipfile.ZipFile(zipPath,mode='r')

    while True:
        pwdstr = str(np.random.choice(lowerCase,size=8))
        print(pwdstr)
        pwd = bytes(pwdstr,encoding='Cp437')   
        try:
            Zip.extractall(expPath,pwd=pwd)
            print("\t\tPWD:",pwdstr)
        except:
            continue
    """
    print("=)")
