import string
import getpass
import sys
import telnetlib
import time

HOST = "192.168.100.20"
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("enable\n")
tn.write("123\n")
tn.write("terminal leng 0\n")
while True:
    output= tn.read_very_eager()
    cli= raw_input(output +"")
    tn.write(cli+"\n")
    time.sleep(0.5)
    print output

