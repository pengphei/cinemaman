# -*- coding: utf-8 -*-

from datetime import *
from CMDB import *
from CMHall import *
from CMMovie import *
from CMMoviePlay import *

import calendar

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
        self.now = datetime.now()
        self.date = date(now.year, now.month, now.day)

        self.make_calendar_list(month.year, month.day)
        return
    
    def make_calendar_list(self, year=2014, month=09):
        self.calendar_list = []
        # previous month
        self.prev_year = year
        self.prev_month = month - 1

        if(self.pre_month == 0):
            self.prev_year = year - 1
            self.prev_month = 12
            
        self.prev_calendar = calendar.month(self.prev_year, self.prev_month)
        
        # next month
        self.next_year = year
        self.next_month = month + 1
        if(self.next_month == 13):
            self.next_year = year + 1
            self.next_month = 1

        self.next_calendar = calendar.month(self.next_year, self.next_month)

        # current month
        self.curr_calendar = calendar.month(year, month)

        curr_list = self.curr_calendar.split('\n')[2:]
        curr_len = len(curr_list)
        prev_list = self.prev_calendar.split('\n')[2:]
        prev_len = len(prev_list)
        next_list = self.next_calendar.split('\n')[2:]
        next_len = len(next_list)
        
        # complete first week
        if('1' == curr_list[0][1]):
            
        else:
                
        # complete last two weeks
        if(20 != len(curr_list[4])):
            idx_first = next_list[0].find('1') - 2
            curr_list[4] = curr_list[4] + next_list[0][idx_first:]
            curr_list.append(next_list[1])
        else:
            curr_list.append(next_list[0])
            
        return 
    
    def _fini_db(self):
        """ fini database """
        self.db.fini()
        
        
