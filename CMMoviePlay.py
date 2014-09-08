# -*- coding: utf-8 -*-

import sqlite3

class CMMoviePlay:
    """ 电影播放安排 """
    id = -1
    hallID = -1
    movieID = -1
    startTime = ""
    endTime = ""
    price = -1
    def __init__(self, hallID, movieID, startTime, endTime, price):
        self.hallID = hallID
        self.movieID = movieID
        self.startTime = startTime
        self.endTime = endTime
        self.price = price
        return

class CMDBMoviePlay:
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

    def all(self, conn):
        list = []
        cursor = conn.cursor()
        cursor.execute(self.CMD_ALL)
        for item in cursor.fetchall():
            play = CMMoviePlay(item[1], item[2], item[3], item[4], item[5])
            play.id = item[0]
            list.append(play)
        return list

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
            start_time text,
            end_time text,
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

        self.CMD_ALL = """
        select * from tb_movieplay
        """

        self.CMD_CLEAR = """
        """

# for test
if __name__ == "__main__":
    m0 = CMMoviePlay(1, 1, "2014-09-12 12:21", "2014-09-12 14:21", 25)
    m1 = CMMoviePlay(1, 1, "2014-09-12 12:45", "2014-09-12 14:21", 23)
    m2 = CMMoviePlay(2, 2, "2014-09-12 12:21", "2014-09-12 14:21", 44)

    dbPlay = CMDBMoviePlay()
    conn = sqlite3.connect(":memory:")
    dbPlay.init(conn)

    i = dbPlay.add(conn, m0)
    i = dbPlay.add(conn, m1)
    i = dbPlay.add(conn, m2)

    mlist = dbPlay.all(conn)

    for iplay in mlist:
        print iplay.id, iplay.hallID, iplay.movieID, iplay.startTime, iplay.endTime, iplay.price

    print("\nedit one item")
    mlist[0].hallID = 3
    dbPlay.edit(conn, mlist[0])

    mlist = dbPlay.all(conn)

    for iplay in mlist:
        print iplay.id, iplay.hallID, iplay.movieID, iplay.startTime, iplay.endTime, iplay.price

    print("\ndelete one item")
    dbPlay.delete(conn, mlist[0])

    mlist = dbPlay.all(conn)

    for iplay in mlist:
        print iplay.id, iplay.hallID, iplay.movieID, iplay.startTime, iplay.endTime, iplay.price

