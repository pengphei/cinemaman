# -*- coding: utf-8 -*-

import Tkinter as tk

from CMApp import *

class CMMovieListView():

    def __init__(self, root, parent, w):
        self.root = root
        self.parent = parent
        self.movieStrVar = tk.StringVar()
        self.movieFrame = tk.LabelFrame(self.parent, width=w, borderwidth=2, bg='light gray')
        self.movieFrame.pack(fill=tk.Y, side=tk.RIGHT)

        self.movieTitle = tk.Label(self.movieFrame, text = u"电影列表", width=w, bg='light gray')
        self.movieTitle.pack(fill=tk.X, side=tk.TOP)
        self.movieList = tk.Listbox(self.movieFrame, width=w, listvariable=self.movieStrVar, selectmode=tk.SINGLE, bg='light green')
        self.movieList.pack(fill=tk.BOTH, side=tk.TOP)

        # movie list key bindings
        self.movieList.bind('<ButtonRelease-1>', self.movie_single_click)
        self.movieList.bind('<Double-ButtonRelease-1>', self.movie_double_click)

        self.movieToolsFrame = tk.LabelFrame(self.movieFrame, width=w, bg='light gray')
        self.movieToolsFrame.pack(fill=tk.Y, side=tk.BOTTOM)
        self.movieToolAdd = tk.Button(self.movieToolsFrame, text = '添加', command=self.movie_add)
        self.movieToolAdd.pack(fill=tk.Y, side=tk.LEFT)
        self.movieToolDel = tk.Button(self.movieToolsFrame, text = '删除', command=self.movie_del)
        self.movieToolDel.pack(fill=tk.Y, side=tk.LEFT)
        self.movieToolEdit = tk.Button(self.movieToolsFrame, text = '编辑', command=self.movie_edit)
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
        dialog.open_edit(self)
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
