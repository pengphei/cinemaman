# -*- coding: utf-8 -*-

import Tkinter as tk
import ttk

from CMApp import *

class CMMovieListView(ttk.Frame):

    def __init__(self, root, parent, width_):
        ttk.Frame.__init__(self, parent, class_="CMMovieListView", width=width_)
        self.root = root
        self.parent = parent
        self.width = width_
        self._setup_widgets()
        return
    def _setup_widgets(self):
        self.movieStrVar = tk.StringVar()

        self.movieTitle = ttk.Label(self, text = u"电影列表", width=self.width)
        self.movieTitle.pack(fill=tk.X, side=tk.TOP)
        self.movieList = tk.Listbox(self, width=self.width, listvariable=self.movieStrVar, selectmode=tk.SINGLE, bg='light green')
        self.movieList.pack(fill=tk.BOTH, side=tk.TOP)

        # movie list key bindings
        self.movieList.bind('<ButtonRelease-1>', self.movie_single_click)
        self.movieList.bind('<Double-ButtonRelease-1>', self.movie_double_click)

        self.movieToolsFrame = ttk.Frame(self, width=self.width)
        self.movieToolsFrame.pack(fill=tk.Y, side=tk.BOTTOM)
        self.movieToolAdd = ttk.Button(self.movieToolsFrame, text = '添加', command=self.movie_add)
        self.movieToolAdd.pack(fill=tk.Y, side=tk.LEFT)
        self.movieToolDel = ttk.Button(self.movieToolsFrame, text = '删除', command=self.movie_del)
        self.movieToolDel.pack(fill=tk.Y, side=tk.LEFT)
        self.movieToolEdit = ttk.Button(self.movieToolsFrame, text = '编辑', command=self.movie_edit)
        self.movieToolEdit.pack(fill=tk.Y, side=tk.LEFT)

        self.movie_list_update()
        return
        
    def movie_list_update(self):
        # add movie
        movies = []
        for idx in range(len(gInfo.movie_list)):
            movies.append(gInfo.movie_list[idx].name)
        self.movieStrVar.set(tuple(movies))
        return
    
    def movie_single_click(self, event):
        idxs = self.movieList.curselection()
        if(len(idxs) == 0):
            return
        gInfo.movie_focus = idxs[0]
        self.focus_movie = gInfo.movie_list[gInfo.movie_focus]
        print("movie single click")
        print(self.focus_movie.name)
        return

    def movie_double_click(self, event):
        idxs = self.movieList.curselection()
        if(len(idxs) == 0):
            return
        gInfo.movie_focus = idxs[0]
        self.focus_movie = gInfo.movie_list[gInfo.movie_focus]
        print("mocie double click")
        print(self.focus_movie.name)
        self.movie_edit()
        return
    
    def movie_add(self):
        dialog = MovieDialog(self.root)
        dialog.open_add(self)
        return

    def movie_del(self):
        if(len(gInfo.movie_list) == 0 or gInfo.movie_focus == -1):
            return
        
        dialog = MovieDialog(self.root)
        dialog.open_del(self, self.focus_movie.name)
        return

    def movie_edit(self):
        if(len(gInfo.movie_list) == 0 or gInfo.movie_focus == -1):
            return
        
        dialog = MovieDialog(self.root)
        dialog.open_edit(self, self.focus_movie)
        return

    def movie_add_confirm(self, movie):
        movie.id = gInfo.db_movie.add(gInfo.db.conn, movie)
        gInfo.movie_list.append(movie);
        self.movie_list_update()
        return

    def movie_edit_confirm(self, movie):
        if(len(gInfo.movie_list) == 0 or gInfo.movie_focus == -1):
            return
        
        movie_old = gInfo.movie_list[gInfo.movie_focus]
        movie.id = movie_old.id
        gInfo.db_movie.edit(gInfo.db.conn, movie)
        gInfo.movie_list[gInfo.movie_focus] = movie
        self.movie_list_update()
        return

    def movie_del_confirm(self):
        if(len(gInfo.movie_list) == 0 or gInfo.movie_focus == -1):
            return
        
        movie_del = gInfo.movie_list[gInfo.movie_focus]
        gInfo.db_movie.delete(gInfo.db.conn, movie_del)
        gInfo.movie_list.pop(gInfo.movie_focus)

        last = len(gInfo.movie_list) - 1
        
        if(gInfo.movie_focus > last):
            gInfo.movie_focus = last
        self.movie_list_update()
        return
