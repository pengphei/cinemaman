# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 15:27:50 2014

@author: kurain
"""

import sqlite3
import os.path

class CMDB:
    path = ""
    conn = None
    def __init__(self, path):
        self.path = path
        return

    def connect(self):
        return self.conn

    def init(self):
        self.conn = sqlite3.connect(self.path)
        return

    def fini(self):
        cursor = self.conn.cursor()
        cursor.close()
        self.conn.close()
        return

# for test
if __name__ == "__main__":
    db = CMDB("test.db")
    db.init()
    dbconn = db.connect()
    db.fini()