# superl-url
<<<<<<< HEAD
##### 根据关键词，对搜索引擎内容检索结果的网址内容进行采集的一款轻量级软程序(支持中文)。
=======
##### 根据关键词，对搜索引擎内容检索结果的网址内容进行采集的一款轻量级软程序。
>>>>>>> aa9e5e0d2df099c57769e3ba3c0357d7b16cb5d6
##### 程序主要运用于安全渗透测试项目，以及批量评估各类CMS系统0DAY的影响程度，同时也是批量采集自己获取感兴趣的网站的一个小程序~~
##### 可自动从搜索引擎采集相关网站的真实地址与标题等信息，可保存为文件，自动去除重复URL。同时，也可以自定义忽略多条域名。

# 当前版本
<<<<<<< HEAD
##### Version 2.1.0
=======
##### Version 2.0
>>>>>>> aa9e5e0d2df099c57769e3ba3c0357d7b16cb5d6
  
# 更新说明
##### 2.0新版，对程序进行了重写升级，采用模块化开发，方便后期的扩展；
##### 2.0新版，内置的搜索引擎增加。包括百度，搜狗，360搜索（新增加支持的搜索引擎比较容易）；
##### 2.0新版，增加了配置文件，无需更改代码即可自定义。方便新手使用；


# 使用效果
<<<<<<< HEAD
测试环境系统为Mac Pro 10.12
测试环境python版本为2.7
如果提示模块不存在，则根据提示进行安装！
一般没有安装tld模块，使用 pip install tld 进行安装。或者官网下载(https://pypi.python.org/pypi/tld/0.7.6)
如果使用遇到问题，可以在博客页面评论留言。
=======
测试环境为Mac Pro 10.12
>>>>>>> aa9e5e0d2df099c57769e3ba3c0357d7b16cb5d6

![image](https://github.com/super-l/search-url/blob/master/run1.png)
![image](https://github.com/super-l/search-url/blob/master/run2.png)

# 联系方式

##### 作者博客:http://www.superl.org/post-searchurl.html

##### QQ:86717375    QQ群：199688491


# 使用说明

* 为了防止采集过快导致封IP之类的事情，程序已经设置了延迟时间。建议不要追求速度，免得换IP。

* 2.0版本的文件为superl-url.py，如果需要使用老版本的，则运行search-url-old.py

* 测试环境为Python2.7.x，如果需要python3版本的，可以自行修改，或者博客(http://www.superl.org)留言

* 如果要采集关键词为“hacker”的相关网站，采集搜索结果的前3页，则输入如下：

  * please input keyword:hacker

  * Search Number of pages:3
  
* 配置文件说明
  * [global]
  * savefile = True    ;是否保存文件
  * sleeptime = 30      ;延迟30秒

  * [filter]
  * filter_urlparam = True ;是否去除URL参数
  * filter_url = True      ;是否过滤网址
  * filter_title = True    ;是否过滤标题

  * [log]
  * write_title = True    ;是否把标题也写入日志文件
  * write_name = True     ;是否把搜索引擎名称也写入日志文件

  * [search]
  * baidu_search = True    ;是否开启百度搜索
  * sougou_search = True   ;是否开启搜狗搜索
  * so_search = True       ;是否开启360搜索
  * baidu_page_size = 50   ;百度结果每页显示50条
  * sougou_page_size = 50  ;搜狗结果每页显示50条

# 程序特点

* 支持同时采集多个搜索引擎(已内置了百度，搜狗，360),结构模块化，很方便进行扩展，可以无限添加。

* 获取到的是搜索引擎的搜索结果的真实URL地址

* 可以忽略不需要的常见网站，如忽略百度翻译，等等所有百度相关结果，给数组添加baidu.com即可。程序已经默认忽略了很多条，也支持根据自己的需求进行自定义。如

  filter_array1 = ['baidu.com','sina.com.cn','sohu.com','taobao.com','douban.com','163.com','tianya.cn','qq.com','1688.com']

  filter_array2 = ['ganji.com','58.com','baixing.com']

  filter_array3 = ['zhihu.com','weibo.com','iqiyi.com','kugou.com','51.com','youku.com','soku.com','acfun.cn','verycd.com']

  filter_array4 = ['google.cn','youdao.com','iciba.com','cdict.net']

  filter_array5 = ['pconline.com.cn','zcool.com.cn','csdn.net','lofter.com']
  
* 实时显示采集到的网页的【真实URL】以及【标题】。前面的【ID】对应的是当前页百度结果的第X条数据

* 可以自定义采集返回的是详细URL，或者只采集返回域名

* 自动保存结果到当前目录的txt文件，文件名为搜索的 关键词.txt 

* 为了方便导入到其他工具，txt文件里面只记录了采集的网址。当然也可以自定义加入。如果需要同时记录标题，把代码中的注释删除即可

* 自动去除重复记录

* 统计总采集条数（143 found），有效的条数（91 checked），被过滤的条数（52 filter），以及被过滤的重复的URL条数（9 delete）

* 开源免费使用，甚至可以根据自己的需求进行修改，只须保留版权信息。

* 跨平台，并且无捆绑后门风险，更新方便。网上大部分URL采集软件为WINDOWS下的可执行文件，并且很多都在百度更新后无法正常使用。

* 程序会不断更新，根据搜索引擎规则的调整而调整，同时也会增加运行效率与代码质量，功能等。


# 关于反馈

##### 如果搜索引擎规则改变，导致采集不到内容，可以[我的博客发布页](http://www.superl.org/post-searchurl.html)留言联系我进行修改。


# 定制优化

##### 需要多功能的可以联系我定制加强版。

