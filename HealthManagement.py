# -*- coding: utf-8 -*-
"""
HEALTH MANAGEMENT SYSTEM
"""

print("HEALTH MANAGEMENT SYSTEM")
client_list={1:'harry',
             2:'rohan',
             3:'hammad'
             }
log_list={1:'exercise',
          2:'diet'
          }
def getdate():
    import datetime
    return datetime.datetime.now()
try:
    print("Select Client name:")
    for key,value in client_list.items():
        print("press",key ,"for",value,"\n",end=" ")
    client_name=int(input())
    print(f"Selected Client is {client_list[client_name]}")
    print("1 for log \n 2 for retrieve ")
    op=int(input())
    if op is 1:
        for key,value in log_list.items():
            print("Press",key,"tolog",value,"\n",end=" ")
        log_name=int(input())
        print(f"Selected job is {log_list[log_name]} ")
        f=open(client_list[client_name]+"_"+log_list[log_name]+".txt","a")
        key='y'
        while(key is not 'n'):
            print("Enter",log_list[log_name])
            mytext=input()
            f.write("["+str(getdate())+"]:"+mytext+"\n")
            key=input("Add more : y/n?")
            continue
        f.close()
    elif op is 2:
        for key,value in log_list.items():
            print("Press",key,"to retrieve",value,"\n",end=" ")
        log_name=int(input())
        print(f"{client_list[client_name]}_{log_list[log_name]} report : ")
        f=open( client_list[client_name]+"_"+log_list[log_name]+".txt","r")
        content=f.readlines()
        for line in content:
           print(line,end="")
            
        f.close()
    else:
       print("INVALID Input")
except Exception as e:
          print("Wrong Input")       
       
                 