# -*- coding: utf-8 -*-

import Tkinter as tk
import ttk
from CMGlobal import *
from CMUtil import *

PLAY_DIALOG_ADD = 'add'
PLAY_DIALOG_DEL = 'del'
PLAY_DIALOG_EDIT = 'edit'

IDX_PLAY_LABEL_HALL = 0
IDX_PLAY_LABEL_MOVIE = 1
IDX_PLAY_LABEL_START = 2
IDX_PLAY_LABEL_END = 3
IDX_PLAY_LABEL_REST = 4
IDX_PLAY_LABEL_PRICE = 5

STR_PLAY_LABEL_HALL = u'影厅名称：'
STR_PLAY_LABEL_MOVIE = u'电影名称：'
STR_PLAY_LABEL_START = u'开始时间：'
STR_PLAY_LABEL_END = u'结束时间：'
STR_PLAY_LABEL_REST = u'中场休息：'
STR_PLAY_LABEL_PRICE = u'价格：'

STRS_PLAY_LABEL = [
    STR_PLAY_LABEL_HALL,
    STR_PLAY_LABEL_MOVIE,
    STR_PLAY_LABEL_START,
    STR_PLAY_LABEL_END,
    STR_PLAY_LABEL_REST,
    STR_PLAY_LABEL_PRICE,
]

STR_PLAY_ADD = u'添加'
STR_PLAY_OK = u'确定'
STR_PLAY_CANCEL = u'取消'
STR_PLAY_DEL = u'删除'
STR_PLAY_TITLE_ADD = u'添加播放项'
STR_PLAY_TITLE_EDIT = u'编辑播放项'
STR_PLAY_TITLE_DEL = u'删除播放项'

class PlayDialog():
    def __init__(self, parent):
        self.root = parent
        self.top = tk.Toplevel(parent)
        self.width = 300
        self.height = 200
        return

    def _ui_init_addedit(self, title, dtype, wmain, play=None):
        self.wmain = wmain
        self.dtype = PLAY_DIALOG_ADD
        self.title = title
        self.top.title(self.title)
        
        self.titleLabel = ttk.Label(self.top, text=self.title)
        self.titleLabel.pack(side=tk.TOP)

        self.strVars = []
        var_len = len(STRS_PLAY_LABEL)

        for ii in range(var_len):
            var = tk.StringVar()
            self.strVars.append(var)

        if(play != None):
            self.strVars[IDX_PLAY_LABEL_HALL] = play.hallName
            self.strVars[IDX_PLAY_LABEL_MOVIE] = play.movieName
            self.strVars[IDX_PLAY_LABEL_START] = play.startTime
            self.strVars[IDX_PLAY_LABEL_END] = play.endTime
            self.strVars[IDX_PLAY_LABEL_REST] = str(play.restTime)
            self.strVars[IDX_PLAY_LABEL_PRICE] = str(play.price)

        # hall id combo box
        self.hallFrame = ttk.Frame(self.top)
        self.hallFrame.pack(side=tk.TOP)
        self.hallLabel = ttk.Label(self.hallFrame, text=STRS_PLAY_LABEL[0], width=8)
        self.hallLabel.pack(side=tk.LEFT)
        self.hallCombo = ttk.Combobox(self.hallFrame)
        self.hallCombo.config(state="readonly")
        self.hallCombo['values'] = gInfo.hall_names_list
        self.hallCombo.pack(side=tk.LEFT)

        # movie id combo box
        self.movieFrame = ttk.Frame(self.top)
        self.movieFrame.pack(side=tk.TOP)
        self.movieLabel = ttk.Label(self.movieFrame, text=STRS_PLAY_LABEL[1], width=8)
        self.movieLabel.pack(side=tk.LEFT)
        self.movieCombo = ttk.Combobox(self.movieFrame)
        self.movieCombo.config(state="readonly")
        self.movieCombo['values'] = gInfo.movie_names_list
        self.movieCombo.pack(side=tk.LEFT)

        # start time
        self.stimeStrVar = tk.StringVar()
        self.stimeFrame = ttk.Frame(self.top)
        self.stimeFrame.pack(side=tk.TOP)
        self.stimeLabel = ttk.Label(self.stimeFrame, text=STRS_PLAY_LABEL[2], width=8)
        self.stimeLabel.pack(side=tk.LEFT)
        self.stimeEntry = ttk.Entry(self.stimeFrame, textvariable=self.stimeStrVar)
        self.stimeEntry.pack(side=tk.LEFT)

        # end time
        self.etimeStrVar = tk.StringVar()
        self.etimeFrame = ttk.Frame(self.top)
        self.etimeFrame.pack(side=tk.TOP)
        self.etimeLabel = ttk.Label(self.etimeFrame, text=STRS_PLAY_LABEL[3], width=8)
        self.etimeLabel.pack(side=tk.LEFT)
        self.etimeEntry = ttk.Entry(self.etimeFrame, textvariable=self.etimeStrVar)
        self.etimeEntry.pack(side=tk.LEFT)

        # rest time
        self.rtimeStrVar = tk.StringVar()
        self.rtimeFrame = ttk.Frame(self.top)
        self.rtimeFrame.pack(side=tk.TOP)
        self.rtimeLabel = ttk.Label(self.rtimeFrame, text=STRS_PLAY_LABEL[4], width=8)
        self.rtimeLabel.pack(side=tk.LEFT)
        self.rtimeEntry = ttk.Entry(self.rtimeFrame, textvariable=self.rtimeStrVar)
        self.rtimeEntry.pack(side=tk.LEFT)

        # price
        self.priceStrVar = tk.StringVar()
        self.priceFrame = ttk.Frame(self.top)
        self.priceFrame.pack(side=tk.TOP)
        self.priceLabel = ttk.Label(self.priceFrame, text=STRS_PLAY_LABEL[5], width=8)
        self.priceLabel.pack(side=tk.LEFT)
        self.priceEntry = ttk.Entry(self.priceFrame, textvariable=self.priceStrVar)
        self.priceEntry.pack(side=tk.LEFT)            
        
        self.lastFrame = ttk.Frame(self.top)
        self.lastFrame.pack(side=tk.BOTTOM)
        firstText = u''
        if(self.dtype == PLAY_DIALOG_ADD):
            firstText = STR_PLAY_ADD
            self.addButton = ttk.Button(self.lastFrame, text=firstText, command=self.add_confirm)
            self.addButton.pack(side=tk.LEFT)
        else:
            firstText = STR_PLAY_OK
            self.editButton = ttk.Button(self.lastFrame, text=firstText, command=self.edit_confirm)
            self.editButton.pack(side=tk.LEFT)            

        self.cancelButton = ttk.Button(self.lastFrame, text=STR_PLAY_CANCEL, command=self.close)
        self.cancelButton.pack(side=tk.LEFT)
        # 窗口居中
        util_center_dialog(self.top, self.root, self.width, self.height)
        return
    
    def _ui_init_del(self, title, dtype, wmain, play):
        self.wmain = wmain
        self.dtype = dtype
        self.title = title
        self.top.title(self.title)
        self.titleLabel = ttk.Label(self.top, text=self.title)
        self.titleLabel.pack(side=tk.TOP)

        warnText = u'是否删除播放项： ' + play.hallName
        self.WarnLabel = ttk.Label(self.top, text = warnText)
        self.WarnLabel.pack(side=tk.TOP)

        self.lastFrame = ttk.LabelFrame(self.top)
        self.lastFrame.pack(side=tk.BOTTOM)
        self.addButton = ttk.Button(self.lastFrame, text=STR_PLAY_DEL, command=self.del_confirm)
        self.addButton.pack(side=tk.LEFT)
        self.cancelButton = ttk.Button(self.lastFrame, text=STR_PLAY_CANCEL, command=self.close)
        self.cancelButton.pack(side=tk.LEFT)
        # 窗口居中
        util_center_dialog(self.top, self.root, self.width, self.height)
        return

        
    def open_add(self, wmain):
        dtype = PLAY_DIALOG_ADD
        title = STR_PLAY_TITLE_ADD
        self._ui_init_addedit(title, dtype, wmain)
        return

    def open_edit(self, wmain, name=None):
        dtype = PLAY_DIALOG_EDIT
        title = STR_PLAY_TITLE_EDIT
        self._ui_init_addedit(title, dtype, wmain, name)
        return

    def open_del(self, wmain, name):
        title = STR_PLAY_TITLE_DEL
        dtype = PLAY_DIALOG_DEL
        self._ui_init_del(title, dtype, wmain, name)
        return

    def add_confirm(self):
        hall_idx = self.hallCombo.current()
        movie_idx = self.movieCombo.current()
        stime = self.stimeStrVar.get().split(':')
        etime = self.etimeStrVar.get().split(':')
        play = CMMoviePlay()
        play.id = -1
        # hall referring vars
        play.hallID = gInfo.hall_list[hall_idx].id
        play.hallName = gInfo.hall_list[hall_idx].name
        # movie referring vars
        play.movieID = gInfo.movie_list[movie_idx].id
        play.movieName = gInfo.movie_list[movie_idx].name
        # time referring vars
        play.startTime = datetime.datetime(gInfo.date_focus.year,
                                  gInfo.date_focus.month,
                                  gInfo.date_focus.day,
                                  int(stime[0]),
                                  int(stime[1]),
                                  int(stime[2]))
        play.endTime = datetime.datetime(gInfo.date_focus.year,
                                  gInfo.date_focus.month,
                                  gInfo.date_focus.day,
                                  int(etime[0]),
                                  int(etime[1]),
                                  int(etime[2]))
        play.price = int(self.priceStrVar.get())
        self.wmain.play_add_confirm(play)
        self.top.destroy()
        return

    def edit_confirm(self):
        hall_idx = self.hallCombo.current()
        movie_idx = self.movieCombo.current()
        stime = self.stimeStrVar.get().split(':')
        etime = self.etimeStrVar.get().split(':')
        play = CMMoviePlay()
        play.id = -1
        # hall referring vars
        play.hallID = gInfo.hall_list[hall_idx].id
        play.hallName = gInfo.hall_list[hall_idx].name
        # movie referring vars
        play.movieID = gInfo.movie_list[movie_idx].id
        play.movieName = gInfo.movie_list[movie_idx].name
        # time referring vars
        play.startTime = datetime.datetime(gInfo.date_focus.year,
                                  gInfo.date_focus.month,
                                  gInfo.date_focus.day,
                                  int(stime[0]),
                                  int(stime[1]),
                                  int(stime[2]))
        play.endTime = datetime.datetime(gInfo.date_focus.year,
                                  gInfo.date_focus.month,
                                  gInfo.date_focus.day,
                                  int(etime[0]),
                                  int(etime[1]),
                                  int(etime[2]))
        play.price = int(self.priceStrVar.get())
        self.wmain.play_edit_confirm(play)
        self.top.destroy()
        return

    def del_confirm(self):
        self.wmain.play_del_confirm()
        self.top.destroy()
        return

    def close(self):
        self.top.destroy()
        return
