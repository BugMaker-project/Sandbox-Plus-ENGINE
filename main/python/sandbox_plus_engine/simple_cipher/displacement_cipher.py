# Copyright (c)2020 BugMaker-Project
# An easy cipher way to encode and decode.
import base64
def encode(content:str,password:str="^"):
    #Password Only 1 Letter or a Single.
    if len(password)!=1:
        if password<1:
            password="^"
        else:
            password=password[0]
    result=[]
    for char in content:
        charValue=ord(char)
        charValue+=ord(password)
        charValue=charValue/2
        result.append(str(charValue))
        result.append(";")
    result="".join(result)
    return str(base64.b64encode(bytes(result,encoding="utf-8")),encoding="utf-8")
def decode(content:str,password:str="^"):
    #Password Only 1 Letter or a Single.
    if len(password)!=1:
        if password<1:
            password="^"
        else:
            password=password[0]
    content=str(base64.b64decode(content),encoding="utf-8").split(";")
    content=[char for char in content]
    c=[]
    for char in content:
        if char=="":
            continue
        c.append(char)
    content.clear()
    content=[float(char) for char in c]
    result=[]
    for char in content:
        charValue=int(char*2)
        charValue-=ord(password)
        charValue=chr(charValue)
        result.append(charValue)
    result="".join(result)
    return result