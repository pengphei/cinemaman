# -*- coding: utf-8 -*-

import Tkinter as tk

def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()

# Frame is container for other widgets
class CMApp(tk.Frame):
    left_width = 15
    right_width = 15
    center_width = 70
    width = 800
    height = 600
    
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.root = master
        # init ui elemets
        self._init_misc()
        self._init_menu()
        self._init_left(self.left_width)
        self._init_right(self.right_width)
        self._init_calender_list(self.center_width)
        
        
        # init ui data elements
        self._init_hall_list()
        self._init_movie_list()
        self._init_play_list()
        return

    def say_hi(self):
        print "hi there, everyone!"

        return
    def _init_menu(self):
        # Menu widget which displays a list of choice of MenuButton
        # choises includes:
        #   simple command
        #   cascade, string or image user can select to show another Menu includes choices list
        #   Checkbutton
        #   group of Radiobutton
        self.menuBar = tk.Menu(self.root)

        # file cascade
        self.fileMenu = tk.Menu(self.menuBar)
        self.fileMenu.add_command(label="新建", command=donothing)
        self.fileMenu.add_command(label="打开", command=donothing)
        self.fileMenu.add_command(label="保存", command=donothing)
        self.fileMenu.add_command(label="另存为...", command=donothing)
        self.fileMenu.add_command(label="关闭", command=donothing)

        self.fileMenu.add_separator()

        self.fileMenu.add_command(label="退出", command=self.root.quit)
        
        self.menuBar.add_cascade(label="文件", menu=self.fileMenu)
        
        # movie hall cascade
        self.hallMenu = tk.Menu(self.menuBar)
        self.hallMenu.add_command(label="添加", command=donothing)
        self.hallMenu.add_command(label="删除", command=donothing)
        self.hallMenu.add_command(label="编辑", command=donothing)
        self.menuBar.add_cascade(label="电影厅", menu=self.hallMenu)

        # movie cascade
        self.movieMenu = tk.Menu(self.menuBar)
        self.movieMenu.add_command(label="添加", command=donothing)
        self.movieMenu.add_command(label="删除", command=donothing)
        self.movieMenu.add_command(label="编辑", command=donothing)
        self.menuBar.add_cascade(label="电影", menu=self.movieMenu)

        # help cascade
        self.helpMenu = tk.Menu(self.menuBar)
        self.helpMenu.add_command(label="帮助", command=donothing)
        self.menuBar.add_cascade(label="帮助", menu=self.helpMenu)
        self.master.config(menu=self.menuBar)
        return
    
    def _init_misc(self):
        # title
        self.root.title('cineman')
        # pack
        self.pack(fill=tk.BOTH, expand=1)

        # centered window
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x = (sw-self.width)/2
        y = (sh-self.height)/2
        self.root.geometry('%dx%d+%d+%d' % (self.width,self.height,x,y))
        return

    def _init_left(self, w):
        self.hallFrame = tk.LabelFrame(self, width = w, borderwidth = 2, bg='light blue')
        self.hallFrame.pack(fill=tk.Y, side=tk.LEFT)
        
        self.hallList = tk.Listbox(self.hallFrame, width=w, selectmode=tk.SINGLE, bg='light blue')
        self.hallList.pack(fill=tk.Y, side=tk.LEFT)
        return

    def _init_right(self, w):
        self.movieFrame = tk.LabelFrame(self, width=w, borderwidth=2, bg='light green')
        self.movieFrame.pack(fill=tk.Y, side=tk.RIGHT)
        
        self.movielist = tk.Listbox(self.movieFrame, width=w, selectmode=tk.SINGLE, bg='light green')
        self.movielist.pack(fill=tk.Y, side=tk.RIGHT)
        pass

    def _init_calender_list(self, w):
        self.calenderFrame = tk.LabelFrame(self, width=w, borderwidth=2, bg='light gray')
        self.calenderFrame.pack(fill=tk.X, side=tk.TOP)
        
        # init center canender list
        self.calender_list = []
        
        # init left arrow
        self.calender_minus_button = tk.Button(self.calenderFrame, text = '<', fg='red', width=2, height = 5, command=self._calender_minus)
        self.calender_minus_button.pack(side=tk.LEFT)
        
        for i in range(5):
            button = tk.Button(self.calenderFrame, text="2014-09-08", fg="red", height = 5, command=self.root.quit)
            button.pack(fill=tk.X, side=tk.LEFT)
            self.calender_list.append(button)
            
        # init right arrow
        self.calender_plus_button = tk.Button(self.calenderFrame, text = '>', fg='red', width = 2, height = 5, command=self._calender_minus)
        self.calender_plus_button.pack(side=tk.RIGHT)
        
        pass
    
    def _init_hall_list(self):
        # add hall
        self.hallList.insert(0, "一号厅")
        self.hallList.insert(1, "二号厅")
        self.hallList.insert(2, "三号厅")
        self.hallList.insert(3, "四号厅")
        self.hallList.insert(4, "五号厅")
        return
    
    def _init_movie_list(self):
        # add movie
        self.movielist.insert(0, "盗马记")
        self.movielist.insert(1, "极品飞车3D")
        self.movielist.insert(2, "盟军夺宝队")
        self.movielist.insert(3, "天才眼镜狗3D")
        self.movielist.insert(4, "我在路上最爱你")
        pass
    
    def _init_play_list(self):
        pass
    
    def _calender_minus(self):
        pass
    
    def _calender_plus(self):
        pass
        

if __name__ == "__main__":
    root = tk.Tk()
    app = CMApp(root)
    root.mainloop()
    root.destroy()
