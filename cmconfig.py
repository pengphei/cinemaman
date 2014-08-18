# -*- coding: utf-8 -*-

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
