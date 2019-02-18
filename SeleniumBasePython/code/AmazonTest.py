# -*- coding: utf-8 -*-
'''
Created on Nov 3, 2018

@author: evanli
'''


from selenium import webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
from time import sleep

class PurchaseBookAtAmazonWebsite(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome("/Users/evanli/eclipse-workspace/chromedriver")
        self.target_url = 'https://www.amazon.cn/'
        self.keyword_book = '软件测试'
        self.target_book = '软件测试(原书第2版)'
        self.price = '20.40'
        
        print('test start')
    
        
    def T001_loginWebAndSearch(self):
        #open web site
        self.driver.get(self.target_url)
        sleep(1)
        #search book
        self.driver.find_element_by_id('twotabsearchtextbox').clear()
        self.driver.find_element_by_id('twotabsearchtextbox').send_keys(self.keyword_book)
        self.driver.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input').click()
        
        sleep(2)
        #check whether search book successfully
        self.assertEqual(self.driver.title, self.keyword_book +' - 所有类别 - 亚马逊', 'search book fail!')
        print('open amazon web and search book successfully!')
        
        #whether open new windows
        self.isNewestWindows()
    
    
    def T002_SelectSearchResult(self):          
        #check whether search result has the book we want
        for element in self.driver.find_elements_by_xpath('//ul/li/div/div[3]/div[1]/a'):
            if element.get_attribute("title") == self.target_book:               
                element.click()
                sleep(1)
                print('the book appears in the search result')
                self.isNewestWindows()
                return True
            else:
                print('there is no wanted book in search result! ')
                return False
    
            
    def T003_AddBookIntoShoppingCart(self):    
        #add book to shopping cart
        self.driver.find_element_by_xpath('//input[@id="add-to-cart-button"]').click()
        self.isNewestWindows()
        
        #get keyword and price
        result = self.driver.find_element_by_xpath('//*[@id="huc-v2-order-row-confirm-text"]/h1').text
        price_amozon = self.driver.find_element_by_xpath('//*[@id="hlb-subcart"]/div[1]/span/span[2]').text
        
        #check keyword and price
        self.assertEqual(result,"商品已加⼊入购物⻋车",'the book do not add shop cart successfully!')
        print("the book add shop cart successfully")
        self.assertEqual(price_amozon, self.price,"the price of book is not 20.40!")
        print('the price of the book is ' + self.price)
    
    
    @classmethod                                
    def tearDownClass(self):
        self.driver.quit()
        print('test end')
        
       
    #keep control the newest windows 
    def isNewestWindows(self):
        self.driver.switch_to_window(self.driver.window_handles[-1]) 
           
         
'''   
if __name__ == '__main__' :
    testunit = unittest.TestSuite()
    testunit.addTest(PurchaseBookAtAmazonWebsite("T001_loginWebAndSearch"))
    testunit.addTest(PurchaseBookAtAmazonWebsite("T002_SelectSearchResult"))
    testunit.addTest(PurchaseBookAtAmazonWebsite("T003_AddBookIntoShoppingCart"))   
    
    
    runner = unittest.TextTestRunner()
    runner.run(testunit)
        
'''        
if __name__ == '__main__' :
    #add test case to test suite
    testunit = unittest.TestSuite()
    testunit.addTest(PurchaseBookAtAmazonWebsite("T001_loginWebAndSearch"))
    testunit.addTest(PurchaseBookAtAmazonWebsite("T002_SelectSearchResult"))
    testunit.addTest(PurchaseBookAtAmazonWebsite("T003_AddBookIntoShoppingCart"))   
    #creat test report  
    report = open('./result.html','wb')
    runner = HTMLTestRunner(stream = report, title = 'Purchase book at Amazon website', description = 'test case report')
   
    #run test suite
    runner.run(testunit)
  
    report.close()

