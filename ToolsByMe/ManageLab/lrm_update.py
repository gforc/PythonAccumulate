'''
Created on Sep 9, 2016

@author: evanli
'''


#! /usr/bin/python
# coding:utf-8
import urllib
import re
import json

class LRM_Resources:
    
    #def __init__(self):
    
    global res_list 
    res_list = []    
    
    def chk_res_with_domain(self,domain_name):
        
        domain_res = urllib.urlopen("http://inception.juniper.net/lrm/core/resource/search.json?domain_name=%s&is_active=true" %domain_name).read()
        json_res = json.loads(domain_res)
        num_rows = json_res[u"num_rows"]
        
        for i in range(num_rows):
            res_list.append(json_res[u"rows"][i][u"name"])
        print res_list
            
        
        
    def chk_res_with_name(self,name):
        
        #get name,model,mgt ip,rack,elevation
        lrm_url = urllib.urlopen("http://inception.juniper.net/lrm/core/resource/search.json?name=%s&is_active=true&_chassis_and_interface" %name).read()
        json_lrm = json.loads(lrm_url)
        
        
        #create dict
        keys = ('name','model','mgt','rack','elevation','reserved_by')
        dict = {}.fromkeys(keys)
        
        #add value to dict
        dict['name'] = json_lrm[u"rows"][0][u"name"]
        dict['rack'] = json_lrm[u"rows"][0][u"rack"]
        dict['elevation'] = int(json_lrm[u"rows"][0][u"elevation"])
        dict['model'] = json_lrm[u"rows"][0][u"model"]
        dict['mgt'] = json_lrm[u"rows"][0][u"mgt_ip_address"]
        
        dict_reservation = json_lrm[u"rows"][0][u"reservation"]
        
        if 'by_user' in dict_reservation.keys():
            dict['reserved_by'] = json_lrm[u"rows"][0][u"reservation"][u"by_user"]
        else:
            dict['reserved_by'] = 'Null'
        

        for key in dict.keys():
            print key + ' : ' + str(dict[key])
        
    
        
    def chk_card_with_SN(self,sn):
        
        lrm_url = urllib.urlopen("http://inception.juniper.net/lrm/core/component/search.json?serial_number=%s&_flat&" %sn).read()
        json_lrm = json.loads(lrm_url)
        #print json_lrm
        #create dict
        keys = ('chassis','model','label','chassis_rack')
        dict = {}.fromkeys(keys)
        
        #add value to dict
        dict['chassis'] = json_lrm[u"rows"][0][u"chassis_resource_name"][0]
        dict['model'] = json_lrm[u"rows"][0][u"model"]
        dict['label'] = json_lrm[u"rows"][0][u"label"]
        dict['chassis_rack'] = json_lrm[u"rows"][0][u"chassis_rack"]

        #print dict
        for key in dict.keys():
            print key + ' : ' + str(dict[key])

    def chk_chassis_with_SN(self,sn):
        
        lrm_url = urllib.urlopen("https://inception.juniper.net/lrm/core/chassis/search.json?serial_number=%s&_hierarchical" %sn).read()
        json_lrm = json.loads(lrm_url)
        
        keys = ('chassis','model','rack','elevation')
        dict = {}.fromkeys(keys)
        
        dict['chassis'] = json_lrm[u"rows"][0][u"chassis_resource"][0][u"resource"][u"name"]
        dict['model'] = json_lrm[u"rows"][0][u"chassis_model"][u"name"]
        dict['rack'] = json_lrm[u"rows"][0][u"chassis_rack"][u"name"]
        dict['elevation'] = json_lrm[u"rows"][0][u"elevation"]
        
        #print dict
        for key in dict.keys():
            print key + ' : ' + str(dict[key])
    
    
    def chk_res_with_IP(self,ip):

        lrm_url = urllib.urlopen("https://inception.juniper.net/lrm/core/resource/search.json?management_ip=%s" %ip).read()
        json_lrm = json.loads(lrm_url)
        
        chassis_name = json_lrm[u"rows"][0][u"name"]
        self.chk_res_with_name(chassis_name)
        
        
    def chk_res_interface(self,name):
        
        lrm_url = urllib.urlopen("https://inception.juniper.net/lrm/core/logical_interface/search.json?resource_name=%s&_flat&" %name).read()
        json_lrm = json.loads(lrm_url)

        local_int = []
        remote_int = []
        dict_int = {}
        
        for logical_int in json_lrm[u"rows"]:
            
            #put local int in list local_int
            local_int.append(logical_int['name'])
            #put remote int in list remote_int
            remote_int.append(logical_int['switch'])
            

        #generate dict for interfaces   
        dict_int = dict(map(lambda x,y:[x,y],local_int,remote_int))
        print dict_int
        
    def chk_specific_interface(self,name,interface):
        
        lrm_url = urllib.urlopen("https://inception.juniper.net/lrm/core/logical_interface/search.json?resource_name=%s&_flat&" %name).read()
        json_lrm = json.loads(lrm_url)

        local_int = []
        remote_int = []
        dict_int = {}
        
        for logical_int in json_lrm[u"rows"]:
            
            #put local int in list local_int
            local_int.append(logical_int['name'])
            #put remote int in list remote_int
            remote_int.append(logical_int['switch'])
            

        #generate dict for interfaces   
        dict_int = dict(map(lambda x,y:[x,y],local_int,remote_int))
        print interface +' : '+dict_int[interface]

    def write_to_mysql(self):
        
        self.chk_res_with_domain('pdt-regression')
        list_two = res_list[0:3]
        print list_two
        
        for device in list_two:
            
            self.chk_res_with_name(device)
            self.chk_res_interface(device)

    def write_mysql(self, box_inform,):
        
        database_table_name = "lab"
        database = mysqlConnection()
        ## must create "test" database in mysql by mannal
        database.establishConnection("localhost", "root", "root", "test", 3306)
       
       
        inform = {}
        inform_key = []
        table_item_type = []      
        for device in list_two:
            inform = self.chk_res_with_name(device)
#            print inform
            ##get database table items title
            if not inform_key :
                inform_key = inform.keys()
                ## set database table item type, "name" is unique index
                for i in range(0,len(inform_key)):
                    table_item_type.append("varchar(32)")
                database.createTable(database_table_name,inform_key,table_item_type,"name")
             
            ##get database table items value   
            inform_value = []
            for i in inform_key :
                
                inform_value.append(inform.get(i))
                
#            print inform_key    
#            print inform_value
                
            database.insetinform_list(database_table_name,inform_value)
           

        database.showInform(database_table_name)
        database.closeMysqlConnection()

       
       
       
       
       
     
a = LRM_Resources()
a.write_to_mysql()

#a.chk_res_interface('slt104-banana')

#a.chk_res_with_SN('CAAB1461')


    
