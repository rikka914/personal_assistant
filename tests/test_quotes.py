#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
名言管理模块的单元测试
注意：使用unittest.mock模拟文件操作，避免真实文件读写
"""

import unittest
import sys
import os
from unittest.mock import patch,MagicMock
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'..','src'))
from modules.quotes import  QuoteManager

class TestQuoteManager(unittest.TestCase):
    """
    测试QuoteManager类的核心功能
    使用模拟(mock)技术避免真实文件操作
    """

    def setUp(self):
        #模拟的默认名言数据
        self.mock_default_quotes = [
            {"id":1,"text":"测试名言1","author":"作者A","favorite":True},
            {"id":2,"text":"测试名言2","author":"作者B","favorite":False},
        ]