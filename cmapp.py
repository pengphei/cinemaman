# -*- coding: utf-8 -*-
import Tkinter as tk

def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()

# Frame is container for other widgets
class CMApp(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.root = master
        self._init_misc()
        self._init_menu()
        self._init_left()
        self._init_center()
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
        self.menuBar.add_cascade(label="电影厅", menu=self.fileMenu)

        # movie cascade
        self.menuBar.add_cascade(label="电影", menu=self.fileMenu)

        # help cascade
        self.menuBar.add_cascade(label="帮助", menu=self.fileMenu)
        self.master.config(menu=self.menuBar)
        return
    
    def _init_misc(self):
        # title
        self.root.title('cineman')
        # pack
        self.pack(fill=tk.BOTH, expand=1)

        # centered window
        w = 800
        h = 600
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x = (sw-w)/2
        y = (sh-h)/2
        self.root.geometry('%dx%d+%d+%d' % (w,h,x,y))
        return

    def _init_left(self):
        self.hallList = tk.Listbox(self, selectmode=tk.SINGLE, bg='gray')
        self.hallList.pack(fill=tk.Y, side=tk.LEFT)

        # add sample hall
        self.hallList.insert(0, "一号厅")
        self.hallList.insert(1, "二号厅")
        self.hallList.insert(2, "三号厅")
        self.hallList.insert(3, "四号厅")
        self.hallList.insert(4, "五号厅")
        return

    def _init_right(self):
        pass

    def _init_center(self):
        self.button = tk.Button(self, text="QUIT", fg="red", command=self.root.quit)
        self.button.pack(side=tk.LEFT)

        self.hi_there = tk.Button(self, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=tk.LEFT)
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = CMApp(root)
    root.mainloop()
    root.destroy()
