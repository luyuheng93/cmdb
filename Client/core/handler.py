# -*- coding:utf-8 -*- 
__author__ = 'LYH'

import json
import time
import urllib.parse
import urllib.request
from core import info_collection
from conf import settings

class ArgvHandler(object):

    def __init__(self, args):
        self.args = args
        self.parse_args()

    def parse_args(self):
        """分析参数"""

