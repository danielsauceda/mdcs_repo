import os
import sys
import shutil
import requests
import logging


huddle_path='/home/danielsauceda/Desktop/Materials_Data_Curation_Huddle'
desktop_path='/home/danielsauceda/Desktop'
xsd_path='/home/danielsauceda/huddle_xsd'

def get_files(path,ext=('.xsd'):
    """ gets all file files recursively that has a certain extenstion"""
    file_list=[]
    for root,dirs,files in os.walk(path):
        for f in files:
              if f.endswith(ext):
              file_list.append(os.path.join(root,f))
    return file_list
/home/danielsauceda/Desktop/pythons/mdcsScripts_2

os.pat



def main():
    list=get_files(huddle_path)
    for file_path in list:
        shutil.copy(file_path,xsd_path)
    

    requests.



if __name__=="__main__":
    main()
