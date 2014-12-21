# -*- coding: utf-8 -*-

import Tkinter as tk
import tkFont
import ttk

from CMApp import *

PLAY_VIEW_INFO_HALL = u"电影厅"
PLAY_VIEW_INFO_MOVIE = u"电影名称"
PLAY_VIEW_INFO_STARTTIME = u"开始时间"
PLAY_VIEW_INFO_ENDTIME = u"结束时间"
PLAY_VIEW_INFO_RESTTIME = u"中场休息"
PLAY_VIEW_INFO_PRICE = u"价格"

class CMPlayListViewItem:

    def __init__(self, parent, width, background="light yellow"):
        self.itemWidth = 15
        self.parent = parent
        self.frame = tk.LabelFrame(parent, width=width, bg=background)
        self.frame.pack(fill=tk.X, side=tk.TOP)
        
        self.hall = tk.StringVar()
        self.movie = tk.StringVar()
        self.starttime = tk.StringVar()
        self.endtime = tk.StringVar()
        self.resttime = tk.StringVar()
        self.price = tk.StringVar()

        self.hallLabel = tk.Label(self.frame, width=self.itemWidth, textvariable=self.hall, bg=background)
        self.hallLabel.pack(fill=tk.Y, side=tk.LEFT)
        self.movieLabel = tk.Label(self.frame, width=self.itemWidth, textvariable=self.movie, bg=background)
        self.movieLabel.pack(fill=tk.Y, side=tk.LEFT)
        self.startLabel = tk.Label(self.frame, width=self.itemWidth, textvariable=self.starttime, bg=background)
        self.startLabel.pack(fill=tk.Y, side=tk.LEFT)
        self.endLabel = tk.Label(self.frame, width=self.itemWidth, textvariable=self.endtime, bg=background)
        self.endLabel.pack(fill=tk.Y, side=tk.LEFT)
        self.restLabel = tk.Label(self.frame, width=self.itemWidth, textvariable=self.resttime, bg=background)
        self.restLabel.pack(fill=tk.Y, side=tk.LEFT)
        self.priceLabel = tk.Label(self.frame, width=self.itemWidth, textvariable=self.price, bg=background)
        self.priceLabel.pack(fill=tk.Y, side=tk.LEFT)
        return

    def update(self, play):
        self.hall.set(play.hallName)
        self.movie.set(play.movieName)
        self.starttime.set(play.startTime)
        self.endtime.set(play.endTime)
        self.resttime.set(play.restTime)
        self.price.set(play.price)
        return


class CMPlayListView:
    table_header = [
        PLAY_VIEW_INFO_HALL,
        PLAY_VIEW_INFO_MOVIE,
        PLAY_VIEW_INFO_STARTTIME,
        PLAY_VIEW_INFO_ENDTIME,
        PLAY_VIEW_INFO_RESTTIME,
        PLAY_VIEW_INFO_PRICE
    ]
    def __init__(self, root, parent, w, background='light yellow'):
        self.root = root
        self.parent = parent
        self.width = w
        # self._init_list_widget_legacy()
        self._init_list_widget()
        self._update_list_widget()
        return

    def _init_list_widget_legacy(self):
        self.frame = tk.LabelFrame(self.parent, width=self.width, bg='light gray')
        self.frame.pack(fill=tk.BOTH, side=tk.TOP)

        self.infoFrame = tk.LabelFrame(self.frame, width=self.width, bg=background)
        self.infoFrame.pack(fill=tk.X, side=tk.TOP)

        for header in self.table_header:
            label = tk.Label(self.infoFrame, text=header, width=15, bg=background)
            label.pack(fill=tk.Y, side=tk.LEFT)
            
        self.items = []
        
        for ii in range(10):
            item = CMPlayListViewItem(self.frame, width=self.width)
            item.frame.bind('<ButtonRelease-1>', self.play_list_single_click)
            item.frame.bind('<Double-ButtonRelease-1>', self.play_list_double_click)
            self.items.append(item)

        self.ToolsFrame = tk.LabelFrame(self.frame, width=self.width, bg='light gray')
        self.ToolsFrame.pack(fill=tk.Y, side=tk.BOTTOM)
        self.ToolAdd = tk.Button(self.ToolsFrame, text = '添加', command=self.play_add)
        self.ToolAdd.pack(fill=tk.Y, side=tk.LEFT)
        self.ToolDel = tk.Button(self.ToolsFrame, text = '删除', command=self.play_del)
        self.ToolDel.pack(fill=tk.Y, side=tk.LEFT)
        self.ToolEdit = tk.Button(self.ToolsFrame, text = '编辑', command=self.play_edit)
        self.ToolEdit.pack(fill=tk.Y, side=tk.LEFT)
        return

    def _init_list_widget(self):
        self.frame = tk.Frame(self.parent)
        self.frame.pack(fill=tk.BOTH, side=tk.TOP)
        self.playFrame = ttk.Frame(self.frame)
        self.playFrame.pack(fill=tk.BOTH, side=tk.TOP)
        self.playView = ttk.Treeview(columns=self.table_header, show='headings')
        self.playVsbar = ttk.Scrollbar(orient="vertical", command=self.playView.yview)
        self.playHsbar = ttk.Scrollbar(orient="horizontal", command=self.playView.xview)
        self.playView.configure(yscrollcommand=self.playVsbar.set, xscrollcommand=self.playHsbar.set)
        self.playView.grid(column=0, row=0, sticky='nsew', in_=self.playFrame)
        self.playVsbar.grid(column=1, row=0, sticky='ns', in_=self.playFrame)
        self.playHsbar.grid(column=0, row=1, sticky='ew', in_=self.playFrame)
        self.playFrame.grid_columnconfigure(0, weight=1)
        self.playFrame.grid_rowconfigure(0, weight=1)
        
        self.ToolsFrame = ttk.Frame(self.frame, width=self.width)
        self.ToolsFrame.pack(fill=tk.X, side=tk.BOTTOM)
        self.ToolAdd = ttk.Button(self.ToolsFrame, text = '添加', command=self.play_add)
        self.ToolAdd.pack(fill=tk.X, side=tk.LEFT)
        self.ToolDel = ttk.Button(self.ToolsFrame, text = '删除', command=self.play_del)
        self.ToolDel.pack(fill=tk.X, side=tk.LEFT)
        self.ToolEdit = ttk.Button(self.ToolsFrame, text = '编辑', command=self.play_edit)
        self.ToolEdit.pack(fill=tk.X, side=tk.LEFT)
        return

    def _update_list_widget(self):
        self.playView.configure(columns=self.table_header)

        for col in self.table_header:
            self.playView.heading(col, text=col)
            # adjust header width if necessary
            self.playView.column(col, width=tkFont.Font().measure(col))

        for item in gInfo.play_list:
            item_vars = (item.hallName, item.movieName, item.startTime, item.endTime, item.restTime, item.price)
            self.playView.insert('', 'end', values=item_vars)
            # adjust item width if necessary
            for ix, var in enumerate(item_vars):
                col_w = tkFont.Font().measure(var)
                if(self.playView.column(self.table_header[ix], width=None) < col_w):
                    self.playView.column(self.table_header[ix], width=col_w)


    def play_list_single_click(self, event):
        print("single click")
        return

    def play_list_double_click(self, event):
        print("double click")
        return
        

    def play_list_update(self):
        self._update_list_widget()
        return
    
    def play_add(self):
        dialog = PlayDialog(self.root)
        dialog.open_add(self)
        return

    def play_del(self):
        dialog = PlayDialog(self.root)
        dialog.open_del(self, self.focus_play)
        return

    def play_edit(self):
        dialog = PlayDialog(self.root)
        dialog.open_edit(self, self.focus_play)
        return

    def play_add_confirm(self, play):
        print play.hallName
        print play.movieName
        play.id = gInfo.db_play.add(gInfo.db.conn, play)
        gInfo.play_list.append(play)
        self.play_list_update()
        return
    
    def play_edit_confirm(self, play):
        if(len(gInfo.play_list) == 0 or gInfo.play_focus == -1):
            return

        play_old = gInfo.play_list[gInfo.play_focus]
        play.id = play_old.id
        gInfo.db_play.edit(gInfo.db.conn, play)
        gInfo.play_list[gInfo.play_focus] = play
        self.play_list_update()
        return
    
    def play_del_confirm(self, play):
        if(len(gInfo.play_list) == 0 or gInfo.play_focus == -1):
            return
        
        play_del = gInfo.play_list[gInfo.play_focus]
        gInfo.db_play.delete(gInfo.db.conn, play_del)
        gInfo.play_list.pop(gInfo.play_focus)

        last = len(gInfo.play_list) - 1
        
        if(gInfo.play_focus > last):
            gInfo.play_focus = last
        self.play_list_update()          
        return
