#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import configparser

def config2json(cfgpath):
    """
    读取配置文件为json
    :param cfgpath: 配置文件路径，eg: config.ini/config.conf/config.cfg
    :return 返回json eg: {"项名":{"选项":"值"}
    """
    _dict = {}
    conf = configparser.ConfigParser()
    conf.read(cfgpath, encoding="utf-8")
    sections = conf.sections()
    for item in sections:
        _dict.setdefault(item,{})
        _dict[item].update(dict(conf.items(item)))
    return _dict



