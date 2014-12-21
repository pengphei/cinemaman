# -*- coding: utf-8 -*-

import sqlite3

class CMHall(object):
    """ 电影院观赏厅 """
    def __init__(self, idx=-1, name='', info=""):
        self.idx = idx
        self.name = name
        self.info = info
        return


class CMDBHall(object):
    """ movie hall in db """
    def __init__(self):
        self._prepare()
        return

    def init(self, conn):
        cursor = conn.cursor()
        cursor.execute(self.CMD_CREATE_TABLE)
        conn.commit()
        return

    def add(self, conn, hall):
        cursor = conn.cursor()
        cursor.execute(self.CMD_ADD, (hall.name, hall.info))
        conn.commit()
        return cursor.lastrowid

    def delete(self, conn, hall):
        cursor = conn.cursor()
        cursor.execute(self.CMD_DEL+str(hall.id))
        conn.commit()
        return

    def edit(self, conn, hall):
        cursor = conn.cursor()
        cursor.execute(self.CMD_EDIT, (hall.name, hall.info, hall.id))
        conn.commit()
        return

    def get_all(self, conn):
        halls = []
        cursor = conn.cursor()
        cursor.execute(self.CMD_ALL)
        for item in cursor.fetchall():
            hall = CMHall(-1, item[1], item[2])
            hall.id = item[0]
            halls.append(hall)
        return halls

    def clear(self, conn):
        pass
        cursor = conn.cursor()
        cursor.execute(self.CMD_CLEAR)
        conn.commit()
        pass

    def _prepare(self):
        self.CMD_CREATE_TABLE = """
        create table if not exists tb_hall(
            id integer primary key autoincrement,
            name text,
            info text
        )
        """

        self.CMD_ADD = """
        insert into tb_hall (id,name,info) values (NULL,?,?)
        """

        self.CMD_DEL = """
        delete from tb_hall where id = 
        """

        self.CMD_EDIT = """
        update tb_hall set name=?, info=? where id = ?
        """

        self.CMD_ALL = """
        select * from tb_hall
        """

        self.CMD_CLEAR = """
        """

# for test
if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    
    dbHall = CMDBHall()
    dbHall.init(conn)

    h0 = CMHall(u"第1号厅", u"demo")
    h1 = CMHall(u"第2号厅", u"demo")
    h2 = CMHall(u"第3号厅", u"demo")

    i = dbHall.add(conn, h0)
    i = dbHall.add(conn, h1)
    i = dbHall.add(conn, h2)

    halllist = dbHall.all(conn)

    for ihall in halllist:
        print ihall.id, ihall.name, ihall.info

    print("\nedit one item")
    halllist[0].name = u"第N号厅"
    dbHall.edit(conn, halllist[0])
    
    halllist = dbHall.all(conn)

    for ihall in halllist:
        print ihall.id, ihall.name, ihall.info
        
    print("\ndelete one item")
    dbHall.delete(conn, halllist[0])

    halllist = dbHall.all(conn)

    for ihall in halllist:
        print ihall.id, ihall.name, ihall.info
