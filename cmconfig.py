# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 15:27:50 2014

@author: kurain
"""

import ConfigParser
import os

class CMConfig:
    fcfg = "cmconfig.ini"
    def __init__(self):
        self.config = ConfigParser.ConfigParser()
        return

    def _sample_config(self):
        """ write sample config """
        pass

    def config(self):
        return self.config
