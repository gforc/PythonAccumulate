# -*- coding:UTF-8 -*-

'''
Created on Nov 17, 2016

@author: evanli
'''

#from /Library/Python/2.7/site-packages/MySQL_python-1.2.5-py2.7-macosx-10.10-intel.egg 
import MySQLdb
import time


class mysqlConnection:



    def __init__(self):
        self.conn = None
        self.cur = None
        self.fileName = "/Users/evanli/Documents/Program/Python/python/GrapWeb/grap/log/mysqlCommand_" + time.strftime('%Y_%m_%d') + ".txt"
        self.input_file = open(self.fileName, "w+")
       
    def establishConnection(self,host,user,passwd,dbname,port):
        
        self.conn = MySQLdb.connect(host = host, user = user, passwd = passwd, port = port,charset='utf8')
        self.cur = self.conn.cursor()
 
        try:
            self.cur.execute('create database %s' % dbname)
        except:
            print 'Database %s exists!' % dbname
 
        self.conn.select_db(dbname)
        
        
    def createTable(self,table_name,title_name,title_type,unique_index):

        i = 0
        
        create_table_command = "create table if not exists "
        create_table_command = create_table_command + table_name + "("       
        for title in title_name:
            create_table_command = create_table_command + title + " " +title_type[i] + ", "
            i = i + 1             
        create_table_command = create_table_command[:-2] + ")"
        self.input_file.write(create_table_command +";\n")
        print "create_table_command = %s" %create_table_command

        try :
            self.cur.execute(create_table_command) 
        except:
            print "the table is already exists!"
        
        ### set unique command         
        if not self.cur.execute("show index from %s" % table_name):
            self.cur.execute("alter table %s add unique(%s)" % (table_name,unique_index))
          
        

       
            
    def showInform(self,table_name):
        if self.cur is None:
            self.establishConnection()             
        show_command = "select * from "
        show_command = show_command + table_name          
        num = self.cur.execute(show_command)
#        info = self.cur.fetchmany(num)
        result = self.cur.fetchall()
        print "total entry in table %s is %s" %(table_name,num)
        for ii in result:
            print ii
#            print ii[0],ii[1],ii[2],ii[3]

##############################################################################
        # the variable "inform_list" is like this :
        #slt10_lotus = ["11","srx5400","6L","3year"]
        #slt10_peony = ["22","srx5400","6L","3year"]
        #slt41_seal = ["33","srx5400","6L","3year"]
        #inform_list = [slt10_lotus,slt10_peony,slt41_seal]
##############################################################################            
    def insetinform_listInlist(self,table_name,inform_list):
        if self.cur is None:
            self.establishConnection()      
        for name in inform_list:
            insert_command = "insert into " + table_name + " values("
            for inform in name:
                insert_command = insert_command + "'" +inform + "'" + ","           
            insert_command = insert_command[:-1] + ")"    
            self.input_file.write(insert_command +";\n")
            print "insert_command = %s" %insert_command
            try :
                self.cur.execute(insert_command)
            except :
                print "the inform you want to insert is already exists!"
#        self.cur.execute("insert into student values('2','evanli','3 year 2 class','9')")
            self.conn.commit()
   

##############################################################################
        # the variable "inform_list" is like this :
        #inform_list  = ["11","srx5400","6L","3year"]
##############################################################################
    def insetinform_list(self,table_name,inform):
        if self.cur is None:
            self.establishConnection()      
        
        insert_command = "replace into " + table_name + " values("
        for i in inform:
#            print "insetinform_list = %s"  % i
            insert_command = insert_command + "'" + str(i) + "'" + "," 
        insert_command = insert_command[:-1] + ")"    
        self.input_file.write(insert_command +";\n")
        print "insert_command = %s" %insert_command
        try:
            self.cur.execute(insert_command)
#           self.cur.execute("insert into student values('2','evanli','3 year 2 class','9')")
        except :
            print "the inform you want to insert is already exists!"
             
        self.conn.commit()
    
    
    
   
    def deleteinform(self,table_name,title_element,inform_element):
        if self.cur is None:
            self.establishConnection()
        
        delete_command = "delete from " + table_name + " where " + title_element + "= " + "'" +inform_element + "'"
        print "delete_command = %s" %delete_command
        self.cur.execute(delete_command) 
#        self.cur.execute("delete from student where age='9'")

   

    
    
    def readTabelName(self,database_name):
        execute_command = "use " + database_name 
        self.cur.execute(execute_command)
        
        execute_command = "show tables;"
        self.cur.execute(execute_command)
        
        result = self.cur.fetchall()

#         for items in  result:
#             for item in items :
#                 print item
              
        return result


    def readRowName(self,database_name, tableName):
        execute_command = "use " + database_name 
        self.cur.execute(execute_command)
 
        execute_command = "select column_name from information_schema.columns where table_name=\'" + tableName + "\';"
        self.cur.execute(execute_command)
#        print execute_command
        result = self.cur.fetchall()
        
#         print "###########################################"
#         for items in  result:            
#             for item in items :
#                 print item
#         print "###########################################"

        return result
    
    


    def readAlldate(self,database_name,table_name):
        
        execute_command = "use " + database_name 
        self.cur.execute(execute_command)
        
        execute_command = "select * from " + table_name + " order by date"
        self.cur.execute(execute_command)
        
        result = self.cur.fetchall()
        
#         for items in  result:
#             for item in items :
#                 print item
        
        return result
    
    
    
    def getOneRowData(self,database_name,table_name,row_name):
        
        execute_command = "use " + database_name 
        self.cur.execute(execute_command)
        
        execute_command = "select "+ row_name +" from " + table_name + " order by date"
#         print execute_command
        self.cur.execute(execute_command)
        
        result = self.cur.fetchall()
        
#         for items in  result:
#             for item in items :
#                 print item
        
        return result       
        
        
        
      
    def closeMysqlConnection(self):
        self.cur.close()
        self.conn.close()
        self.input_file.close()
        





#  
# title_type = ["varchar(40)", "varchar(20)","varchar(20)","varchar(20)"]
# title_name = ["date","可售房屋套数","可售房屋面积","其中住宅套数"]
# #title_name = ["date","aa","bb","cc"]
# slt10_lotus = ["2016_11_15","89099","8236836.1400","30424"]
# #slt10_peony = ["22","srx5400","6L","3year"]
# #slt41_seal = ["33","srx5400","6L","3year"]
# #box_name_list = [slt10_lotus,slt10_peony,slt41_seal]
# box_name_list = [slt10_lotus]
# table_name = '可售期房统计'
# #table_name = 'ee'
#  
#  
# aa = mysqlConnection()
# #      
# #  
# aa.establishConnection("localhost", "root", "root", "house", 3306)
# # aa.createTable(table_name,title_name,title_type,"date")
# # aa.insetinform_listInlist(table_name, box_name_list)
# # aa.showInform(table_name)
#  
# # aa.readTabelName("house")
# # for names in aa.readTabelName("house"):  
# #     for name in names:       
# #         aa.readRowName("house", name)       
# #         aa.readAlldate("house","现房项目情况")
#       
# # #aa.closeMysqlConnection()
#  
#  
# aa.getOneRowData("house","现房项目情况","现房项目个数1")



