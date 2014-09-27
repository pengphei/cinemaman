# -*- coding: utf-8 -*-

import Tkinter as tk
from threading import Timer
from datetime import *

from CMGlobal import *
from CMConfig import *
from CMUtil import *

# dialog import
from ui.MovieDialog import *
from ui.HallDialog import *

## global config
gCfg = CMConfig()

## global information
gInfo = CMGlobal()
gInfo.init()

# Frame is container for other widgets
class CMApp(tk.Frame):
    left_width = 15
    right_width = 15
    center_width = 70
    width = 1000
    height = 800
    
    def __init__(self, root=None):
        tk.Frame.__init__(self, root)
        self.root = root
        # init ui elemets
        self._init_misc()
        #self._init_menu()
        self._init_hall_list(self.left_width)
        self._init_movie_list(self.right_width)
        self._init_week_list(self.center_width)
        self._init_play_list(self.center_width)
        
        # init ui data elements
        self.update_hall_list()
        self.update_movie_list()
        self.update_play_list()
        return

    def _init_data(self):
        print "hi there, everyone!"

        return
    def _init_menu(self):
        # Menu widget which displays a list of choice of MenuButton
        # choises includes:
        #   simple command
        #   cascade, string or image user can select to show another Menu includes choices list
        #   Checkbutton
        #   group of Radiobutton
        self.menuBar = tk.Menu(self.root)

        # file cascade
        self.fileMenu = tk.Menu(self.menuBar)
        self.fileMenu.add_command(label="新建", command=self._menu_click)
        self.fileMenu.add_command(label="打开", command=self._menu_click)
        self.fileMenu.add_command(label="保存", command=self._menu_click)
        self.fileMenu.add_command(label="另存为...", command=self._menu_click)
        self.fileMenu.add_command(label="关闭", command=self._menu_click)

        self.fileMenu.add_separator()

        self.fileMenu.add_command(label="退出", command=self.root.quit)
        
        self.menuBar.add_cascade(label="文件", menu=self.fileMenu)
        
        # movie hall cascade
        self.hallMenu = tk.Menu(self.menuBar)
        self.hallMenu.add_command(label="添加", command=self._menu_click)
        self.hallMenu.add_command(label="删除", command=self._menu_click)
        self.hallMenu.add_command(label="编辑", command=self._menu_click)
        self.menuBar.add_cascade(label="电影厅", menu=self.hallMenu)

        # movie cascade
        self.movieMenu = tk.Menu(self.menuBar)
        self.movieMenu.add_command(label="添加", command=self._menu_click)
        self.movieMenu.add_command(label="删除", command=self._menu_click)
        self.movieMenu.add_command(label="编辑", command=self._menu_click)
        self.menuBar.add_cascade(label="电影", menu=self.movieMenu)

        # help cascade
        self.helpMenu = tk.Menu(self.menuBar)
        self.helpMenu.add_command(label="帮助", command=self._menu_click)
        self.menuBar.add_cascade(label="帮助", menu=self.helpMenu)
        self.master.config(menu=self.menuBar)
        return
    
    def _init_misc(self):
        # title
        self.root.title(u'电影院管理')
        # pack
        self.pack(fill=tk.BOTH, expand=1)

        # centered window
        util_center_win(self)
        return

    def _init_hall_list(self, w):
        self.hallFrame = tk.LabelFrame(self, width = w, borderwidth = 2, bg='light gray')
        self.hallFrame.pack(fill=tk.Y, side=tk.LEFT)

        self.hallTitle = tk.Label(self.hallFrame, text = u"电影厅列表", width=w, bg='light gray')
        self.hallTitle.pack(fill=tk.Y, side=tk.TOP)
        
        self.hallList = tk.Listbox(self.hallFrame, width=w, selectmode=tk.SINGLE, bg='light blue')
        self.hallList.pack(fill=tk.BOTH, side=tk.TOP)

        self.hallToolsFrame = tk.LabelFrame(self.hallFrame, width=w, bg='light gray')
        self.hallToolsFrame.pack(fill=tk.Y, side=tk.BOTTOM)
        self.hallToolAdd = tk.Button(self.hallToolsFrame, text = '添加', command=self._hall_add)
        self.hallToolAdd.pack(fill=tk.Y, side=tk.LEFT)
        self.hallToolDel = tk.Button(self.hallToolsFrame, text = '删除', command=self._hall_del)
        self.hallToolDel.pack(fill=tk.Y, side=tk.LEFT)
        self.hallToolEdit = tk.Button(self.hallToolsFrame, text = '编辑', command=self._hall_edit)
        self.hallToolEdit.pack(fill=tk.Y, side=tk.LEFT)
        return

    def _init_movie_list(self, w):
        self.movieFrame = tk.LabelFrame(self, width=w, borderwidth=2, bg='light gray')
        self.movieFrame.pack(fill=tk.Y, side=tk.RIGHT)

        self.movieTitle = tk.Label(self.movieFrame, text = u"电影列表", width=w, bg='light gray')
        self.movieTitle.pack(fill=tk.Y, side=tk.TOP)
        self.movielist = tk.Listbox(self.movieFrame, width=w, selectmode=tk.SINGLE, bg='light green')
        self.movielist.pack(fill=tk.BOTH, side=tk.TOP)

        self.movieToolsFrame = tk.LabelFrame(self.movieFrame, width=w, bg='light gray')
        self.movieToolsFrame.pack(fill=tk.Y, side=tk.BOTTOM)
        self.movieToolAdd = tk.Button(self.movieToolsFrame, text = '添加', command=self._movie_add)
        self.movieToolAdd.pack(fill=tk.Y, side=tk.LEFT)
        self.movieToolDel = tk.Button(self.movieToolsFrame, text = '删除', command=self._movie_del)
        self.movieToolDel.pack(fill=tk.Y, side=tk.LEFT)
        self.movieToolEdit = tk.Button(self.movieToolsFrame, text = '编辑', command=self._movie_edit)
        self.movieToolEdit.pack(fill=tk.Y, side=tk.LEFT)
        pass

    def _init_week_list(self, w):
        self.calenderFrame = tk.LabelFrame(self, width=w, bg='light gray')
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
        self.NowTimer = Timer(2, self.update_week_now)
        self.NowTimer.start()
        
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
        return
    
    def _init_play_list(self, w):
        self.PlayFrame = tk.LabelFrame(self, width=w, bg='light blue')
        self.PlayFrame.pack(fill=tk.BOTH, side=tk.TOP)
        return
    
    def update_hall_list(self):
        # add hall
        for idx in range(len(gInfo.hall_list)):
            self.hallList.insert(idx, gInfo.hall_list[idx].name)
        return
    
    def update_movie_list(self):
        # add movie
        for idx in range(len(gInfo.movie_list)):
            self.movieList.insert(idx, gInfo.movie_list[idx].name)
        return
    
    def update_play_list(self):
        for idx in range(len(gInfo.play_list)):
            self.playList.insert(idx, gInfo.play_list[idx].name)
        return

    def update_week_now(self):
        print('hello world!')
        gInfo.now = datetime.now()
        self.StrVarNow.set(gInfo.now.ctime())
        self.root.update()
        return
    
    def update_week_list(self):
        # update year
        self.StrVarYear.set(str(gInfo.date_focus.year) + u'年')
        # update month
        self.StrVarMonth.set(str(gInfo.date_focus.month) + u'月')
        # update weeks
        for idx in range(6*7):
            self.WeekStrVarList[idx].set(str(gInfo.date_list[idx].day))
        self.root.update_idletasks()
        return

    def update_play_list(self, hall=-1, date=''):
        return

    def _menu_click(self):
        return

    def _movie_add(self):
        dialog = MovieDialog(self.root)
        dialog.open_add(gInfo)
        return

    def _movie_del(self):
        dialog = MovieDialog(self.root)
        dialog.open_del(gInfo)
        return

    def _movie_edit(self):
        dialog = MovieDialog(self.root)
        dialog.open_edit(gInfo)
        return

    def _play_add(self):
        return

    def _play_del(self):
        return

    def _play_edit(self):
        return

    def _hall_add(self):
        dialog = HallDialog(self.root)
        dialog.open_add(gInfo)
        return

    def _hall_del(self):
        dialog = HallDialog(self.root)
        dialog.open_del(gInfo)
        return

    def _hall_edit(self):
        dialog = HallDialog(self.root)
        dialog.open_edit(gInfo)
        return

    def _day_click(self):
        return

    def _year_minus(self):
        gInfo.year_minus()
        self.update_week_list()
        return

    def _year_plus(self):
        gInfo.year_plus()
        self.update_week_list()
        return
    
    def _month_minus(self):
        gInfo.month_minus()
        self.update_week_list()
        return
    
    def _month_plus(self):
        gInfo.month_plus()
        self.update_week_list()
        return    

if __name__ == "__main__":
    root = tk.Tk()
    app = CMApp(root)
    root.mainloop()
    root.destroy()
