# -*- coding: utf-8 -*-

import Tkinter as tk

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
    info_titles = [
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
        self.frame = tk.LabelFrame(self.parent, width=w, bg=background)
        self.frame.pack(fill=tk.BOTH, side=tk.TOP)

        self.infoFrame = tk.LabelFrame(self.frame, width=w, bg=background)
        self.infoFrame.pack(fill=tk.X, side=tk.TOP)

        for title in self.info_titles:
            label = tk.Label(self.infoFrame, text=title, width=15, bg=background)
            label.pack(fill=tk.Y, side=tk.LEFT)
            
        self.items = []
        
        for ii in range(10):
            item = CMPlayListViewItem(self.frame, width=w)
            item.frame.bind('<ButtonRelease-1>', self.play_list_single_click)
            item.frame.bind('<Double-ButtonRelease-1>', self.play_list_double_click)
            self.items.append(item)
            
        return

    def play_list_single_click(self, event):
        print("single click")
        return

    def play_list_double_click(self, event):
        print("double click")
        return
        

    def play_list_update(self):
        for idx in range(len(gInfo.play_list)):
            self.items.update(gInfo.play_list[idx])
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
