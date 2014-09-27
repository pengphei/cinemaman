# -*- coding: utf-8 -*-

def util_center_win(win):
    sw = win.root.winfo_screenwidth()
    sh = win.root.winfo_screenheight()
    x = (sw-win.width)/2
    y = (sh-win.height)/2
    win.root.geometry('%dx%d+%d+%d' % (win.width,win.height,x,y))
    return

def util_center_dialog(dialog, root, width, height):
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw-width)/2
    y = (sh-height)/2
    dialog.geometry('%dx%d+%d+%d' % (width,height,x,y))   
