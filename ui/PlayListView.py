# -*- coding: utf-8 -*-

import Tkinter as tk

from CMMoviePlay import *

PLAY_VIEW_INFO_HALL = u"hall"
PLAY_VIEW_INFO_MOVIE = u"电影"
PLAY_VIEW_INFO_STARTTIME = u"start"
PLAY_VIEW_INFO_ENDTIME = u"end"
PLAY_VIEW_INFO_PRICE = u"price"

class CMPlayListViewItem:

    def __init__(self, parent, width, background="light yellow"):
        self.parent = parent
        self.frame = tk.LabelFrame(parent, width=width, bg=background)
        self.frame.pack(fill=tk.X, side=tk.TOP)
        
        self.hall = tk.StringVar()
        self.movie = tk.StringVar()
        self.starttime = tk.StringVar()
        self.endtime = tk.StringVar()
        self.price = tk.StringVar()

        self.hallLabel = tk.Label(self.frame, width=5, textvariable=self.hall, bg=background)
        self.hallLabel.pack(fill=tk.Y, side=tk.LEFT)
        self.movieLabel = tk.Label(self.frame, width=5, textvariable=self.movie, bg=background)
        self.movieLabel.pack(fill=tk.Y, side=tk.LEFT)
        self.startLabel = tk.Label(self.frame, width=5, textvariable=self.starttime, bg=background)
        self.startLabel.pack(fill=tk.Y, side=tk.LEFT)
        self.endLabel = tk.Label(self.frame, width=5, textvariable=self.endtime, bg=background)
        self.endLabel.pack(fill=tk.Y, side=tk.LEFT)
        self.priceLabel = tk.Label(self.frame, width=5, textvariable=self.price, bg=background)
        self.priceLabel.pack(fill=tk.Y, side=tk.LEFT)
        return

    def update(self, play):
        self.hall.set(play.hallName)
        self.movie.set(play.movieName)
        self.starttime.set(play.startTime)
        self.endtime.set(play.endTime)
        self.price.set(play.price)
        return


class CMPlayListView:
    info_titles = [
        PLAY_VIEW_INFO_HALL,
        PLAY_VIEW_INFO_MOVIE,
        PLAY_VIEW_INFO_STARTTIME,
        PLAY_VIEW_INFO_ENDTIME,
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
            label = tk.Label(self.infoFrame, text=title, width=5, bg=background)
            label.pack(fill=tk.Y, side=tk.LEFT)
            
        self.items = []
        
        for ii in range(10):
            item = CMPlayListViewItem(self.frame, width=w)
            self.items.append(item)
            
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
