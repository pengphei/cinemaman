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

class CMPlayListView(ttk.Frame):
    table_header = [
        PLAY_VIEW_INFO_HALL,
        PLAY_VIEW_INFO_MOVIE,
        PLAY_VIEW_INFO_STARTTIME,
        PLAY_VIEW_INFO_ENDTIME,
        PLAY_VIEW_INFO_RESTTIME,
        PLAY_VIEW_INFO_PRICE
    ]
    def __init__(self, root, parent, width_):
        ttk.Frame.__init__(self, parent, class_="CMPlayListView", width=width_)
        self.root = root
        self.parent = parent
        self.width = width_
        self._setup_widgets()
        self._update_list_widget()
        return

    def _setup_widgets(self):
        self.playFrame = ttk.Frame(self)
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
        
        self.ToolsFrame = ttk.Frame(self, width=self.width)
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


    def show(self):
        self.frame.show()
        return

    def hide(self):
        self.frame.hide()
        return
    
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
