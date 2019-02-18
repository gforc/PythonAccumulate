


#!/usr/bin/python

import os
from _ctypes import Array
from warnings import catch_warnings


inputFilenName = raw_input("please input your source-file:") 
outputFileName = raw_input("please input your target-file:") 
flagInactive = 0
c = []
b = []
a = []
i = 0
outputFile = open(outputFileName,'w+')


for line in open(inputFilenName,'r'):

    if line.strip():
        if line[0] == '#' :     # ignore # line 
            continue      
        if line.find('#') != -1:   # delete '#' after cli       
            line = line.split("##")[0]     

        if line.find('{') != -1 & line.find('${node}') == -1 :     
            if line.find ('inactive:') != -1:
                a.append(line.strip().replace(" {", "").replace("inactive:",""))
                flagInactive = 1                                             
            else:
                a.append(line.strip().replace(" {", ""))  
        if line.find(';') != -1:
            line = line.replace(";","")   #remove ';'               
            if line.find('[') != -1 & line.find('version') == -1:
                b =line.strip().split()
                i = 0
                c = []
                while b[i] != '[' :
                    c.append(b[i]+ " ")
                    i+=1                
                for i in range(len(b)-b.index('[')-2):   
                    newline =  "set " + ' '.join(a) + " " + ''.join(c)  + ''.join(b[b.index('[') + i+1]) +"\n"
                    outputFile.write(newline)
            elif line.find ('inactive:') != -1:
                newline = "set"+ " " +' '.join(a) +" "+ line.strip().replace("inactive:","").replace(";\n","") +"\n"               
                outputFile.write(newline)        
                flagInactive = 1    
            else:
                newline = "set"+ " " +' '.join(a) +" "+ line.strip().replace(";\n","") +"\n"                       
                outputFile.write(newline)
       
        if flagInactive == 1 :              #deal with the sentence with inactive            
            if line .find('url') != -1:
                newline = "deactivate"+ " " +' '.join(a) + " " + "url" + "\n"  
            else:
                newline = "deactivate"+ " " +' '.join(a) + "\n"           
            outputFile.write(newline)
            flagInactive = 0
                                 
        if line.find('}') != -1:
            if len(a) != 0:               # whether the list is empty 
                a.pop()
            continue
      
      
outputFile.close()  
print "mission complete !"    
    
      
