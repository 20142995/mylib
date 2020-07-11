#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import paramiko
import time


from .logs_help import Logger

logger = Logger("debug",name=os.path.split(os.path.splitext(os.path.abspath(__file__))[0])[-1])

class SSHManager():

    def __init__(self,ip,port,user,passwd):
        """
        初始化函数，创建ssh连接
        :param ip: 传入ip，eg: 127.0.0.1
        :param port: 传入端口 eg: 22
        :param user: 传入用户名 eg: root
        :param passwd: 传入密码 eg: 123456
        """
        self.ip = ip
        self.port = port
        self.user = user
        self.passwd = passwd
        self.transport = None
        self.sftp = None
        self.ssh = None
    
    def connect(self):
        try:
            self.transport = paramiko.Transport((self.ip, int(self.port)))
            self.transport.connect(username=self.user, password=self.passwd)
            self.sftp = paramiko.SFTPClient.from_transport(self.transport)
            logger.info(f"{self.user}@{self.ip}:{self.port}建立sftp连接成功")
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(hostname=self.ip, port=int(self.port), username=self.user, password=self.passwd)
            logger.info(f"{self.user}@{self.ip}:{self.port}建立ssh连接成功")
        except Exception:
            logger.error(f"{self.user}@{self.ip}:{self.port}建立连接失败", exc_info=True)
    def bash(self,cmd):
        """
        执行命令
        :param cmd: 传入命令，eg: whoami
        :return 成功返回执行结果，失败返回False
        """
        try:
            _, stdout, stderr = self.ssh.exec_command(cmd)
            res,err = stdout.read(),stderr.read()
            result = res if res else err
            logger.debug(f"{self.user}@{self.ip}:{self.port}执行{cmd}命令成功：{result}")
            return result.decode()
        except Exception :
            logger.debug(f"{self.user}@{self.ip}:{self.port}执行{cmd}命令失败：{result}")
            return False
    def put(self,s_file,d_file):
        """
        上传文件
        :param s_file: 传入要上传的文件，eg: ./test.txt
        :param d_file: 远程位置，eg: /tmp/test.txt
        :return 成功返回True，失败返回False
        """
        try:
            self.sftp.put(s_file,d_file) 
            logger.info(f"{self.user}@{self.ip}:{self.port}上传{s_file}->{d_file}成功")
            return True
        except Exception:
            logger.info(f"{self.user}@{self.ip}:{self.port}上传{s_file}->{d_file}失败")
    def get(self,s_file,d_file):
        """
        下载文件
        :param s_file: 远程文件位置，eg: /tmp/test.txt
        :param d_file: 下载存储位置，eg: ./test.txt
        :return 成功返回True，失败返回False
        """
        try:
            self.sftp.get(s_file,d_file) 
            logger.info(f"{self.user}@{self.ip}:{self.port}下载{s_file}->{d_file}成功")
            return True
        except Exception:
            logger.info(f"{self.user}@{self.ip}:{self.port}下载{s_file}->{d_file}失败")
            return False

    def close(self):
        if self.transport:
            self.transport.close()
        if self.sftp:
            self.sftp.close()
        if self.ssh:
            self.ssh.close()

    def __del__(self):
        self.close()