import os
import sys
import shutil
import requests
import logging



HOME=os.path.expanduser('~')
huddle_path=HOME+'/Desktop/Materials_Data_Curation_Huddle'
desktop_path=HOME+'/Desktop'
xsd_path=HOME+'/Desktop/huddle_xsd'

def makeMyDirs(folder_path):
    """ Take a list of folder names and make folders inside of a path """
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        logging.debug("CREATED: " +folder_path)





def get_files(path,ext=('.xsd')):
    """ gets all file files recursively that has a certain extenstion"""
    file_list=[]
    for root,dirs,files in os.walk(path):
        for f in files:
              if f.endswith(ext):
                  file_list.append(os.path.join(root,f))
    #returns list of all files with path
    return file_list

def template_upload(filePath, mdcsUser='admin', mdcsPass='admin' ):
    """ uploads an xsd template """
    schema_data= "" #some string of loaded xsd
    #TODO: finish payload
    #TODO establish title as none type
    payload = {"content" : [ schema_data], 
               "filename" : [ '%s'], 
               "hash":["unknown"], 
               "title":["%s"] } % ('s')


def type_upload(filePath, mdcsUser='admin', mdcsPass='admin' ):
    """ uploads an xsd template """
    schema_data= "" #some string of loaded xsd
    #TODO: finish payload
    #TODO establish title as none type
    payload = {"content" : [ schema_data], 
               "filename" : [ '%s'], 
               "hash":["unknown"], 
               "title":["%s"] } % ('s')


def main():
    urlIP='127.0.0.1:8000'
    


    list_xsd_filePaths=get_files(huddle_path)
    for file_path in list_xsd_filePaths:
        shutil.copy(file_path,xsd_path)
    


if __name__=="__main__":
    main()
