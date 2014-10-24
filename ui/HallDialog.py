# -*- coding: utf-8 -*-

import Tkinter as tk
from CMGlobal import *
from CMUtil import *

HALL_DIALOG_ADD = 'add'
HALL_DIALOG_DEL = 'del'
HALL_DIALOG_EDIT = 'edit'

STR_HALL_LABEL_NAME = u'影厅名称：'
STR_HALL_ADD = u'添加'
STR_HALL_OK = u'确定'
STR_HALL_CANCEL = u'取消'
STR_HALL_DEL = u'删除'
STR_HALL_TITLE_ADD = u'添加影厅'
STR_HALL_TITLE_EDIT = u'编辑影厅'
STR_HALL_TITLE_DEL = u'删除影厅'

class HallDialog():
    add_name = ''
    edit_name = ''
    def __init__(self, parent):
        self.root = parent
        self.top = tk.Toplevel(parent)
        self.width = 300
        self.height = 150
        return

    def _ui_init_addedit(self, title, dtype, wmain, name=None):
        self.wmain = wmain
        self.dtype = HALL_DIALOG_ADD
        self.title = title
        self.top.title(self.title)
        
        self.titleLabel = tk.Label(self.top, text=self.title)
        self.titleLabel.pack(side=tk.TOP)
        
        self.nameVar = tk.StringVar()
        
        if(name != None):
            self.nameVar.set(name)

        self.nameFrame = tk.LabelFrame(self.top)
        self.nameFrame.pack(side=tk.TOP)
        self.nameLabel = tk.Label(self.nameFrame, text=STR_HALL_LABEL_NAME)
        self.nameLabel.pack(side=tk.LEFT)
        self.nameEntry = tk.Entry(self.nameFrame, textvariable=self.nameVar)
        self.nameEntry.pack(side=tk.LEFT)

        self.lastFrame = tk.LabelFrame(self.top)
        self.lastFrame.pack(side=tk.BOTTOM)
        firstText = u''
        if(self.dtype == HALL_DIALOG_ADD):
            firstText = STR_HALL_ADD
            self.addButton = tk.Button(self.lastFrame, text=firstText, command=self.add_confirm)
            self.addButton.pack(side=tk.LEFT)
        else:
            firstText = STR_HALL_OK
            self.editButton = tk.Button(self.lastFrame, text=firstText, command=self.edit_confirm)
            self.editButton.pack(side=tk.LEFT)            

        self.cancelButton = tk.Button(self.lastFrame, text=STR_HALL_CANCEL, command=self.close)
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

        warnText = u'是否删除影厅： ' + name
        self.WarnLabel = tk.Label(self.top, text = warnText)
        self.WarnLabel.pack(side=tk.TOP)

        self.lastFrame = tk.LabelFrame(self.top)
        self.lastFrame.pack(side=tk.BOTTOM)
        self.addButton = tk.Button(self.lastFrame, text=STR_HALL_DEL, command=self.del_confirm)
        self.addButton.pack(side=tk.LEFT)
        self.cancelButton = tk.Button(self.lastFrame, text=STR_HALL_CANCEL, command=self.close)
        self.cancelButton.pack(side=tk.LEFT)
        # 窗口居中
        util_center_dialog(self.top, self.root, self.width, self.height)
        return

        
    def open_add(self, wmain):
        dtype = HALL_DIALOG_ADD
        title = STR_HALL_TITLE_ADD
        self._ui_init_addedit(title, dtype, wmain)
        return

    def open_edit(self, wmain, name=None):
        dtype = HALL_DIALOG_EDIT
        title = STR_HALL_TITLE_EDIT
        self._ui_init_addedit(title, dtype, wmain, name)
        return

    def open_del(self, wmain, name):
        title = STR_HALL_TITLE_DEL
        dtype = HALL_DIALOG_DEL
        self._ui_init_del(title, dtype, wmain, name)
        return

    def add_confirm(self):
        hall = CMHall()
        hall.id = -1
        hall.name = self.nameVar.get()
        self.wmain.hall_add_confirm(hall)
        self.top.destroy()
        return

    def edit_confirm(self):
        hall = CMHall()
        hall.id = -1
        hall.name = self.nameVar.get()
        self.wmain.hall_edit_confirm(hall)
        self.top.destroy()
        return

    def del_confirm(self):
        self.wmain.hall_del_confirm()
        self.top.destroy()
        return

    def close(self):
        self.top.destroy()
        return
