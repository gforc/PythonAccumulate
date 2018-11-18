This is unclassified APIs

# ZIP
zip()是Python的一个内建函数，它接受一系列可迭代的对象作为参数，将对象中对应的元素打包成一个个tuple（元组），然后返回由这些tuples组成的list（列表）。
若传入参数的长度不等，则返回list的长度和参数中长度最短的对象相同。利用*号操作符，可以将list unzip（解压）。
```
list1 = [1,2,3,4]
list2 = [5,6,7,8]
print zip(list1,list2) 
#输出结果是   [(1, 5), (2, 6), (3, 7), (4, 8)]
```

```
str1 = "abcd"
str2 = "123456"
print zip(str1,str2)
输出结果是：[('a', '1'), ('b', '2'), ('c', '3'), ('d', '4')]
```

```
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
 print zip(*a)  输出结果是：[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
 ```

# round()
round()方法返回 x 的小数点四舍五入到n个数字。
```
print “round(80.23456, 2) : “, round(80.23456, 2) 
print “round(100.000056, 3) : “, round(100.000056, 3) 
print “round(-100.000056, 3) : “, round(-100.000056, 3) 

#当我们运行上面的程序，它会产生以下结果：
round(80.23456, 2) : 80.23 
round(100.000056, 3) : 100.0 
round(-100.000056, 3) : -100.0
```

# Python collections
https://blog.csdn.net/liufang0001/article/details/54618484
## defaultdict() 
### defaultdict() 与 dict 区别
1. defaultdict()创建字典性能比 dict更高
2. 如果方法字典的value是空时，dict方式创建的字典会抛出KeyError异常的；defaultdict()方式可以利用工厂函数，给初始key带来一个默认值。这个默认值也许是空的list[]  defaultdict(list), 也许是0, defaultdict(int).  
```
mport collections
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# defaultdict
d = collections.defaultdict(list)
for k, v in s:
    d[k].append(v)
# Use dict and setdefault   
g = {}
for k, v in s:
    g.setdefault(k, []).append(v)
      
# Use dict
e = {}
for k, v in s:
    e[k] = v
```

