# -*- coding: utf-8 -*-

import Tkinter as tk
from CMGlobal import *
from CMUtil import *

HALL_DIALOG_ADD = 'add'
HALL_DIALOG_DEL = 'del'
HALL_DIALOG_EDIT = 'edit'

class HallDialog():
    add_name = ''
    edit_name = ''
    def __init__(self, parent):
        self.root = parent
        self.top = tk.Toplevel(parent)
        self.width = 300
        self.height = 150
        return

    def _ui_init_addedit(self, title, dtype):
        self.dtype = HALL_DIALOG_ADD
        self.title = title
        self.top.title(self.title)
        
        self.titleLabel = tk.Label(self.top, text=self.title)
        self.titleLabel.pack(side=tk.TOP)

        self.nameFrame = tk.LabelFrame(self.top)
        self.nameFrame.pack(side=tk.TOP)
        self.nameLabel = tk.Label(self.nameFrame, text=u'影厅名称：')
        self.nameLabel.pack(side=tk.LEFT)
        self.nameEntryBox = tk.Entry(self.nameFrame)
        self.nameEntryBox.pack(side=tk.LEFT)

        self.lastFrame = tk.LabelFrame(self.top)
        self.lastFrame.pack(side=tk.BOTTOM)
        firstText = u''
        if(self.dtype == HALL_DIALOG_ADD):
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
    
    def _ui_init_del(self, title, dtype):
        self.dtype = dtype
        self.title = title
        self.top.title(self.title)
        self.titleLabel = tk.Label(self.top, text=self.title)
        self.titleLabel.pack(side=tk.TOP)

        warnText = u'是否删除影厅： ' + u'XXXXX'
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
        dtype = HALL_DIALOG_ADD
        title = u'添加影厅'
        self._ui_init_addedit(title, dtype)
        return

    def open_edit(self, ginfo):
        dtype = HALL_DIALOG_EDIT
        title = u'编辑影厅'
        self._ui_init_addedit(title, dtype)
        return

    def open_del(self, ginfo):
        title = u'删除影厅'
        dtype = HALL_DIALOG_DEL
        self._ui_init_del(title, dtype)
        return

    def add_confirm(self):
        return

    def close(self):
        return
