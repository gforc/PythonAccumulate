
# setUp() and tearDwon()

setUp和tearDown会在执行每一个def函数的时候都执行一遍；所有当有多个def在一个class种是，setUp和tearDown会执行多遍

修改如下：（会使setUp和tearDown在一个class钟只执行一次）
```
@classmethod
    def setUpClass(self):
    
@classmethod                                
    def tearDownClass(self):
    
```
