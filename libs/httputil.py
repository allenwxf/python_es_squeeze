#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
This module is http Util
Authors: linming(linming@ztgame.com)
Date   : 2017/07/25
"""

import httplib
import urllib
import sys
import logging

sys.path.append("./libs")
from timeoutexception import timelimited

class HttpUtil(object):
    def __init__(self, master, master_port, slave, 
                 slave_port, interface, timeout, sendinfo, ):
        """
        init
        """
        super(HttpUtil, self).__init__()
        self.master = master
        self.master_port = master_port
        self.interface = interface
        self.timeout = timeout
        self.sendinfo = sendinfo
        self.slave = slave
        self.slave_port = slave_port
    
    @timelimited(60)
    def post(self):
        """
        http post
        """
        httpClient = None
        try:
            params = str(self.sendinfo)
            headers = { "Content-type":"application/x-www-form-urlencoded", \
                        "Accept":"text/plain"}
            httpClient = httplib.HTTPConnection(self.master, self.master_port, self.timeout)
            try:
                httpClient.request("POST", self.interface, params, headers)
                response = httpClient.getresponse()
            except Exception:
                logging.fatal(self.master + " Master connection time out")
                httpClient = httplib.HTTPConnection(self.slave, self.slave_port, self.timeout)
                httpClient.request("POST", self.interface, params, headers)
                response = httpClient.getresponse()
            # print response.status
            # print response.reason
            # print response.read()
            # print response.getheaders()
        except Exception:
            logging.fatal(self.slave + " Slave connection time out")
        finally:
            if httpClient:
                httpClient.close()
