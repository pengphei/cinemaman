# -*- coding: utf-8 -*-

import datetime
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
        self.movie_list_update()
        self.hall_list_update()
        self.movie_focus = -1
        self.play_focus = -1
        self.hall_focus = -1
        return
    
    def _init_date(self):
        """ init date referrent information """
        self.calendar = CMCalendar()
        self.now = datetime.datetime.now()
        self.date_focus = datetime.date(self.now.year, self.now.month, self.now.day)
        self.date_list = self.calendar.make_dates_list_align(self.date_focus.year, self.date_focus.month)
        self.caculate_date_index()
        self.play_list_update()
        return

    def set_focus_date(self, date):
        self.date_focus = date
        self.caculate_date_index()
        self.play_list_update()
        return

    def set_focus_index(self, idx):
        self.date_focus = self.date_list[idx];
        self.date_list_focus = idx;
        self.play_list_update()
        return

    def year_minus(self):
        self.date_focus = datetime.date(self.date_focus.year + 1, self.date_focus.month, 1)
        self.date_list = self.calendar.make_dates_list_align(self.date_focus.year, self.date_focus.month)
        self.caculate_date_index()
        self.play_list_update()
        return

    def year_plus(self):
        self.date_focus = datetime.date(self.date_focus.year - 1, self.date_focus.month, 1)
        self.date_list = self.calendar.make_dates_list_align(self.date_focus.year, self.date_focus.month)
        self.caculate_date_index()
        self.play_list_update()
        return

    def month_minus(self):
        focus_year, focus_month = self.calendar.get_prev_month(self.date_focus.year, self.date_focus.month)
        self.date_focus = datetime.date(focus_year, focus_month, 1)
        self.date_list = self.calendar.make_dates_list_align(self.date_focus.year, self.date_focus.month)
        self.caculate_date_index()
        self.play_list_update()
        return

    def month_plus(self):
        focus_year, focus_month = self.calendar.get_next_month(self.date_focus.year, self.date_focus.month)
        self.date_focus = datetime.date(focus_year, focus_month, 1)
        self.date_list = self.calendar.make_dates_list_align(self.date_focus.year, self.date_focus.month)
        self.caculate_date_index()
        self.play_list_update()
        return

    def caculate_date_index(self):
        for idx in range(len(self.date_list)):
            dd = self.date_list[idx]
            if(self.date_focus.day == dd.day and self.date_focus.month == dd.month):
                self.date_list_focus = idx
                break
            

    def now_update(self):
        self.now = datetime.datetime.now()
        return

    def movie_list_update(self):
        self.movie_list = self.db_movie.get_all(self.db.conn)
        self.movie_names_list = []
        for item in self.movie_list:
            self.movie_names_list.append(item.name)
        return
    
    def hall_list_update(self):
        self.hall_list = self.db_hall.get_all(self.db.conn)
        self.hall_names_list = []
        for hall in self.hall_list:
            self.hall_names_list.append(hall.name)
        return
    
    def play_list_update(self):
        start_date = self.date_focus
        end_date = 0
        hall_id = self.hall_list[self.hall_focus].id
        if(self.date_list_focus < len(self.date_list)-1):
            end_date = self.date_list[self.date_list_focus+1]
        else:
            end_date = self.date_focus
            end_date.date += 1
            
        self.play_list = self.db_play.get_by_day_hall(self.db.conn, start_date, end_date, hall_id)
        return

    def _fini_db(self):
        """ fini database """
        self.db.fini()

## global information
gInfo = CMGlobal()
gInfo.init()

