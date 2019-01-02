#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module read config info

Author:linming(linming@ztgame.com)
Date: 2016/11/20
"""

import ConfigParser
import logging

class Config(object):
    """
    param:
         direct:conf配置文件路径
         confname:conf参数名
         conflist:conf参数list
    """
    def __init__(self, direct, confname, conflist):
        """
        init the config

        Args:
            direct: The config file name
            confname: The config name
            conflist: The config key list
        Returns:
            None
        """
        super(Config, self).__init__()
        self.direct = direct
        self.confname = confname
        self.conflist = conflist

    def get_conf(self):
        """
        get config from the file
        
        Args:
            self
        Returns:
            confs
        """
        cf = ConfigParser.ConfigParser()
        try:
            cf.read(self.direct)
        except IOError as e:
            logging.fatal("conf file is not exist %s [%s]" % (self.direct, str(e)))
        conf = {}
        for key in self.conflist:
            try:
                conf[key] = cf.get(self.confname, key)
            except Exception as e:
                logging.fatal("key is not exist %s [%s]" % (key, str(e)))
        return conf