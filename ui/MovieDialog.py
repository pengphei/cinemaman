# -*- coding: utf-8 -*-

import Tkinter as tk
from CMGlobal import *
from CMUtil import *

MOVIE_DIALOG_ADD = 'add'
MOVIE_DIALOG_DEL = 'del'
MOVIE_DIALOG_EDIT = 'edit'

class MovieDialog:
    add_name = ''
    edit_name = ''
    def __init__(self, parent):
        self.root = parent
        self.top = tk.Toplevel(parent)
        self.width = 300
        self.height = 150
        return

    def _ui_init_addedit(self, title, dtype):
        self.dtype = dtype
        self.title = title
        self.top.title(self.title)
        
        self.titleLabel = tk.Label(self.top, text=self.title)
        self.titleLabel.pack(side=tk.TOP)

        self.nameFrame = tk.LabelFrame(self.top)
        self.nameFrame.pack(side=tk.TOP)
        self.nameLabel = tk.Label(self.nameFrame, text=u'电影名称：')
        self.nameLabel.pack(side=tk.LEFT)
        self.nameEntryBox = tk.Entry(self.nameFrame)
        self.nameEntryBox.pack(side=tk.LEFT)

        self.durationFrame = tk.LabelFrame(self.top)
        self.durationFrame.pack(side=tk.TOP)
        self.durationLabel = tk.Label(self.durationFrame, text=u'电影时长：')
        self.durationLabel.pack(side=tk.LEFT)
        self.durationEntryBox = tk.Entry(self.durationFrame)
        self.durationEntryBox.pack(side=tk.LEFT)

        self.langFrame = tk.LabelFrame(self.top)
        self.langFrame.pack(side=tk.TOP)
        self.langLabel = tk.Label(self.langFrame, text=u'电影语言：')
        self.langLabel.pack(side=tk.LEFT)
        self.langEntryBox = tk.Entry(self.langFrame)
        self.langEntryBox.pack(side=tk.LEFT)

        self.TypeFrame = tk.LabelFrame(self.top)
        self.TypeFrame.pack(side=tk.TOP)
        self.TypeLabel = tk.Label(self.TypeFrame, text=u'电影类型：')
        self.TypeLabel.pack(side=tk.LEFT)
        self.TypeEntryBox = tk.Entry(self.TypeFrame)
        self.TypeEntryBox.pack(side=tk.LEFT)

        self.lastFrame = tk.LabelFrame(self.top)
        self.lastFrame.pack(side=tk.BOTTOM)
        firstText = u''
        if(self.dtype == MOVIE_DIALOG_ADD):
            firstText = u'添加'
        else:
            firstText = u'确定'
            
        self.addButton = tk.Button(self.lastFrame, text=firstText, command=self.add_confirm)
        self.addButton.pack(side=tk.LEFT)
        self.cancelButton = tk.Button(self.lastFrame, text=u'取消', command=self.close)
        self.cancelButton.pack(side=tk.LEFT)
        # 窗口居中
        util_center_dialog(self.top, self.root, self.width, self.height)
        return

    def _ui_init_del(self, title, dtype, ginfo):
        self.dtype = dtype
        self.title = title
        self.top.title(self.title)
        self.titleLabel = tk.Label(self.top, text=self.title)
        self.titleLabel.pack(side=tk.TOP)

        warnText = u'是否删除电影： ' + u'XXXXX'
        self.WarnLabel = tk.Label(self.top, text = warnText)
        self.WarnLabel.pack(side=tk.TOP)

        self.lastFrame = tk.LabelFrame(self.top)
        self.lastFrame.pack(side=tk.BOTTOM)
        self.addButton = tk.Button(self.lastFrame, text=u'删除', command=self.add_confirm)
        self.addButton.pack(side=tk.LEFT)
        self.cancelButton = tk.Button(self.lastFrame, text=u'取消', command=self.close)
        self.cancelButton.pack(side=tk.LEFT)
        # 窗口居中
        util_center_dialog(self.top, self.root, self.width, self.height)
        return

    def open_add(self, ginfo):
        title = u'添加电影'
        dtype = MOVIE_DIALOG_ADD
        self._ui_init_addedit(title, dtype)
        return

    def open_edit(self, ginfo):
        title = u'编辑电影'
        dtype = MOVIE_DIALOG_EDIT
        self._ui_init_addedit(title, dtype)
        return

    def open_del(self, ginfo):
        title = u'删除电影'
        dtype = MOVIE_DIALOG_DEL
        self._ui_init_del(title, dtype, ginfo)
        return

    def add_confirm(self):
        return

    def edit_confirm(self):
        return

    def close(self):
        return
