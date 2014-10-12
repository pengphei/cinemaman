# -*- coding: utf-8 -*-

import traceback
import calendar
import datetime

class CMCalendar(object):
    """ for calendar management """
    def __init__(self):
        return

    def make_dates_list_align(self, year, month):
        """ make dates list aligned by 6 weeks """
        dates_list = []
        next_year, next_month = self.get_next_month(year, month)
        prev_year, prev_month = self.get_prev_month(year, month)

        prev_dates = self.make_dates_list(prev_year, prev_month)
        next_dates = self.make_dates_list(next_year, next_month)
        curr_dates = self.make_dates_list(year, month)

        # dates alignment processing
        # add dates before
        weekday_first = int(curr_dates[0].weekday())
        if(weekday_first != 0):
            dates_list = prev_dates[-weekday_first:] + curr_dates
        else:
            dates_list = curr_dates

        # add dates after
        days_left = 6*7 - len(dates_list)
        dates_list = dates_list + next_dates[0:days_left]
        
        return dates_list

    def make_dates_list(self, year, month):
        """ make dates list according to year and month """
        date_list = []
        cal_str = calendar.month(year, month)
        pre_weeks = cal_str.split('\n')[2:]
        pre_weeks = self.pre_check_invalid_weeks(pre_weeks)

        for week in pre_weeks:
            week_days = week.split()
            for day in week_days:
                date_list.append(datetime.date(year, month, int(day)))
            
        return date_list

    def pre_check_invalid_weeks(self, cal_weeks=[]):
        """ check prepared invalidation of weeks """
        assert len(cal_weeks) >= 3
            
        if(cal_weeks[-1] == ''):
            return cal_weeks[:-1]

        return cal_weeks

    def get_prev_month(self, year, month):
        """ get prev month according to year and month"""
        ret_year = year
        ret_month = month - 1
        if(ret_month == 0):
            ret_year = year - 1
            ret_month = 12
            
        return ret_year, ret_month

    def get_next_month(self, year, month):
        """ get next month according to year and month"""
        ret_year = year
        ret_month = month + 1
        if(ret_month == 13):
            ret_year = year + 1
            ret_month = 1
            
        return ret_year, ret_month

# test only
if __name__ == "__main__":
    cal = CMCalendar()

    # test for make_dates_list
    dates = cal.make_dates_list(2014, 9)

    for dt in dates:
        print dt.year, dt.month, dt.day, dt.weekday()

    print '\n'
    # test for make_dates_list_align

    dates = cal.make_dates_list_align(2014, 9)

    for dt in dates:
        print dt.year, dt.month, dt.day, dt.weekday()
