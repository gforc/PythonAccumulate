#filename telnet_dut
import telnetlib
from matplotlib.cbook import Null
import time



class login_dut:
    
    def __init__(self,host,name,password):
        self.host = host
        self.name = name
        self.password = password
        
        self.telnet = telnetlib.Telnet(self.host)
    
        self.telnet.write("\n\n")
        self.telnet.read_until("login")
        self.telnet.write(name + "\n")
        self.telnet.read_until("Password:")
        self.telnet.write(password + "\n")
        self.telnet.read_until("%")
        self.telnet.write("cli\n")
        self.telnet.read_until("regress")
        self.telnet.write("config\n")
        self.telnet.read_until("regress")
        print "telnet successfully!"

    def input_command_without_commit(self,file):
        print "begin to input command, please wait ..."
        output_file = open(file,'r+')
        input_file = open("result.txt", "a+")
        command = output_file.readline()
        while command != "":
            
            self.telnet.write("commandstart"+"\n") 
            self.telnet.write(command+"\n")         
            command = output_file.readline()


        self.telnet.write("commandfinish\n")   ## end key words  
        input_file.write(self.telnet.read_until("commandfinish"))
        
        output_file.close()
        input_file.close()
        print "finish to input command!"
    
    def close_connect(self):
        self.telnet.close()
        print "telnet connection closed! "
    


#while 1:



#aa = login_dut("10.208.84.45","regress","MaRtInI")
#aa.input_command_without_commit("show_command.cfg")  
#time.sleep(5)
#aa.close_connect()
    
