# mylib 

## config_help.py
```
from lib.config_help import config2json

代码:
def config2json(cfgpath):
    """
    读取配置文件为json
    :param cfgpath: 配置文件路径，eg: config.ini/config.conf/config.cfg
    :return 返回json eg: {"项名":{"选项":"值"}
    """
```

## excel_help.py
```
from lib.excel_help import excel2list, excel2json, write_xlsx

代码:
def excel2list(excle_name,**kwargs):
    """
    读取表格为列表
    :param excle_name: excel文件路径
    :param index: 按索引取sheet eg：0
    :param name: 按sheet名称取sheet eg：Sheet1
    :param row_or_col: 按行或列读取sheet，默认按行，eg：True
    :return 返回list eg: [[["a","b","c"],[第1个sheet第2行],[第1个sheet第2行]],[第2个sheet],[...],...]
    """
def excel2json(excle_name):
    """
    读取表格为json
    :param excle_name: excel文件路径
    :return 返回json eg: {"sheet1":[{"表头":第1行}，{"表头":第2行}],"sheet2":[{"表头":第1行}，{"表头":第2行}],...}
    """
def write_xlsx(excle_name, **tables):
    ''''
    写入xlsx文件
    :param excle_name: excel文件路径
    :param sheet: sheet名称与数据
    '''
```
## logs_help.py
```
from lib.logs_help import Logger

代码:
class Logger:
    def __init__(self, set_level="INFO",
                 name=os.path.split(os.path.splitext(sys.argv[0])[0])[-1],
                 log_name=time.strftime("%Y-%m-%d.log", time.localtime()),
                 log_path=os.path.join(log_path, "log"),
                 use_console=True):
        """
        :param set_level: 日志级别["NOTSET"|"DEBUG"|"INFO"|"WARNING"|"ERROR"|"CRITICAL"]，默认为INFO
        :param name: 日志中打印的name，默认为运行程序的name
        :param log_name: 日志文件的名字，默认为当前时间（年-月-日.log）
        :param log_path: 日志文件夹的路径，默认为logger.py同级目录中的log文件夹
        :param use_console: 是否在控制台打印，默认为True
        """
```
## network_help.py
```
from lib.network_help import net2ip

代码:
def net2ip(net_str,_all=False,_error=False):
    """
    拆分网段为IP
    :param net_str: 传入合法网段，eg: 192.168.1.0/24 or 192.168.1.1-33 or 192.168.1.5-192.168.1.8
    :param _all: 是否包含网络地址和广播地址 eg: False
    :param _error: 是否包含无法处理地址 eg: False
    :return 返回list eg [ip1,ip2,...]
    """
```
## sqlite_help.py
```
from lib.sqlite_help import sqliteDB

代码:
class sqliteDB():
    
    def __init__(self,dbnmae,create_table_sql=None):
        """
        初始化函数，创建数据库连接
        :param dbnmae: 传入数据库名称或数据库文件路径，eg: test.db
        :param create_table_sql: 传入的创建表SQL语句,eg:CREATE TABLE tablename (name TEXT NOT NULL);
        """
    def set(self,sql,data=[],many=False):
        """
        数据库的插入、修改、删除函数
        :param sql: 传入的SQL语句 eg:INSERT INTO tablename (name) VALUES (?) / DELETE from tablename where name=? / UPDATE tablename set name = ? where name=?
        :param data: 传入对应数据，many=False:[a,b,c,d] many=True:[[a,b,c,d],[a,b,c,d],[a,b,c,d]]
        :param many: 传入批量数据，many=False
        :return: 返回操作数据库状态 eg: True or False
        """
    def get(self,sql,data=[]): 
        """
        数据库的查询函数
        :param sql: 传入的SQL语句,eg:select * from tablename where name=?
        :param data: 传入查询参数,eg: [name,]
        :return : 返回查询结果 eg: [(a,b,)]
        """
```
## ssh_help.py
```
from lib.ssh_help import SSHManager

代码:
class SSHManager():

    def __init__(self,ip,port,user,passwd):
        """
        初始化函数，创建ssh连接
        :param ip: 传入ip，eg: 127.0.0.1
        :param port: 传入端口 eg: 22
        :param user: 传入用户名 eg: root
        :param passwd: 传入密码 eg: 123456
        """
    def bash(self,cmd):
        """
        执行命令
        :param cmd: 传入命令，eg: whoami
        :return 成功返回执行结果，失败返回False
        """
    def put(self,s_file,d_file):
        """
        上传文件
        :param s_file: 传入要上传的文件，eg: ./test.txt
        :param d_file: 远程位置，eg: /tmp/test.txt
        :return 成功返回True，失败返回False
        """
    def get(self,s_file,d_file):
        """
        下载文件
        :param s_file: 远程文件位置，eg: /tmp/test.txt
        :param d_file: 下载存储位置，eg: ./test.txt
        :return 成功返回True，失败返回False
        """
```

