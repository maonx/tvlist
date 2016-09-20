# tvlist

tvlist 是一个用来获取电视剧集网页链接的脚本，配合 [you-get](https://github.com/soimort/you-get) 可以下载免费剧集的部分或全部剧集。

# 支持网站

  Sohu 搜狐网
  
# 如何使用

### 运行程序所需要的第三方库：
 * requests  

### 1. 选择你想获取的一个剧集播放页面或剧集页面， `-i` 选项可以显示简单的信息：  

```
$ tvlist.py -i http://tv.sohu.com/20160907/n467893374.shtml 
亲爱的，公主病(14/16集)
非会员周四五1集，会员周四2集
可免费下载 12 集
```

### 2. 获取剧集全部播放链接地址： 

```
$ tvlist.py http://tv.sohu.com/20160907/n467893374.shtml 
```

### 3. 获取剧集5-8集播放链接地址，选项 `-s N` 为开始下载的集数，选项 `-e N` 为结束下载的集数： 

```
$ tvlist.py http://tv.sohu.com/20160907/n467893374.shtml -s 5 -e 8
```

### 4. 获取剧集最新2集播放链接地址，若开始数为负数，则为倒数的集数开始： 

```
$ tvlist.py http://tv.sohu.com/20160907/n467893374.shtml -s -2
```
