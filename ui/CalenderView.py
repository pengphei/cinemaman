# -*- coding: utf-8 -*-

import Tkinter as tk
import ttk
import datetime
import time
import thread
import calendar

from CMApp import *

class CMCalenderView(ttk.Frame):
    
    def __init__(self, root, parent, width_):
        ttk.Frame.__init__(self, parent, class_="CMCalenderView", width=width_)
        self.root = root
        self.parent = parent
        self.width = width_
        self._setup_widgets()
        return

    def _setup_widgets(self):
        self.calenderLeftFrame = ttk.Frame(self, width=self.width/2)
        self.calenderLeftFrame.pack(fill=tk.Y, side=tk.LEFT)

        self.calenderRightFrame = ttk.Frame(self, width=self.width/2)
        self.calenderRightFrame.pack(fill=tk.Y, side=tk.LEFT)

        # styles
        self.styles = ttk.Style()
        self.styles.configure('focus.TButton', foreground='red')
        self.styles.configure('normal.TButton', foreground='black')
        
        # now objects
        self.StrVarNow = tk.StringVar()
        self.StrVarNow.set(gInfo.now.ctime())
        self.NowFrame = ttk.Frame(self.calenderLeftFrame, width=self.width)
        self.NowStateLabel = ttk.Label(self.NowFrame, textvariable = self.StrVarNow)
        self.NowStateLabel.pack(side=tk.LEFT)
        self.NowFrame.pack(fill=tk.X, side=tk.TOP)
        
        # year objects
        self.StrVarYear = tk.StringVar()
        self.StrVarYear.set(str(gInfo.date_focus.year)+ u'年')
        self.YearFrame = ttk.Frame(self.calenderLeftFrame, width=2)
        self.YearMinusButton = ttk.Button(self.YearFrame, text = '<', command=self._year_minus, width=2)
        self.YearMinusButton.pack(side=tk.LEFT)
        self.YearStateLabel = ttk.Label(self.YearFrame, textvariable = self.StrVarYear, width=8)
        self.YearStateLabel.pack(side=tk.LEFT)
        self.YearPlusButton = ttk.Button(self.YearFrame, text = '>', command=self._year_plus, width=2)
        self.YearPlusButton.pack(side=tk.LEFT)
        self.YearFrame.pack(fill=tk.X, side=tk.TOP)

        # month objects
        self.StrVarMonth = tk.StringVar()
        self.StrVarMonth.set(str(gInfo.date_focus.month) + u'月')
        self.MonthFrame = ttk.Frame(self.calenderLeftFrame, width=2)
        self.MonthMinusButton = ttk.Button(self.MonthFrame, text = '<', command=self._month_minus, width=2)
        self.MonthMinusButton.pack(side=tk.LEFT)
        self.MonthStateLabel = ttk.Label(self.MonthFrame, textvariable = self.StrVarMonth, width=8)
        self.MonthStateLabel.pack(side=tk.LEFT)
        self.MonthPlusButton = ttk.Button(self.MonthFrame, text = '>', command=self._month_plus, width=2)
        self.MonthPlusButton.pack(side=tk.LEFT)
        self.MonthFrame.pack(fill=tk.X, side=tk.TOP)
        
        # calendar objects
        self.WeekButtonsList = []
        self.WeekStrVarList = []
        self.WeekFramesList = []
        self.WeekFrame = ttk.Frame(self.calenderRightFrame, width=2)
        self.WeekFrame.pack(fill=tk.X, side=tk.TOP)
        # days title
        self.week_titles = [u'星期一', u'星期二', u'星期三', u'星期四', u'星期五', u'星期六', u'星期日']
        self.WeekTitleFrame = ttk.Frame(self.WeekFrame)
        self.WeekTitleFrame.pack(fill=tk.X, side=tk.TOP)

        for title in self.week_titles:
            titleButton = ttk.Button(self.WeekTitleFrame, text=title, width=5)
            titleButton.pack(side=tk.LEFT)
        
        # days index
        for week_idx in range(6):
            weekFrame = ttk.Frame(self.WeekFrame)
            weekFrame.pack(fill=tk.X, side=tk.TOP)
            self.WeekFramesList.append(weekFrame)
            for day_idx in range(7):
                dayStrVar = tk.StringVar()
                dayStrVar.set(gInfo.date_list[week_idx*7 + day_idx].day)
                dayButton = ttk.Button(weekFrame, textvariable = dayStrVar, width=5)
                dayButton.bind('<ButtonRelease-1>', self._day_release)
                dayButton.pack(side=tk.LEFT)
                self.WeekStrVarList.append(dayStrVar)
                self.WeekButtonsList.append(dayButton)

        self.WeekButtonsList[gInfo.date_list_focus].config(style='focus.TButton')
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
        gInfo.now = datetime.datetime.now()
        self.StrVarNow.set(gInfo.now.ctime())
        self.root.update_idletasks()
        self.parent.after(1000, self.week_now_update)
        return

    def _day_release(self, event):
        self.WeekButtonsList[gInfo.date_list_focus].config(style='normal.TButton')
        idx = self.WeekButtonsList.index(event.widget)
        gInfo.set_focus_index(idx)
        self.WeekButtonsList[gInfo.date_list_focus].config(style='focus.TButton')
        self.root.update_idletasks()
        return

    def _year_minus(self):
        self.WeekButtonsList[gInfo.date_list_focus].config(style='normal.TButton')
        gInfo.year_minus()
        self.WeekButtonsList[gInfo.date_list_focus].config(style='focus.TButton')
        self.week_list_update()
        return

    def _year_plus(self):
        self.WeekButtonsList[gInfo.date_list_focus].config(style='normal.TButton')
        gInfo.year_plus()
        self.WeekButtonsList[gInfo.date_list_focus].config(style='focus.TButton')
        self.week_list_update()
        return
    
    def _month_minus(self):
        self.WeekButtonsList[gInfo.date_list_focus].config(style='normal.TButton')
        gInfo.month_minus()
        self.WeekButtonsList[gInfo.date_list_focus].config(style='focus.TButton')
        self.week_list_update()
        return
    
    def _month_plus(self):
        self.WeekButtonsList[gInfo.date_list_focus].config(style='normal.TButton')
        gInfo.month_plus()
        self.WeekButtonsList[gInfo.date_list_focus].config(style='focus.TButton')
        self.week_list_update()
        return
