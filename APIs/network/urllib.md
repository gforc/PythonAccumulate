


# API
## urllib.parse.quote(question)

将字符串转化为url能识别的字符串格式
```
question = "我是谁"
webbrowser.open('https://baidu.com/s?wd=' + urllib.parse.quote(question))


>>>print(urllib.parse.quote('我是谁'))
%E6%88%91%E6%98%AF%E8%B0%81
```
