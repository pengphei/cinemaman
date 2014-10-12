# -*- coding: utf-8 -*-

import sqlite3

class CMMovie(object):
    """电影院电影"""
    def __init__(self, idx=-1, name='', duration=0, lang="未知", typex="", price=0):
        self.id = idx
        self.name = name
        self.duration = duration
        self.lang = lang
        self.type = typex
        self.price = price
        return

class CMDBMovie(object):
    """ movie in db """
    def __init__(self):
        self._prepare()
        return

    def init(self, conn):
        cursor = conn.cursor()
        cursor.execute(self.CMD_CREATE_TABLE)
        conn.commit()
        return

    def add(self, conn, movie):
        cursor = conn.cursor()
        cursor.execute(self.CMD_ADD, (movie.name, movie.duration, movie.lang, movie.type, movie.price))
        conn.commit()
        return cursor.lastrowid

    def delete(self, conn, movie):
        cursor = conn.cursor()
        cursor.execute(self.CMD_DEL+str(movie.id))
        conn.commit()
        return

    def edit(self, conn, movie):
        cursor = conn.cursor()
        cursor.execute(self.CMD_EDIT, (movie.name, movie.duration, movie.lang, movie.type, movie.price, movie.id))
        conn.commit()
        return

    def all(self, conn):
        movies = []
        cursor = conn.cursor()
        cursor.execute(self.CMD_ALL)
        for item in cursor.fetchall():
            movie = CMMovie(-1, item[1], item[2], item[3], item[4], item[5])
            movie.id = item[0]
            movies.append(movie)
        return movies

    def clear(self, conn):
        pass
        cursor = conn.cursor()
        cursor.execute(self.CMD_CLEAR)
        conn.commit()
        pass

    def _prepare(self):
        self.CMD_CREATE_TABLE = """
        create table if not exists tb_movie(
            id integer primary key autoincrement,
            name text,
            duration integer,
            lang text,
            type text,
            price integer
        )
        """

        self.CMD_ADD = """
        insert into tb_movie (id,name,duration,lang,type,price) values (NULL,?,?,?,?,?)
        """

        self.CMD_DEL = """
        delete from tb_movie where id =
        """

        self.CMD_EDIT = """
        update tb_movie set name=?, duration=?, lang=?, type=?, price=? where id = ?
        """

        self.CMD_ALL = """
        select * from tb_movie
        """

        self.CMD_CLEAR = """
        """

# for test
if __name__ == "__main__":
    m0 = CMMovie(-1, u"盗马记", 96, u"中", u"喜剧/剧情", 25)
    m1 = CMMovie(-1, u"整容日记", 88, u"中", u"喜剧/剧情", 25)
    m2 = CMMovie(-1, u"我在路上爱上你", 86, u"国语", u"喜剧/剧情", 25)

    dbMovie = CMDBMovie()
    conn = sqlite3.connect("./test.db")
    dbMovie.init(conn)

    i = dbMovie.add(conn, m0)
    i = dbMovie.add(conn, m1)
    i = dbMovie.add(conn, m2)

    mlist = dbMovie.all(conn)

    for imovie in mlist:
        print imovie.id, imovie.name, imovie.duration, imovie.lang, imovie.type, imovie.price

    print("\nedit one item")
    mlist[0].name = u"第二号厅"
    dbMovie.edit(conn, mlist[0])

    mlist = dbMovie.all(conn)

    for imovie in mlist:
        print imovie.id, imovie.name, imovie.duration, imovie.lang, imovie.type, imovie.price

    print("\ndelete one item")
    dbMovie.delete(conn, mlist[0])

    mlist = dbMovie.all(conn)

    for imovie in mlist:
        print imovie.id, imovie.name, imovie.duration, imovie.lang, imovie.type, imovie.price
