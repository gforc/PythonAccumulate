
# 等待
实际写selenium code时，一定要注意等待时间。
执行每一条语句时，都要考虑上一条命令执行以后，页面是否已经加在完成，如果没有，需要等待一段实际，再执行第二条命令。
再运行selenium脚本时，如果报错‘没有找到元素’，一种可能是定位元素路径或是名称没有写对；另一种就是页面元素没有加载完成，需要等待一段时间，再执行下一条命令。

##

## className不允许使用复合类名做参数
例如，class="s-result-list s-col-3 s-result-list-hgrid s-height-equalized s-grid-view s-text-condensed"，
要定位这个元素可以只写class的一部分，只能写成driver.find_elements_by_class_name('s-result-item')，如果把整个classname写进参数，会报错。
也就是说，classname的参数不能有空格。

##

# 分级定位
复杂环境可以先定位父级元素，然后再定位子元素，例如parentElement.findElement(By.***)

# ID定位是最快速最准确的
ID定位是最快速最准确的，但实际上需要开发人员的友好配合才能有唯一且确定的id可用，真实环境中往往会出现没有id，id重复或者动态id（extjs和query都是动态id）；若动态id有规律我们还能考虑使用正则表达式，否则只能老老实实另谋出路了。

# 定位数组元素：
实际使用中className和tagName经常被用来定位数组元素,例如driver.findElements(by.tagName(“**”))或driver.findElements(by.className(“**”))

　　例如，打开www.baidu.com，运行List<WebElement> Els= driver.findElements(by.tagName(“a”));看看是不是得到了一个元素数组

# className不允许使用复合类名做参数

   真实环境中元素往往使用复合类名(即多个class用空格分隔)，使用className定位时要注意了，className的参数只能是一个class。
'''  
　　例如，打开http://hao.360.cn/，我们要使用className定位这个元素

<a class="tab-item news" data-page="http://sh.qihoo.com/daohang/index1.html" hidefocus="false"href="./brother.html#!news">新闻头条</a>
'''

　　1）执行driver.findElements(by.className("news")),成功定位到元素

　　2）执行driver.findElements(by.className("tab-item news")),定位失败，报错信息：Compound class names not permitted，意思是不允许使用复合类名称

　　分析：className的参数仅允许是一个class，此处class="tab-item news"是复合类名，直接使用会报错

# linkText与partialLinkText

　　遇到文字链接元素，首先考虑使用linkText定位，那它与partialLinkText有什么区别与特性呐？

　　1) linkText=链接文字，表示精准匹配链接文字；partialLinkText=部分链接文字，表示模糊匹配链接文字。例如定位一下元素
'''  
<a target="_blank" title="" href="http://www.nuomi.com/?cid=bdsywzl">劳动节不劳动，吃喝玩乐5.1元起！</a>
 
'''  
　　　　| driver.findElement(By.linkText("劳动节不劳动，吃喝玩乐5.1元起！"));

　　　　| driver.findElement(By.partialLinkText("吃喝玩乐"));

　　2.都对大小写敏感

 

