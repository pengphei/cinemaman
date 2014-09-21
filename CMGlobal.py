# -*- coding: utf-8 -*-

from datetime import *
from CMDB import *
from CMHall import *
from CMMovie import *
from CMMoviePlay import *
from CMCalendar import *

class CMGlobal(object):
    movie_list = []
    play_list = []
    hall_list = []
    date_list = []

    def __init__(self):
        return

    def init(self, db_path="./cm.db"):
        self._init_db(db_path)
        self._init_list()
        self._init_date()
        return

    def fini(self):
        self._fini_db()
        return
    
    def _init_db(self, path):
        """ init database """
        # db init
        self.db = CMDB(path)
        self.db.init()
        
        # hall db init
        self.db_hall = CMDBHall()
        self.db_hall.init(self.db.conn)

        # movie db init
        self.db_movie = CMDBMovie()
        self.db_movie.init(self.db.conn)

        # play db init
        self.db_play = CMDBMoviePlay()
        self.db_play.init(self.db.conn)
        return

    def _init_list(self):
        """ init all lists """
        self.movie_list = self.db_movie.all(self.db.conn)
        self.play_list = self.db_play.all(self.db.conn)
        self.hall_list = self.db_hall.all(self.db.conn)
        return
    
    def _init_date(self):
        """ init date referrent information """
        self.calendar = CMCalendar()
        self.now = datetime.now()
        self.date_focus = date(self.now.year, self.now.month, self.now.day)
        self.date_list = self.calendar.make_dates_list_align(self.date_focus.year, self.date_focus.month)
        return

    def _fini_db(self):
        """ fini database """
        self.db.fini()
        
        
