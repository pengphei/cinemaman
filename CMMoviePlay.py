# -*- coding: utf-8 -*-

import sqlite3
import datetime

class CMMoviePlay(object):
    """ 电影播放安排 """
    def __init__(self, idx = -1, hallID=-1, movieID=-1, startTime="", endTime="", price=0):
        self.id = idx
        self.hallID = hallID
        self.movieID = movieID
        self.startTime = startTime
        self.endTime = endTime
        self.price = price
        self.restTime = 0

        self.hallName = ""
        self.movieName = ""
        return

class CMDBMoviePlay(object):
    """ movie in db """
    def __init__(self):
        self._prepare()
        return

    def init(self, conn):
        cursor = conn.cursor()
        cursor.execute(self.CMD_CREATE_TABLE)
        conn.commit()
        return

    def add(self, conn, play):
        cursor = conn.cursor()
        cursor.execute(self.CMD_ADD, (play.hallID, play.movieID, play.startTime, play.endTime, play.price))
        conn.commit()
        return cursor.lastrowid

    def delete(self, conn, play):
        cursor = conn.cursor()
        cursor.execute(self.CMD_DEL+str(play.id))
        conn.commit()
        return

    def edit(self, conn, play):
        cursor = conn.cursor()
        cursor.execute(self.CMD_EDIT, (play.hallID, play.movieID, play.startTime, play.endTime, play.price, play.id))
        conn.commit()
        return

    def get_by_day_hall(self, conn, sdate, edate, hallid):
        rlist = []
        cursor = conn.cursor()
        start_day = datetime.datetime(sdate.year, sdate.month, sdate.day)
        end_day = datetime.datetime(edate.year, edate.month, edate.day)
        cursor.execute(self.CMD_QUERY_DATE_HALL, (start_day, end_day, hallid))
        for item in cursor.fetchall():
            play = CMMoviePlay(item[0], item[1], item[2], item[3], item[4], item[5])
            rlist.append(play)
        return rlist

    def get_all(self, conn):
        rlist = []
        cursor = conn.cursor()
        cursor.execute(self.CMD_ALL)
        for item in cursor.fetchall():
            play = CMMoviePlay(item[0], item[1], item[2], item[3], item[4], item[5])
            rlist.append(play)
        return rlist

    def clear(self, conn):
        pass
        cursor = conn.cursor()
        cursor.execute(self.CMD_CLEAR)
        conn.commit()
        pass

    def _prepare(self):
        self.CMD_CREATE_TABLE = """
        create table if not exists tb_movieplay(
            id integer primary key autoincrement,
            hall_id integer,
            movie_id integer,
            start_time timestamp,
            end_time timestamp,
            price integer
        )
        """

        self.CMD_ADD = """
        insert into tb_movieplay (id,hall_id,movie_id,start_time,end_time,price) values (NULL,?,?,?,?,?)
        """

        self.CMD_DEL = """
        delete from tb_movieplay where id =
        """

        self.CMD_EDIT = """
        update tb_movieplay set hall_id=?, movie_id=?, start_time=?, end_time=?, price=? where id = ?
        """

        self.CMD_QUERY_DATE_HALL = """
        select * from tb_movieplay where start_time >= ? and start_time < ? and hall_id = ?
        """

        self.CMD_ALL = """
        select * from tb_movieplay
        """

        self.CMD_CLEAR = """
        """

# for test
if __name__ == "__main__":
    m0 = CMMoviePlay(0, 1, 1, datetime.datetime(2014,9,12,12,21), datetime.datetime(2014,9,12,14,21), 25)
    m1 = CMMoviePlay(0, 1, 1, datetime.datetime(2014,10,12,16,21), datetime.datetime(2014,10,12,18,21), 23)
    m2 = CMMoviePlay(0, 2, 2, datetime.datetime(2014,10,12,18,21), datetime.datetime(2014,10,12,20,21), 44)

    dbPlay = CMDBMoviePlay()
    conn = sqlite3.connect("play.db")
    dbPlay.init(conn)

    i = dbPlay.add(conn, m0)
    i = dbPlay.add(conn, m1)
    i = dbPlay.add(conn, m2)

    mlist = dbPlay.all(conn)

    for iplay in mlist:
        print type(iplay.id), type(iplay.startTime), type(iplay.endTime)
        print iplay.id, iplay.hallID, iplay.movieID, iplay.startTime, iplay.endTime, iplay.price

    print("\nedit one item")
    mlist[0].hallID = 3
    dbPlay.edit(conn, mlist[0])

    mlist = dbPlay.all(conn)

    for iplay in mlist:
        print iplay.id, iplay.hallID, iplay.movieID, iplay.startTime, iplay.endTime, iplay.price

    print("\ndelete one item")
    dbPlay.delete(conn, mlist[0])

    print("\nget all \n")
    mlist = dbPlay.get_all(conn)

    for iplay in mlist:
        print iplay.id, iplay.hallID, iplay.movieID, iplay.startTime, iplay.endTime, iplay.price

    print("\nget date id \n")
    mlist = dbPlay.get_by_day_hall(conn, datetime.date(2014,10,12), datetime.date(2014,10,13), 1)

    for iplay in mlist:
        print iplay.id, iplay.hallID, iplay.movieID, iplay.startTime, iplay.endTime, iplay.price
