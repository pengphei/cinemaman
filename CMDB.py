# -*- coding: utf-8 -*-

import sqlite3
import os.path

class CMDB(object):
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
