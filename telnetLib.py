import string
import getpass
import sys
import telnetlib

# Open Telnet by IP, Username + password
def telnet_access(ip,username,password):
    #print ip + username + password
    tn = telnetlib.Telnet(ip) # open connect
    tn.read_until("Username: ")
    tn.write(username + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")
    print tn.read_some() #print to check
    return tn

#save config to File
def save_config(tn,fileNameSave,pass_enable,command):
    tn.write("enable\n")
    tn.write(pass_enable+"\n")
    tn.write("terminal leng 0\n")
    tn.write(command + "\r\n")
    tn.write("\n \n")
    tn.write("exit\n")
    output=tn.read_all()
    print output
    
    fileConfig = open(fileNameSave,"w")
    fileConfig.write(output)
    fileConfig.close()


#main    
save_config(telnet_access("192.168.100.20","quandm","123"),"text.txt","123","show running-config")
