import ctypes
import json
library = ctypes.cdll.LoadLibrary('./bindings/library.so')

def Ping():
    farewell = library.ping
    farewell.restype = ctypes.c_void_p
    farewell_output = farewell()

    
    farewell_bytes = ctypes.string_at(farewell_output)

    
    farewell_string = farewell_bytes.decode('utf-8')
    print(farewell_string)

def apInstall(name:str,file:str,icon:str,version:str):
    
    print("on AP funtion ",name,file,icon,version,"\n")

    print("_-"*10,"GO LANG CODE","-_"*10,"\n")

    goapinstall = library.apinstall
    goapinstall.argtypes = [ctypes.c_char_p]
    goapinstall(name.encode('utf-8'),file.encode('utf-8'),icon.encode('utf-8'),version.encode('utf-8'))

def apList():
    
    APlist = library.aplist
    APlist.restype = ctypes.c_char_p
    json_data = APlist()
    json_data = json.loads(json_data.decode('utf-8'))
    return json_data

def apRemove(id):
    
    goapRemove = library.apremove
    goapRemove.argtypes = [ctypes.c_char_p]
    goapRemove(id.encode('utf-8'))

def apUpdate():
    library.apupdate()

