# 程序简介

##### 由于现在时间很有限，如果用的人不多，就不更新和写java版本了。Star数如果达到200就开始写java命令行版本谢谢。

##### 根据关键词，对搜索引擎内容检索结果的网址内容进行采集的一款轻量级软程序(支持中文)。
##### 程序主要运用于安全渗透测试项目，以及批量评估各类CMS系统0DAY的影响程度，同时也是批量采集自己获取感兴趣的网站的一个小程序~~
##### 可自动从搜索引擎采集相关网站的真实地址与标题等信息，可保存为文件，自动去除重复URL。同时，也可以自定义忽略多条域名。

# 升级说明

2019-5-6  开始升级新版。此次升级，主要是修复BUG,提升运行效率，提升兼容性以及降低新手小白的使用难度。


# 程序特色
*  支持同时采集多个搜索引擎(已内置了百度，搜狗，360),结构模块化，很方便进行扩展，可以无限添加。

*  获取到的是搜索引擎的搜索结果的真实URL地址

*  跨平台，采用Python开发，所有代码完整开源.并且无捆绑后门风险，更新方便。网上大部分URL采集软件为WINDOWS下的可执行文件，并且很多都在搜索引擎更新后无法正常使用。

*  强大的过滤功能。可过滤多种顶级域名，可过滤指定标题中包含某关键子的URL，比如搜索结果中过滤属于youku.com的子域名URL。支持TXT配置过滤。

*  可自动去除重复URL

*  可灵活的通过配置文件自定义要保存的结果格式。比如只输出带参数的原始真实URL，或者只输出域名，或者同时输出标题，搜索引擎名称。

*  可灵活的开启与关闭参与采集的搜索引擎，比如只想使用百度

*  同时兼容python3和python2版本运行！良心开源小产品啊~~~

*  可分别自定义不同搜索引擎每页显示数量(如果搜索引擎自身支持的话)

*  支持多进程同时采集，每个搜索引擎一个进程

*  可自定义每页采集时间间隔，防止被屏蔽

*  实时显示采集到的网页的【真实URL】以及【标题】。前面的【ID】对应的是当前页搜索引擎结果的第X条数据

*  自动保存结果到result目录的txt文件，文件名为搜索的 关键词.txt 

# 当前版本
##### Version 3.0
  
# 更新说明
##### 3.0版，更新如下：
######  1：系统重构，工程目录结构更清晰
######  2：同时兼容Python2和python3
######  3：搜索引擎模块化集成
######  4：代码质量与运行效率优化
######  5：支持不同搜索引擎多进程同时采集
######  6：去重复功能优化
######  7：过滤功能优化，要过滤的域名添加到txt配置文件即可，同时支持过滤标题关键词
######  8：tld包换成了tldextract(截取url的顶级域名用的)
######  9：修复360搜索(so)的采集BUG
######  10：中文采集BUG修复，保存的文件名也同样为中文，方便识别。

##### 2.0版，内置的搜索引擎增加。包括百度，搜狗，360搜索（新增加支持的搜索引擎比较容易）；
##### 1.0版，初始版本，满足个人基本需要；


# 使用效果
##### 测试环境为Mac Pro 10.12
##### 测试环境系统为Mac Pro 10.12
##### 测试环境python版本为2.7
##### 如果提示模块不存在，则根据提示进行安装！
##### 一般没有安装tld模块，使用 pip install tld 进行安装。或者官网下载(https://pypi.python.org/pypi/tld/0.7.6)
##### 如果使用遇到问题，可以在博客页面评论留言。

![image](https://github.com/super-l/search-url/blob/master/run1.png)
![image](https://github.com/super-l/search-url/blob/master/run2.png)

# 安装依赖
##### 如果是python3，则：
###### pip3 install ConfigParser
###### pip3 install tldextract

##### 如果是Python2，则：
###### pip2 install tldextract
###### pip2 install -i https://pypi.tuna.tsinghua.edu.cn/simple configparser


# 联系方式

##### 作者博客:http://www.superl.org/post-searchurl.html

##### QQ:86717375    QQ群：50246933


# 使用说明

* 如果要采集关键词为“hacker”的相关网站，采集搜索结果的前3页，则输入如下：

  * please input keyword:hacker

  * Search Number of pages:3
  
* 配置文件说明 config/setting.conf
* [global]
* savefile = True    是否保存文件
* sleeptime = 0      每页采集间隔X秒
* current_duplicate = False
* end_duplicate = True

* [filter]
* filter_status = True    
* filter_urlparam = True   是否去除URL参数
* filter_url = True        是否过滤域名
* filter_title = True      是否过滤标题

* [log]
* write_title = True       是否把标题也写入日志文件
* write_name = True        是否把搜索引擎名称也写入日志文件

* [search]
* baidu_search = True      是否开启百度搜索
* sougou_search = False    是否开启搜狗搜索
* so_search = True         是否开启360搜索

* [pagesize]
* so = 10                  360搜索结果每页显示10条
* baidu = 50               百度结果每页显示50条
* sougou = 50              搜狗结果每页显示50条

* [mysql]                  导出到Mysql插件(等待后续更新)
* status = False
* ip = 127.0.0.1
* database = superurl
* user = root
* password = root
* table = url
* field = url,title,pr,timestamp

* [plugin]
* pr = True                是否开启域名PR查询功能(等待后续更新)

# 关于反馈

##### 如果搜索引擎规则改变，导致采集不到内容，可以[我的博客发布页](http://www.superl.org/post-searchurl.html)留言联系我进行修改。


# 定制优化

##### 有基础的自己修改吧，随便改，但请保留版权信息。暂时没有时间更新和，也不接定制，有使用问题可以群里问，闲了会回答。

