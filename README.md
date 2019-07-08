
### 程序公告

4.0版本已经升级完成。后续的更新可能只是添加更多的搜索引擎支持了。预计将还要支持如谷歌，必应等。
result目录下面，自带了一个测试搜索python的结果txt.


### 程序简介

+ 根据关键词，对搜索引擎内容检索结果的网址内容进行采集的一款轻量级软程序。
+ 程序主要运用于安全渗透测试项目，以及批量评估各类CMS系统0DAY的影响程度，同时也是批量采集自己获取感兴趣的网站的一个小程序~~
+ 可自动从搜索引擎采集相关网站的真实地址与标题等信息，可保存为文件，自动去除重复URL。同时，也可以自定义忽略多条域名。


### 程序特色
-  支持同时采集多个搜索引擎(已内置了百度，搜狗，360),结构模块化，很方便进行扩展，可以无限添加。
-  获取到的是搜索引擎的搜索结果的真实URL地址
-  跨平台，采用Python开发，所有代码完整开源.并且无捆绑后门风险，更新方便。网上大部分URL采集软件为WINDOWS下的可执行文件，并且很多都在搜索引擎更新后无法正常使用。
-  强大的过滤功能。可过滤多种顶级域名，可过滤指定标题中包含某关键子的URL，比如搜索结果中过滤属于youku.com的子域名URL。支持TXT配置过滤。
-  可自动去除重复URL
-  可灵活的通过配置文件自定义要保存的结果格式。比如只输出带参数的原始真实URL，或者只输出域名，或者同时输出标题，搜索引擎名称。
-  可灵活的开启与关闭参与采集的搜索引擎，比如只想使用百度，就把其他搜索引擎参数设置为False即可。
-  同时兼容python3和python2版本运行！良心开源小产品啊~~~
-  可分别自定义不同搜索引擎每页显示数量(如果搜索引擎自身支持的话)
-  支持多进程同时采集，每个搜索引擎一个进程
-  可自定义每页采集时间间隔，防止被屏蔽
-  实时显示采集到的网页的【真实URL】以及【标题】。前面的【ID】对应的是当前页搜索引擎结果的第X条数据
-  保存类型可自定义，目前支持保存为本地txt，以及写入远程MYSQL数据库！

### 当前版本
- Version 4.0

### 使用效果
- 测试环境1：系统为Mac Pro 10.12  python版本为2.7和python3【测试通过】
- 测试环境2：系统为win7 64位。python版本为2.7 【测试通过】
- 如果发现运行有问题，一般都是操作系统的编码导致的小问题，欢迎截图反馈

![image1](https://github.com/super-l/resource/raw/master/superl-url/images/1.png)
![image2](https://github.com/super-l/resource/raw/master/superl-url/images/2.png)
![image3](https://github.com/super-l/resource/raw/master/superl-url/images/3.png)


### 安装依赖
- 如果是python3，则：

        pip3 install ConfigParser
        
        pip3 install tldextract
        
- 如果是Python2，则：

        pip2 install tldextract
        
        pip2 install -i https://pypi.tuna.tsinghua.edu.cn/simple configparser
        
- 如果提示模块不存在，则根据提示进行安装！
- 一般没有安装tld模块，使用 pip install tld 进行安装。或者官网下载(https://pypi.python.org/pypi/tld/0.7.6)
- 如果使用遇到问题，可以在博客页面评论留言。

### 联系方式

- 作者博客:http://www.superl.org/post-searchurl.html
- QQ:86717375    QQ群：50246933


### 使用说明

- 如果要采集关键词为“hacker”的相关网站，采集搜索结果的前3页，则输入如下：
- please input keyword:hacker
- Search Number of pages:3
  
### 配置文件说明 config.cfg

| 节点 | 参数 | 示例值 | 说明 |
| :------| ------: | :------: |:------: |
| global | save_type | mysql | 保存类型 可选择file或者mysql 如果是file则保存为本地txt |
| global | sleep_time | 1 | 每次搜索处理完一页后的等待时间，防止太频繁被搜索引擎屏蔽 |
| url | url_type | realurl | 保存文件txt里面显示的url类型。realurl=真实网站地址 baseurl=原始搜索引擎地址 urlparam=带参数的真实网站地址 |
| filter | filter_status | True | 是否开启过滤器，如果开启，则过滤域名和标题都不生效 |
| filter | filter_domain | True | 是否过滤域名 |
| filter | filter_title | True | 是否过滤标题 |
| log | write_title | True | 是否显示标题 |
| log | write_name | True | 是否显示搜索引擎名称 |
| engine | baidu | True | 百度搜索引擎模块是否开启 |
| engine | sougou | True | 搜狗模块是否开启 |
| engine | so | False | 搜搜模块是否开启 (搜搜现在抓取不到了) |
| pagesize | baidu_pagesize | 50 | 每页条数 |
| pagesize | sougou_pagesize | 50 | 每页条数 |
| pagesize | so_pagesize | 10 | 每页条数 |
| mysql | host | 127.0.0.1 | 如果保存类型为Mysql，则此节点必须配置正确 |
| mysql | port | 3306 | 端口 |
| mysql | user | root | 用户名|
| mysql | password | root | 密码 |
| mysql | database | superldb | 数据库名称 |
| mysql | table | search_data | 表名称 |
| file | save_pathdir | result | 如果保存类型为file,则这里设置的是保存的路径，当前为程序根目录的result文件夹 |
| plugin | pr | True | 预留的插件功能，暂时不支持 |


### 数据库创建表sql语句

        CREATE TABLE `search_data` (
          `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
          `engine` varchar(20) NOT NULL DEFAULT '',
          `keyword` varchar(100) NOT NULL DEFAULT '',
          `baseurl` varchar(255) NOT NULL DEFAULT '',
          `realurl` varchar(255) NOT NULL DEFAULT '',
          `urlparam` varchar(255) NOT NULL DEFAULT '',
          `webtitle` varchar(255) NOT NULL DEFAULT '',
          `create_time` int(10) NOT NULL,
          PRIMARY KEY (`id`)
        ) ENGINE=MyISAM AUTO_INCREMENT=395 DEFAULT CHARSET=utf8;


### 关于反馈

- 如果搜索引擎规则改变，导致采集不到内容，可以[我的博客发布页](http://www.superl.org/post-searchurl.html)留言联系我进行修改，或者直接在git上issues也可以。


### 定制优化

- 有基础的自己修改吧，随便改，但请保留版权信息。暂时没有时间更新和，也不接定制，有使用问题可以群里问，闲了会回答。


### 4.0版本更新说明

- 系统核心优化，去除和重新封装部分核心类；
- 配置文件优化（更改部分参数的命名以及新增了参数）；
- 更新搜索引擎类(比如，module/baidu/baidu.py)的实现写法更加方便与简洁；
- python2和python3的兼容性优化(目前在本机MAC系统上分别使用py2和py3都可以正常运行，windows没有环境去测试，如有问题欢迎反馈)
- 同时支持保存为本地txt和写入远程Mysql数据库；
- 修复相关异常报错问题;  
  
  
### 3.0版本更新说明
- 系统重构，工程目录结构更清晰
- 同时兼容Python2和python3
- 搜索引擎模块化集成
- 代码质量与运行效率优化
- 支持不同搜索引擎多进程同时采集
- 去重复功能优化
- 过滤功能优化，要过滤的域名添加到txt配置文件即可，同时支持过滤标题关键词
- tld包换成了tldextract(截取url的顶级域名用的)
- 修复360搜索(so)的采集BUG
- 中文采集BUG修复，保存的文件名也同样为中文，方便识别。

### 2.0版本更新说明
- 2.0版，内置的搜索引擎增加。包括百度，搜狗，360搜索（新增加支持的搜索引擎比较容易）；

### 1.0版本更新说明
- 1.0版，初始版本，满足个人基本需要；

