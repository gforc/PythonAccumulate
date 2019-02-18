import sys
import socket
import getopt
import time
from telnet_dut import login_dut

ipaddress = ""
port = 23
username = "regress"
password = "MaRtInI"
command_file = "show_command.cfg"
result_file = "result.txt"



def usage():
    print "easy debug tool"
    print 
    print "Usage: telnet_tool.py -i ip_address"
    print " require : "
    print " -i --ip_address           >>> DUT ip address"
    print " optional : "
    print " -p --port                 >>> telnet server port, default is 23"
    print " -u --username             >>> DUT login name, default is regress"
    print " -p --password             >>> DUT login password, default is MaRtInI"
    print " -c --command_file         >>> the file used to save commands need to input in DUT, default is show_command.cfg"
    print
    print
    print " Examples: "
    print " telnet_tool.py -i 10.208.84.45"
    print " telnet_toll.py -i 10.208.84.45 -p 23 -u root -p Embe1mpls -c show_command.cfg -r result.txt"
    sys.exit(0)
    
def main():  
    global ipaddress 
    global port
    global username
    global password
    global command_file
    global result_file
    
    if not len(sys.argv[1:]):
        usage()
    try:
        opts,args = getopt.getopt(sys.argv[1:],"i:p:u:w:c:",["ip_address","port","username","password","command_file"])
    except getopt.GetoptError as err:
        print str(err)
        usage();
    
    for o,a in opts:
        if o in ("-i","--ip_address") :
            ipaddress = a
        elif o in ("-p","--port"):
            port = a
        elif o in ("-u","--username"):
            username = a 
        elif o in ("-w", "--password"):
            password = a 
        elif o in ("-c","--command_file"):
            command_file = a
        else :
            assert False, "Unhandled Option"
    if not len(ipaddress):
        assert False, "you must point out DUT ip address!"
            
    aa = login_dut(ipaddress,username,password)
    aa.input_command_without_commit(command_file)  
    time.sleep(5)
    aa.close_connect()



 
 
 
main()   
       
