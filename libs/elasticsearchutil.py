#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
Date   : 2017-06-20
Authors: linming(linming@ztgame.com)
"""

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from elasticsearch import Elasticsearch

class EsConnect(object):
    """
    Class of  EsConnect
    """
    def __init__(self, hostsinfo, index, doc_type, timeout=5000):
        self.hostsinfo = hostsinfo
        self.timeout = timeout
        self._index = index
        self._type = doc_type
        self.es = self._get_connect()

    def _get_connect(self):
        """
        get elasticsearch connect
        args:
        return: es
        """
        try:
            es = Elasticsearch(
                    hosts=self.hostsinfo, 
                    timeout=self.timeout
                    )
        except Exception as e:
            raise e
        return es

    def es_query(self, query, size=1):
        """
        es query
        args:
        return: query result
        """
        try:
            res = self.es.search(
                    index=self._index,
                    doc_type=self._type,
                    body=query,
                    size=size
                    )
        except Exception as e:
            raise e
        return res['hits']['hits']

    def es_insert(self, insert_data):
        """
        es insert data
        args: the type of dict with insert_data
        return: 
        """
        try:
            self.es.index(
                index=self._index, 
                doc_type=self._type, 
                body=insert_data
                )
        except Exception as e:
            raise e

    def es_update(self, id_info, update_info):
        """
        es update data
        args: update_info, id_info
        return:
        """
        try:
            self.es.update(
                index=self._index,
                doc_type=self._type,
                id=id_info,
                body=update_info
                )
        except Exception as e:
            raise e







        
