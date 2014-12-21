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
from ui.PlayDialog import *
from ui.PlayListView import *
from ui.MovieListView import *
from ui.HallListView import *
from ui.CalenderView import *
from ui.ExportToolView import *

## global config
gCfg = CMConfig()

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

        self.hallView = CMHallListView(self.root, self, 5)
        self.movieView = CMMovieListView(self.root, self, 5)
        self.calenderView = CMCalenderView(self.root, self, self.center_width)
        self.playView = CMPlayListView(self.root, self, self.center_width)
        self.exportView = CMExportToolView(self.root, self, self.center_width)
        return

    def play_update(self):
        self.playView.play_list_update()
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

    
if __name__ == "__main__":
    root = tk.Tk()
    app = CMApp(root)
    root.mainloop()
