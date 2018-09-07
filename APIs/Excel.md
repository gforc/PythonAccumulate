
# read excel files
xlrd 可以在任意平台上读取的excel为： .xls以及 .xlsx.
```
import xlrd
```

# write excel files
xlwt支持的excel版本是： Microsoft excel版本 95---2003，也就是 xls文件
```
import xlwd
```
# write existed excel files
如果需要在 xlrd以及 xlwt之间进行交互的话，比如拷贝 xlrd 到 xlwt 需要用到xlutils
目前提供了 copy、display、filter、margins、Save、styles几个函数。
```
from xlutils.copy import copy
rb = xlrd.open_workbook(r"NewCreateWorkbook.xls")
wb = copy(rb)
ws = wb.get_sheet(0)
```

# check wether the files existed

```
import os
path = 'files_path'
check_exsited = os.path.existed(path)
```
