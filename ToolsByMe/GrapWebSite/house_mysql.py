# -*- coding:UTF-8 -*-
'''
Created on Nov 17, 2016

@author: evanli
'''
import urllib
import urllib2
import re
import sys
import time
from mysql_grap import mysqlConnection
import types
import matplotlib.pyplot as plt


class BDTB:
 
    def __init__(self,baseUrl): 
        self.baseURL = baseUrl
 
    def getPage(self):
        try:
            url = self.baseURL
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
#            print response.read()
            return response.read().decode('utf-8')
#            return response.read()
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"connect error, the reason:",e.reason
                return None
            
    def getData(self):
        
        
        ## filter need information
        page = self.getPage()
        
        
        ### delete all the node code
        re_note1 = re.compile('<!--.*?</td>' )
        re_note2 = re.compile('<td.*?-->' )
        page = re_note1.sub("", page)
        page = re_note2.sub("", page)

#        pattern = re.compile('<tr bgcolor=.*?><td.*?>(.*?)</td>|<td align=.*?><span.*?>(.*?)</span>'  ,re.S)
        pattern = re.compile('<tr bgcolor=.*?><td.*?>(.*?)</td>|<td align=.*?>(.*?)</td></tr>'  ,re.S)


        result = re.findall(pattern,page)
#         result = page
#         print result
# #######################  debug code  #####################                                       
#         i = 0
#         for items in result:
#             for item in items:
#                 print "result[%d] = %s"  % (i, item)    
#                 i+=1         
# #######################  debug code  #####################    
         
        return result
        
        
        
     ### delete no need data and translate orgDate to an list type
    def dateShaping(self,orgDate):    
        
        shapingDate = []

        ##write list to file, so define code type
        reload(sys)
        sys.setdefaultencoding( "utf-8" )
               
        for item in orgDate:
            for data in item:
                if data != "" :
                    #### reorganize data 
                    re_html = re.compile('<span.*?>.*?</span>')            
                    re_year = re.compile('<span.*?Year.*?>')    
                    re_month = re.compile('<span.*?Month.*?>')
                    re_date = re.compile('<span.*?>')

                    
                    data = re_html.sub("",data)
                    data = re_year.sub("", data)
                    data = re_month.sub("", data)  
                    data = re_date.sub("", data)

                    
                    data = data.replace("(M<sup>2</sup>)","").replace("&nbsp;","").strip("\n").strip()
                    data = data.replace("</span>","").replace("：","").replace(" ","").replace("-","")

                    
                    if data.find("<") == -1 and data != "" and data.find("截止日期") == -1:

                        shapingDate.append(data)
# #######################  debug code  #####################                                       
#         i = 0
#         for item in shapingDate:
#             print "shapingDate[%d] = %s"  % (i, item)    
#             i+=1         
# #######################  debug code  #####################      
        return shapingDate
 
    def writeToMysql(self,sharpingDate):
        
        dataBaseName = ""
        tableName= []
        rowType= ["varchar(40)","varchar(40)","varchar(40)","varchar(40)","varchar(40)","varchar(40)","varchar(40)","varchar(40)","varchar(40)","varchar(40)","varchar(40)"]
        rowName= []
        data = []
        
        
        rowNameCount = 1
        rowNumber = 0
        tableNumber = 0
        dataBaseNameFlag = 0
        tableNameFlag = 1
        rowNameFlag = 0
        dataFlag = 0
        for item in sharpingDate :
            
            if tableNameFlag == 1 :
                re_tableName = re.compile('^\d{8}|^\d{7}|^\d{6}')     
                item = re_tableName.sub("", item)
                tableName.append(item)
                tableNameFlag = 0
                rowNameFlag = 1
                
            elif rowNameFlag == 1 :
                if rowNumber == 0 :
                    rowName.append("date")
               
                rowName.append(item+str(rowNameCount))
                rowNameFlag = 0
                dataFlag = 1
                rowNumber += 1 
                rowNameCount +=1
                 
            elif dataFlag == 1:    
                if rowNumber == 1 :
                    data.append(time.strftime('%Y_%m_%d'))
                                    
                data.append(item)
                rowNameFlag = 1
                dataFlag = 0
                rowNumber += 1 
                
            elif dataBaseNameFlag == 1 :
                dataBaseName = item
                dataBaseNameFlag = 0 
                tableNameFlag = 1 
            
    
                    
            if rowNumber == 20 :
                rowNumber = 0 
                tableNameFlag = 1
                tableNumber += 1
                rowNameCount = 1

                       
            
            if tableNumber >= 8 :
                break
  
# #######################  debug code  #####################
#         print "##############################################"
#         print "dataBaseName = "  + dataBaseName
#         print "##############################################"
#         i = 0
#         for item in tableName:
#             print "tableName[%d] = %s"  % (i, item)    
#             i+=1            
#         print "##############################################"
#         i = 0
#         for item in rowType:
#             print "rowType[%d] = %s"  % (i, item)    
#             i+=1    
#         print "##############################################"
#         i = 0
#         for item in rowName:
#             print "rowName[%d] = %s"  % (i, item)    
#             i+=1    
#         print "##############################################"
#         i = 0
#         for item in data:
#             print "data[%d] = %s"  % (i, item)    
#             i+=1    
# # #######################  debug code  #####################       
    
        aa = mysqlConnection()
            
        aa.establishConnection("localhost", "root", "root", "house", 3306)    
     
        for i in range(0,8) :
            aa.createTable(tableName[i],rowName[(0+i*11):(11+i*11)],rowType,"date")
            aa.insetinform_list(tableName[i], data[(0+i*11):(11+i*11)])       
                    
        aa.closeMysqlConnection()
          
# #######################  debug code  #####################    
#         i = 0
#         num = 0
#         for i in range(0,7) :
#             for j in rowName[(0+i*11):(11+i*11)]:
#              
#                 print "%d =  %s"  %(num,j)
#                 num += 1 
#             num = 0
#######################  debug code  #####################     
    
        
    
    def readDateFromMysql(self): 
        
        rowName =()
        data = ()   
        result =()
        aa = mysqlConnection()
         
        aa.establishConnection("localhost", "root", "root", "house", 3306)    
    
#         dd = "" 
#         i= 0
#         j= 0
#         m = 0
#         n = 0
        for tableName1 in aa.readTabelName("house"):    ###### get tabel name            
#             i += 1
#             m = 0
#             n = 0
#             j = 0
            for tableName2 in tableName1:   
#                 j+= 1
#                 m = 0
#                 n = 0
                rowName = aa.readRowName("house", tableName2)      ###### get row name 
#                 print tableName2
                result = result + tableName1
                
                for rowName1 in rowName:           
#                     m += 1
#                     n = 0
                    result = result +rowName1
                    for rowName2 in rowName1:
#                         n += 1
#                         print "result[%d][%d][%d][%d] =  %s " % (i,j,m,n,rowName2)
                        oneRowdata = aa.getOneRowData("house",tableName2,rowName2)    ######## get one row data
                        result = result + oneRowdata                    
 
                     
#                 data =data +  aa.readAlldate("house",tableName2)   ###### get row data
#                 for data1 in data:
#                     for data2 in data1:
#                         print data2 
        aa.closeMysqlConnection()
        
        
        
        return result
                      
          
        
 


print "begin to grap web, pleast wait .."               
#baseURL = 'http://www.bjjs.gov.cn/tabid/2167/default.aspx'
baseURL = 'http://www.bjjs.gov.cn/bjjs/fwgl/fdcjy/fwjy/index.shtml'

bdtb = BDTB(baseURL)
 
print "begin to get date, please wait ..."
result = bdtb.getData()
    
print "begin to shape date, please wait ..."
shapingdate = bdtb.dateShaping(result)
     
print "begin to write date to mysql, please wait ..."
bdtb.writeToMysql(shapingdate)










 
# print "begin to get date from mysql, please wait ..."
# dateFromMysql = bdtb.readDateFromMysql()

 
# i = 0
# j = 0
# m = 0
# for item1 in dateFromMysql:   
#     if type(item1) is types.UnicodeType:
#         print "result[%d][%d] = %s" %(i,j,item1)
#         j +=1
#     else :
#         for item2 in item1:            
#             print "result[%d][%d] = %s" %(i,j,item2)
#             j+= 1  
#         i+= 1
#         j = 0

# i = 0
# while 1:
#     try :
#         print "########################### dateFromMysql[%s] = %s #################" % (i,dateFromMysql[i])
#         i+= 1
#     except :
#         break




 
 
# x = [1, 2, 3, 4, 50]
# y = [1, 4, 9, 16, 250]
#  
# x = []
# y = []
#  
#  
#  
#  
#  
# for tableNum in range(0,1):
#     fig = plt.figure()
#     ax1 = fig.add_subplot(1,2,1)
#     ax1 = fig.add_subplot(1,2,2)
# #     ax1 = fig.add_subplot(5,2,1)
# #     ax2 = fig.add_subplot(5,2,2)
# #     ax3 = fig.add_subplot(5,2,3)
# #     ax4 = fig.add_subplot(5,2,4)
# #     ax5 = fig.add_subplot(5,2,5)
# #     ax6 = fig.add_subplot(5,2,6)
# #     ax7 = fig.add_subplot(5,2,7)
# #     ax8 = fig.add_subplot(5,2,8)
# #     ax9 = fig.add_subplot(5,2,9)    
# #     ax10 = fig.add_subplot(5,2,10)    
#   
#     for i in range(2,8):
#         x.append(dateFromMysql[i][0].encode("utf-8").replace("_",""))
#         y.append(dateFromMysql[i+7][0].encode("utf-8"))
#     
# # print x
# # print y  
#         
#     ax1.plot(x,y)
#      
#     fig.suptitle('figure title demo', fontsize = 14, fontweight='bold')
#     ax1.set_title("axes title")
#     ax1.set_xlabel("x label")      
#     ax1.set_ylabel("y label")
#     ax1.set_xticklabels(x,rotation=70)    
#    
#     plt.show()

