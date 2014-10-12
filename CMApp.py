# -*- coding: utf-8 -*-

import Tkinter as tk
import datetime
import time
import thread

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
        self.misc_init()
        #self.menu_init()
        self.hall_list_init(self.left_width)
        self.movie_list_init(self.right_width)
        self.week_list_init(self.center_width)
        self.play_list_init(self.center_width)
        
        # init ui data elements
        self.hall_list_update()
        self.movie_list_update()
        self.play_list_update()
        return

    def _init_data(self):
        return
    
    def menu_init(self):
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
    
    def _menu_click(self):
        return
    
    def misc_init(self):
        # title
        self.root.title(u'电影院管理')
        # pack
        self.pack(fill=tk.BOTH, expand=1)
        # centered window
        util_center_win(self)
        return

    def week_list_init(self, w):
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
        self.after(1000, self.week_now_update)
        return
    
    def movie_list_init(self, w):
        self.movieStrVar = tk.StringVar()
        self.movieFrame = tk.LabelFrame(self, width=w, borderwidth=2, bg='light gray')
        self.movieFrame.pack(fill=tk.Y, side=tk.RIGHT)

        self.movieTitle = tk.Label(self.movieFrame, text = u"电影列表", width=w, bg='light gray')
        self.movieTitle.pack(fill=tk.Y, side=tk.TOP)
        self.movieList = tk.Listbox(self.movieFrame, width=w, listvariable=self.movieStrVar, selectmode=tk.SINGLE, bg='light green')
        self.movieList.pack(fill=tk.BOTH, side=tk.TOP)

        # movie list key bindings
        self.movieList.bind('<ButtonRelease-1>', self.movie_single_click)
        self.movieList.bind('<Double-ButtonRelease-1>', self.movie_double_click)

        self.movieToolsFrame = tk.LabelFrame(self.movieFrame, width=w, bg='light gray')
        self.movieToolsFrame.pack(fill=tk.Y, side=tk.BOTTOM)
        self.movieToolAdd = tk.Button(self.movieToolsFrame, text = '添加', command=self.movie_add)
        self.movieToolAdd.pack(fill=tk.Y, side=tk.LEFT)
        self.movieToolDel = tk.Button(self.movieToolsFrame, text = '删除', command=self.movie_del)
        self.movieToolDel.pack(fill=tk.Y, side=tk.LEFT)
        self.movieToolEdit = tk.Button(self.movieToolsFrame, text = '编辑', command=self.movie_edit)
        self.movieToolEdit.pack(fill=tk.Y, side=tk.LEFT)
        pass

    def movie_list_update(self):
        # add movie
        movies = []
        for idx in range(len(gInfo.movie_list)):
            movies.append(gInfo.movie_list[idx].name)
        self.movieStrVar.set(tuple(movies))
        return
    
    def movie_single_click(self, event):
        idxs = self.movieList.curselection()
        if(len(idxs) == 0):
            return
        gInfo.movie_focus = idxs[0]
        self.focus_movie = gInfo.movie_list[gInfo.movie_focus]
        print("movie single click")
        print(self.focus_movie.name)
        return

    def movie_double_click(self, event):
        idxs = self.movieList.curselection()
        if(len(idxs) == 0):
            return
        gInfo.movie_focus = idxs[0]
        self.focus_movie = gInfo.movie_list[gInfo.movie_focus]
        print("mocie double click")
        print(self.focus_movie.name)
        self.movie_edit()
        return
    
    def movie_add(self):
        dialog = MovieDialog(self.root)
        dialog.open_add(self)
        return

    def movie_del(self):
        if(len(gInfo.movie_list) == 0 or gInfo.movie_focus == -1):
            return
        
        dialog = MovieDialog(self.root)
        dialog.open_del(self, self.focus_movie.name)
        return

    def movie_edit(self):
        if(len(gInfo.movie_list) == 0 or gInfo.movie_focus == -1):
            return
        
        dialog = MovieDialog(self.root)
        dialog.open_edit(self)
        return

    def movie_add_confirm(self, movie):
        movie.id = gInfo.db_movie.add(gInfo.db.conn, movie)
        gInfo.movie_list.append(movie);
        self.movie_list_update()
        return

    def movie_edit_confirm(self, movie):
        if(len(gInfo.movie_list) == 0 or gInfo.movie_focus == -1):
            return
        
        movie_old = gInfo.movie_list[gInfo.movie_focus]
        movie.id = movie_old.id
        gInfo.db_movie.edit(gInfo.db.conn, movie)
        gInfo.movie_list[gInfo.movie_focus] = movie
        self.movie_list_update()
        return

    def movie_del_confirm(self):
        if(len(gInfo.movie_list) == 0 or gInfo.movie_focus == -1):
            return
        
        movie_del = gInfo.movie_list[gInfo.movie_focus]
        gInfo.db_movie.delete(gInfo.db.conn, movie_del)
        gInfo.movie_list.pop(gInfo.movie_focus)

        last = len(gInfo.movie_list) - 1
        
        if(gInfo.movie_focus > last):
            gInfo.movie_focus = last
        self.movie_list_update()
        return
    
    def play_list_init(self, w):
        self.PlayFrame = tk.LabelFrame(self, width=w, bg='light blue')
        self.PlayFrame.pack(fill=tk.BOTH, side=tk.TOP)
        return
    
    def play_list_update(self):
        for idx in range(len(gInfo.play_list)):
            self.playList.insert(idx, gInfo.play_list[idx].name)
        return
    
    def play_add(self):
        return

    def play_del(self):
        return

    def play_edit(self):
        return

    def play_add_confirm(self, play):
        return
    def play_edit_confirm(self, play):
        return
    def play_del_confirm(self, play):
        return
    
    def hall_list_init(self, w):
        self.hallStrVar = tk.StringVar()
        self.hallFrame = tk.LabelFrame(self, width = w, borderwidth = 2, bg='light gray')
        self.hallFrame.pack(fill=tk.Y, side=tk.LEFT)

        self.hallTitle = tk.Label(self.hallFrame, text = u"电影厅列表", width=w, bg='light gray')
        self.hallTitle.pack(fill=tk.Y, side=tk.TOP)
        
        self.hallList = tk.Listbox(self.hallFrame, width=w, listvariable=self.hallStrVar, selectmode=tk.SINGLE, bg='light blue')
        self.hallList.pack(fill=tk.BOTH, side=tk.TOP)

        # hall list key bindings
        self.hallList.bind('<ButtonRelease-1>', self.hall_single_click)
        self.hallList.bind('<Double-ButtonRelease-1>', self.hall_double_click)
        
        self.hallToolsFrame = tk.LabelFrame(self.hallFrame, width=w, bg='light gray')
        self.hallToolsFrame.pack(fill=tk.Y, side=tk.BOTTOM)
        self.hallToolAdd = tk.Button(self.hallToolsFrame, text = '添加', command=self.hall_add)
        self.hallToolAdd.pack(fill=tk.Y, side=tk.LEFT)
        self.hallToolDel = tk.Button(self.hallToolsFrame, text = '删除', command=self.hall_del)
        self.hallToolDel.pack(fill=tk.Y, side=tk.LEFT)
        self.hallToolEdit = tk.Button(self.hallToolsFrame, text = '编辑', command=self.hall_edit)
        self.hallToolEdit.pack(fill=tk.Y, side=tk.LEFT)
        return

    def hall_list_update(self):
        halls = []
        # add hall
        for hall in gInfo.hall_list:
            halls.append(hall.name)
        self.hallStrVar.set(tuple(halls))
        return

    
    def hall_single_click(self, event):
        idxs = self.hallList.curselection()
        if(len(idxs) == 0):
            return
        gInfo.hall_focus = idxs[0]
        self.focus_hall = gInfo.hall_list[gInfo.hall_focus]
        print("hall single click")
        print(self.focus_hall.name)
        return
    
    def hall_double_click(self, event):
        idxs = self.hallList.curselection()
        if(len(idxs) == 0):
            return
        gInfo.hall_focus = idxs[0]
        self.focus_hall = gInfo.hall_list[gInfo.hall_focus]
        print("hall double click")
        print(self.focus_hall.name)
        self.hall_edit()
        return
    
    def hall_add(self):
        """ add hall """
        dialog = HallDialog(self.root)
        dialog.open_add(self)
        return

    def hall_del(self):
        """ dell hall """
        dialog = HallDialog(self.root)
        dialog.open_del(self, self.focus_hall.name)
        return

    def hall_edit(self):
        """ edit hall """
        dialog = HallDialog(self.root)
        dialog.open_edit(self)
        return

    def hall_add_confirm(self, hall):
        print hall.name
        hall.id = gInfo.db_hall.add(gInfo.db.conn, hall)
        gInfo.hall_list.append(hall);
        self.hall_list_update()
        return

    def hall_edit_comfirm(self, hall):
        if(len(gInfo.hall_list) == 0 or gInfo.hall_focus == -1):
            return
        
        hall_old = gInfo.movie_list[gInfo.hall_focus]
        hall.id = hall_old.id
        gInfo.db_hall.edit(gInfo.db.conn, hall)
        gInfo.hall_list[gInfo.hall_focus] = hall
        self.hall_list_update()
        return

    def hall_del_confirm(self):
        if(len(gInfo.hall_list) == 0 or gInfo.hall_focus == -1):
            return
        
        hall_del = gInfo.hall_list[gInfo.hall_focus]
        gInfo.db_hall.delete(gInfo.db.conn, hall_del)
        gInfo.hall_list.pop(gInfo.hall_focus)

        last = len(gInfo.hall_list) - 1
        
        if(gInfo.hall_focus > last):
            gInfo.hall_focus = last
        self.hall_list_update()        
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

if __name__ == "__main__":
    root = tk.Tk()
    app = CMApp(root)
    #uthread = thread.start_new_thread(app.week_now_update, ())
    root.mainloop()
    #uthread.exit()
