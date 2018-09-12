


# request.urlopen
通过urllib打开网页
```
from url import requeset
pattern = re.compile('<tt>(\d+_\d+-\d+)/</tt>')       #设置re正则表达式过滤的规则
f = request.urlopen('http://172.21.111.41:8080/utopia/daily_builds/')
for line in f.readlines():                             #可以通过readlines()一行行读出来
    if time.strftime('%Y%m%d') in line.decode():       #get到的html需要decode以后才能操作
    
        dailyName = pattern.findall(line.decode())[0]   # 利用pattern.findall()过滤想要的东西
        print(dailyName)
        break
```

# request.urlretrieve()
通过此方法下载网页中的可下载文件
request.urlretrieve(url, filename)


# urllib.parse.quote(question)

将字符串转化为url能识别的字符串格式
```
question = "我是谁"
webbrowser.open('https://baidu.com/s?wd=' + urllib.parse.quote(question))


>>>print(urllib.parse.quote('我是谁'))
%E6%88%91%E6%98%AF%E8%B0%81
```
