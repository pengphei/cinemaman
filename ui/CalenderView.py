# -*- coding: utf-8 -*-

import Tkinter as tk
import datetime
import time
import thread

from CMApp import *

class CMCalenderView():
    
    def __init__(self, root, parent, w):
        self.root = root
        self.parent = parent
        self.calenderFrame = tk.LabelFrame(self.parent, width=w, bg='light gray')
        self.calenderFrame.pack(fill=tk.X, side=tk.TOP)

        self.calenderLeftFrame = tk.LabelFrame(self.calenderFrame, width=w/2, bg='light gray')
        self.calenderLeftFrame.pack(fill=tk.Y, side=tk.LEFT)

        self.calenderRightFrame = tk.LabelFrame(self.calenderFrame, width=w/2, bg='light gray')
        self.calenderRightFrame.pack(fill=tk.Y, side=tk.LEFT)
        
        # now objects
        self.StrVarNow = tk.StringVar()
        self.StrVarNow.set(gInfo.now.ctime())
        self.NowFrame = tk.LabelFrame(self.calenderLeftFrame, width=w, bg='light gray')
        self.NowStateLabel = tk.Label(self.NowFrame, textvariable = self.StrVarNow, fg='blue', bg='light gray')
        self.NowStateLabel.pack(side=tk.LEFT)
        self.NowFrame.pack(fill=tk.X, side=tk.TOP)
        
        # year objects
        self.StrVarYear = tk.StringVar()
        self.StrVarYear.set(str(gInfo.date_focus.year)+ u'年')
        self.YearFrame = tk.LabelFrame(self.calenderLeftFrame, width=2, bg='light gray')
        self.YearMinusButton = tk.Button(self.YearFrame, text = '<', fg='green', command=self._year_minus)
        self.YearMinusButton.pack(side=tk.LEFT)
        self.YearStateLabel = tk.Label(self.YearFrame, textvariable = self.StrVarYear, fg='green')
        self.YearStateLabel.pack(side=tk.LEFT)
        self.YearPlusButton = tk.Button(self.YearFrame, text = '>', fg='green', command=self._year_plus)
        self.YearPlusButton.pack(side=tk.LEFT)
        self.YearFrame.pack(fill=tk.X, side=tk.TOP)

        # month objects
        self.StrVarMonth = tk.StringVar()
        self.StrVarMonth.set(str(gInfo.date_focus.month) + u'月')
        self.MonthFrame = tk.LabelFrame(self.calenderLeftFrame, width=2, bg='light gray')
        self.MonthMinusButton = tk.Button(self.MonthFrame, text = '<', fg='green', command=self._month_minus)
        self.MonthMinusButton.pack(side=tk.LEFT)
        self.MonthStateLabel = tk.Label(self.MonthFrame, textvariable = self.StrVarMonth, fg='green')
        self.MonthStateLabel.pack(side=tk.LEFT)
        self.MonthPlusButton = tk.Button(self.MonthFrame, text = '>', fg='green', command=self._month_plus)
        self.MonthPlusButton.pack(side=tk.LEFT)
        self.MonthFrame.pack(fill=tk.X, side=tk.TOP)
        
        # calendar objects
        self.WeekButtonsList = []
        self.WeekStrVarList = []
        self.WeekFramesList = []
        self.WeekFrame = tk.LabelFrame(self.calenderRightFrame, width=2, bg='light gray')
        self.WeekFrame.pack(fill=tk.X, side=tk.TOP)
        # days title
        self.week_titles = [u'星期一', u'星期二', u'星期三', u'星期四', u'星期五', u'星期六', u'星期日']
        self.WeekTitleFrame = tk.LabelFrame(self.WeekFrame)
        self.WeekTitleFrame.pack(fill=tk.X, side=tk.TOP)

        for title in self.week_titles:
            titleButton = tk.Button(self.WeekTitleFrame, text=title, width=5)
            titleButton.pack(side=tk.LEFT)
        
        # days index
        for week_idx in range(6):
            weekFrame = tk.LabelFrame(self.WeekFrame)
            weekFrame.pack(fill=tk.X, side=tk.TOP)
            self.WeekFramesList.append(weekFrame)
            for day_idx in range(7):
                dayStrVar = tk.StringVar()
                dayStrVar.set(gInfo.date_list[week_idx*7 + day_idx].day)
                dayButton = tk.Button(weekFrame, textvariable = dayStrVar, width=5, command=self._day_click)
                dayButton.pack(side=tk.LEFT)
                self.WeekStrVarList.append(dayStrVar)
                self.WeekButtonsList.append(dayButton)

        self.week_now_update()
        return

    def week_list_update(self):
        # update year
        self.StrVarYear.set(str(gInfo.date_focus.year) + u'年')
        # update month
        self.StrVarMonth.set(str(gInfo.date_focus.month) + u'月')
        # update weeks
        for idx in range(6*7):
            self.WeekStrVarList[idx].set(str(gInfo.date_list[idx].day))
            
        self.root.update_idletasks()
        return
    
    def week_now_update(self):
        print('update week now!')
        gInfo.now = datetime.datetime.now()
        self.StrVarNow.set(gInfo.now.ctime())
        self.root.update_idletasks()
        self.parent.after(1000, self.week_now_update)
        return

    def _day_click(self):
        return

    def _year_minus(self):
        gInfo.year_minus()
        self.week_list_update()
        return

    def _year_plus(self):
        gInfo.year_plus()
        self.week_list_update()
        return
    
    def _month_minus(self):
        gInfo.month_minus()
        self.week_list_update()
        return
    
    def _month_plus(self):
        gInfo.month_plus()
        self.week_list_update()
        return
