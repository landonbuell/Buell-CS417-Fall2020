"""
Landon Buell
29 october 2020
"""

import numpy as np
import os
import sys
import zipfile

if __name__ == "__main__":

    zipPath = "C:\\Users\\Landon\\Documents\\GitHub\\Buell-CS417-Fall2020\\Lab14\\Lab14\\archive.zip"
    txtPath = "C:\\Users\\Landon\\Documents\\GitHub\\Buell-CS417-Fall2020\\Lab14\\Lab14\\archiveTXT.txt"

    fileData = np.loadtxt(txtPath,comments='b"',encoding='utf-8')


    Zip = zipfile.ZipFile(zipPath,mode='r')
    


    print("=)")
