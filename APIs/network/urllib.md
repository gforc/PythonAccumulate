


# request.urlopen
通过urllib打开网页
```
from url import requeset
pattern = re.compile('<tt>(\d+_\d+-\d+)/</tt>')      
f = request.urlopen('http://172.21.111.41:8080/utopia/daily_builds/')
for line in f.readlines():
    if time.strftime('%Y%m%d') in line.decode():
    
        dailyName = pattern.findall(line.decode())[0]
        print(dailyName)
        break
```

# urllib.parse.quote(question)

将字符串转化为url能识别的字符串格式
```
question = "我是谁"
webbrowser.open('https://baidu.com/s?wd=' + urllib.parse.quote(question))


>>>print(urllib.parse.quote('我是谁'))
%E6%88%91%E6%98%AF%E8%B0%81
```
