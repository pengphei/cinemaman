# -*- coding: utf-8 -*-

import Tkinter as tk
from CMGlobal import *
from CMUtil import *

MOVIE_DIALOG_ADD = 'add'
MOVIE_DIALOG_DEL = 'del'
MOVIE_DIALOG_EDIT = 'edit'

STR_MOVIE_LABEL_NAME = u'电影名称：'
STR_MOVIE_LABEL_DURATION = u'电影时长：'
STR_MOVIE_LABEL_LANG = u'电影语言：'
STR_MOVIE_LABEL_TYPE = u'电影类型：'
STR_MOVIE_LABEL_PRICE = u'基本价格：'
STR_MOVIE_ADD = u'添加'
STR_MOVIE_OK = u'确定'
STR_MOVIE_CANCEL = u'取消'
STR_MOVIE_DEL = u'删除'
STR_MOVIE_TITLE_ADD = u'添加电影'
STR_MOVIE_TITLE_EDIT = u'编辑电影'
STR_MOVIE_TITLE_DEL = u'删除电影'

class MovieDialog:
    def __init__(self, parent):
        self.root = parent
        self.top = tk.Toplevel(parent)
        self.width = 300
        self.height = 180
        return

    def _ui_init_addedit(self, title, dtype, wmain, movie=None):
        self.wmain = wmain
        self.dtype = dtype
        self.title = title
        self.top.title(self.title)
        
        self.titleLabel = tk.Label(self.top, text=self.title)
        self.titleLabel.pack(side=tk.TOP)

        self.nameVar = tk.StringVar()
        self.durationVar = tk.StringVar()
        self.langVar = tk.StringVar()
        self.typeVar = tk.StringVar()
        self.priceVar = tk.StringVar()

        if(movie != None):
            self.nameVar.set(movie.name)
            self.durationVar.set(movie.duration)
            self.langVar.set(movie.lang)
            self.typeVar.set(movie.type)
            self.priceVar.set(movie.price)
            
        self.nameFrame = tk.LabelFrame(self.top)
        self.nameFrame.pack(side=tk.TOP)
        self.nameLabel = tk.Label(self.nameFrame, text=STR_MOVIE_LABEL_NAME)
        self.nameLabel.pack(side=tk.LEFT)
        self.nameEntry = tk.Entry(self.nameFrame, textvariable=self.nameVar)
        self.nameEntry.pack(side=tk.LEFT)

        self.durationFrame = tk.LabelFrame(self.top)
        self.durationFrame.pack(side=tk.TOP)
        self.durationLabel = tk.Label(self.durationFrame, text=STR_MOVIE_LABEL_DURATION)
        self.durationLabel.pack(side=tk.LEFT)
        self.durationEntry = tk.Entry(self.durationFrame, textvariable=self.durationVar)
        self.durationEntry.pack(side=tk.LEFT)

        self.langFrame = tk.LabelFrame(self.top)
        self.langFrame.pack(side=tk.TOP)
        self.langLabel = tk.Label(self.langFrame, text=STR_MOVIE_LABEL_LANG)
        self.langLabel.pack(side=tk.LEFT)
        self.langEntry = tk.Entry(self.langFrame, textvariable=self.langVar)
        self.langEntry.pack(side=tk.LEFT)
        
        self.typeFrame = tk.LabelFrame(self.top)
        self.typeFrame.pack(side=tk.TOP)
        self.typeLabel = tk.Label(self.typeFrame, text=STR_MOVIE_LABEL_TYPE)
        self.typeLabel.pack(side=tk.LEFT)
        self.typeEntry = tk.Entry(self.typeFrame, textvariable=self.typeVar)
        self.typeEntry.pack(side=tk.LEFT)

        self.priceFrame = tk.LabelFrame(self.top)        
        self.priceFrame.pack(side=tk.TOP)
        self.priceLabel = tk.Label(self.priceFrame, text=STR_MOVIE_LABEL_PRICE)
        self.priceLabel.pack(side=tk.LEFT)
        self.priceEntry = tk.Entry(self.priceFrame, textvariable=self.priceVar)
        self.priceEntry.pack(side=tk.LEFT)
        
        self.lastFrame = tk.LabelFrame(self.top)
        self.lastFrame.pack(side=tk.BOTTOM)
        firstText = u''
        if(self.dtype == MOVIE_DIALOG_ADD):
            firstText = STR_MOVIE_ADD
            self.addButton = tk.Button(self.lastFrame, text=firstText, command=self.add_confirm)
            self.addButton.pack(side=tk.LEFT)
        else:
            firstText = STR_MOVIE_OK
            self.addButton = tk.Button(self.lastFrame, text=firstText, command=self.edit_confirm)
            self.addButton.pack(side=tk.LEFT)
            
        self.cancelButton = tk.Button(self.lastFrame, text=STR_MOVIE_CANCEL, command=self.close)
        self.cancelButton.pack(side=tk.LEFT)

        # 窗口居中
        util_center_dialog(self.top, self.root, self.width, self.height)
        return

    def _ui_init_del(self, title, dtype, wmain, name):
        self.wmain = wmain
        self.dtype = dtype
        self.title = title
        self.top.title(self.title)
        self.titleLabel = tk.Label(self.top, text=self.title)
        self.titleLabel.pack(side=tk.TOP)

        warnText = u'是否删除电影： ' + name
        self.WarnLabel = tk.Label(self.top, text = warnText)
        self.WarnLabel.pack(side=tk.TOP)

        self.lastFrame = tk.LabelFrame(self.top)
        self.lastFrame.pack(side=tk.BOTTOM)
        self.addButton = tk.Button(self.lastFrame, text=STR_MOVIE_DEL, command=self.del_confirm)
        self.addButton.pack(side=tk.LEFT)
        self.cancelButton = tk.Button(self.lastFrame, text=STR_MOVIE_CANCEL, command=self.close)
        self.cancelButton.pack(side=tk.LEFT)
        # 窗口居中
        util_center_dialog(self.top, self.root, self.width, self.height)
        return

    def open_add(self, wmain):
        title = STR_MOVIE_TITLE_ADD
        dtype = MOVIE_DIALOG_ADD
        self._ui_init_addedit(title, dtype, wmain, None)
        return

    def open_edit(self, wmain, movie=None):
        self.wmain = wmain
        title = STR_MOVIE_TITLE_EDIT
        dtype = MOVIE_DIALOG_EDIT
        self._ui_init_addedit(title, dtype, wmain, movie)
        return

    def open_del(self, wmain, name):
        title = STR_MOVIE_TITLE_DEL
        dtype = MOVIE_DIALOG_DEL
        self._ui_init_del(title, dtype, wmain, name)
        return

    def add_confirm(self):
        movie = CMMovie()
        movie.id = -1
        movie.name = self.nameVar.get()
        movie.duration = self.durationVar.get()
        movie.lang = self.langVar.get()
        movie.type = self.typeVar.get()
        movie.price = self.priceVar.get()
        self.wmain.movie_add_confirm(movie)
        self.top.destroy()
        return

    def edit_confirm(self):
        movie = CMMovie()
        movie.id = -1
        movie.name = self.nameVar.get()
        movie.duration = self.durationVar.get()
        movie.lang = self.langVar.get()
        movie.type = self.typeVar.get()
        movie.price = self.priceVar.get()
        self.wmain.movie_edit_confirm(movie)
        self.top.destroy()
        return

    def del_confirm(self):
        self.wmain.movie_del_confirm()
        self.top.destroy()
        return

    def close(self):
        self.top.destroy()
        return
