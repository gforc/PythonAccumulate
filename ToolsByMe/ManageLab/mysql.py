'''
Created on Mar 21, 2016

@author: evanli
'''

import MySQLdb




class mysqlConnection:



    def __init__(self):
        self.conn = None
        self.cur = None
       
       
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
        print "create_table_command = %s" %create_table_command

        try :
            self.cur.execute(create_table_command) 
        except:
            print "the table is already exists!"
        

            
        ### set unique command 
        if not self.cur.execute("show index from %s" % table_name):
            self.cur.execute("alter table %s add unique(%s)" % (table_name,unique_index))
          
        
#       self.cur.execute("create table if not exists lab(id int,name varchar(20),class varchar(30),age varchar(10))")    


       
            
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
            print "insert_command = %s" %insert_command
            try :
                self.cur.execute(insert_command)
                self.conn.commit()
            except :
                print "the inform you want to insert is already exists!"
#        self.cur.execute("insert into student values('2','evanli','3 year 2 class','9')")
            
   

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
        print "insert_command = %s" %insert_command
        self.cur.execute(insert_command)
#       self.cur.execute("insert into student values('2','evanli','3 year 2 class','9')")
        self.conn.commit()
    
   
    def deleteinform(self,table_name,title_element,inform_element):
        if self.cur is None:
            self.establishConnection()
        
        delete_command = "delete from " + table_name + " where " + title_element + "= " + "'" +inform_element + "'"
        print "delete_command = %s" %delete_command
        self.cur.execute(delete_command) 
#        self.cur.execute("delete from student where age='9'")

   
    def readAlldate(self,database_name,table_name):
        
        execute_command = "use " + database_name 
        self.cur.execute(execute_command)
        
        execute_command = "select * from " + table_name 
        self.cur.execute(execute_command)
        
        result = self.cur.fetchall()
        
        for items in  result:
            for item in items :
                print item
                
            print "@@@@@@@@@@@@@@@@@@@@@@"
            print "可售房屋套数" 
      
    def closeMysqlConnection(self):
        self.cur.close()
        self.conn.close()
        




#title_type = ["int", "varchar(20)","varchar(20)","varchar(10)"]
#title_name = ["id","name","class","age"]
#slt10_lotus = ["11","srx5400","6L","3year"]
#slt10_peony = ["22","srx5400","6L","3year"]
#slt41_seal = ["33","srx5400","6L","3year"]
#box_name_list = [slt10_lotus,slt10_peony,slt41_seal]
#table_name = 'lab'



#aa = mysqlConnection()
    

#aa.establishConnection("localhost", "root", "root", "test", 3306)
#aa.createTable(table_name,title_name,title_type)
#aa.insetinform(table_name, box_name_list)
#aa.showInform(table_name)
#aa.deleteinform(table_name,"id","11");
#aa.showInform(table_name)
#aa.closeMysqlConnection()



