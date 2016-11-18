#-*- coding: utf-8 -*-
import ConfigParser

class Config(object):
    def __init__(self):
        conf = ConfigParser.ConfigParser()  #生成config对象
        conf.read('config.cfg')  #用config对象读取配置文件
        self.conf = conf

    def __getattr__(self, attr):
        return Child_config(attr, self.conf)


class Child_config(object):
    # for get config
    def __init__(self, attr, cf):
        self.conf = cf
        self.attr = attr

    def __getattr__(self, attr):
        return self.conf.get(self.attr, attr)


class TestBase(object):

    def get_name(self, cls):
        # you can get the class name
        return cls.__class__.__name__


class Volumes(TestBase):
    pass

class Snapshots(TestBase):
    pass

