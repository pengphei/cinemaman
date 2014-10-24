# -*- coding: utf-8 -*-

import Tkinter as tk

from CMApp import *

class CMHallListView():

    def __init__(self, root, parent, w):
        self.root = root
        self.parent = parent
        self.hallStrVar = tk.StringVar()
        self.hallFrame = tk.LabelFrame(self.parent, width = w, borderwidth = 2, bg='light gray')
        self.hallFrame.pack(fill=tk.Y, side=tk.LEFT)

        self.hallTitle = tk.Label(self.hallFrame, text = u"电影厅列表", width=w, bg='light gray')
        self.hallTitle.pack(fill=tk.X, side=tk.TOP)
        
        self.hallList = tk.Listbox(self.hallFrame, width=w, listvariable=self.hallStrVar, selectmode=tk.SINGLE, bg='light blue')
        self.hallList.pack(fill=tk.BOTH, side=tk.TOP)

        # hall list key bindings
        self.hallList.bind('<ButtonRelease-1>', self.hall_single_click)
        self.hallList.bind('<Double-ButtonRelease-1>', self.hall_double_click)
        
        self.hallToolsFrame = tk.LabelFrame(self.hallFrame, width=w, bg='light gray')
        self.hallToolsFrame.pack(fill=tk.Y, side=tk.BOTTOM)
        self.hallToolAdd = tk.Button(self.hallToolsFrame, text = '添加', command=self.hall_add)
        self.hallToolAdd.pack(fill=tk.Y, side=tk.LEFT)
        self.hallToolDel = tk.Button(self.hallToolsFrame, text = '删除', command=self.hall_del)
        self.hallToolDel.pack(fill=tk.Y, side=tk.LEFT)
        self.hallToolEdit = tk.Button(self.hallToolsFrame, text = '编辑', command=self.hall_edit)
        self.hallToolEdit.pack(fill=tk.Y, side=tk.LEFT)

        self.hall_list_update()
        return

    def hall_list_update(self):
        halls = []
        # add hall
        for hall in gInfo.hall_list:
            halls.append(hall.name)
        self.hallStrVar.set(tuple(halls))
        return

    def hall_single_click(self, event):
        idxs = self.hallList.curselection()
        if(len(idxs) == 0):
            return
        gInfo.hall_focus = idxs[0]
        self.focus_hall = gInfo.hall_list[gInfo.hall_focus]
        print("hall single click")
        print(self.focus_hall.name)
        return
    
    def hall_double_click(self, event):
        idxs = self.hallList.curselection()
        if(len(idxs) == 0):
            return
        gInfo.hall_focus = idxs[0]
        self.focus_hall = gInfo.hall_list[gInfo.hall_focus]
        print("hall double click")
        print(self.focus_hall.name)
        self.hall_edit()
        return
    
    def hall_add(self):
        """ add hall """
        dialog = HallDialog(self.root)
        dialog.open_add(self)
        return

    def hall_del(self):
        """ dell hall """
        dialog = HallDialog(self.root)
        dialog.open_del(self, self.focus_hall.name)
        return

    def hall_edit(self):
        """ edit hall """
        dialog = HallDialog(self.root)
        dialog.open_edit(self, self.focus_hall.name)
        return

    def hall_add_confirm(self, hall):
        print hall.name
        hall.id = gInfo.db_hall.add(gInfo.db.conn, hall)
        gInfo.hall_list.append(hall);
        self.hall_list_update()
        return

    def hall_edit_comfirm(self, hall):
        if(len(gInfo.hall_list) == 0 or gInfo.hall_focus == -1):
            return
        
        hall_old = gInfo.movie_list[gInfo.hall_focus]
        hall.id = hall_old.id
        gInfo.db_hall.edit(gInfo.db.conn, hall)
        gInfo.hall_list[gInfo.hall_focus] = hall
        self.hall_list_update()
        return

    def hall_del_confirm(self):
        if(len(gInfo.hall_list) == 0 or gInfo.hall_focus == -1):
            return
        
        hall_del = gInfo.hall_list[gInfo.hall_focus]
        gInfo.db_hall.delete(gInfo.db.conn, hall_del)
        gInfo.hall_list.pop(gInfo.hall_focus)

        last = len(gInfo.hall_list) - 1
        
        if(gInfo.hall_focus > last):
            gInfo.hall_focus = last
        self.hall_list_update()        
        return
