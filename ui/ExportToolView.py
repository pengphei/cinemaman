# -*- coding: utf-8 -*-

import Tkinter as tk
import tkFont
import ttk

from CMApp import *

class CMExportToolView:
    """
        export excel table tool view
    """

    def __init__(self, root, parent, width, bgcolor=None):
        self.root = root
        self.parent = parent
        self.width = width
        self._setup_widgets()
        return

    def _setup_widgets(self):
        self.frame = ttk.Frame(self.parent, width=self.width)
        self.frame.pack(fill=tk.BOTH, side=tk.TOP)
        self.ToolAdd = ttk.Button(self.frame, text = '导出本天排表', command=self._export_this_day)
        self.ToolAdd.pack(fill=tk.X, side=tk.TOP)
        self.ToolDel = ttk.Button(self.frame, text = '导出本天单影片排表', command=self._export_this_day_movie)
        self.ToolDel.pack(fill=tk.X, side=tk.TOP)
        self.ToolEdit = ttk.Button(self.frame, text = '导出本天影厅拍表', command=self._export_this_day_hall)
        self.ToolEdit.pack(fill=tk.X, side=tk.TOP)
        return

    def _export_this_week(self):
        return

    def _export_this_day(self):
        return

    def _export_this_day_movie(self):
        return

    def _export_this_day_hall(self):
        return
