# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 15:27:50 2014

@author: kurain
"""

# global import
from xlwt import *

# local import

# global vars
header_name = u"按片名排序"
header_names = [
    u"片名",
    u"开始",
    u"结束",
    u"厅号",
]

# unit alignment
unit_align = Alignment()
unit_align.horz = unit_align.HORZ_CENTER
unit_align.vert = unit_align.VERT_CENTER
# unit border
unit_border = Borders()
unit_border.top = unit_border.THIN
unit_border.left = unit_border.THIN
unit_border.right = unit_border.THIN
unit_border.bottom = unit_border.THIN
# unit style
unit_style = XFStyle()
unit_style.alignment = unit_align
unit_style.borders = unit_border

title_pat = Pattern()
title_pat.pattern = title_pat.SOLID_PATTERN
# set color to light green (0x2A)
title_pat.pattern_fore_colour = 0x2A
title_pat.pattern_back_colour = 0x2A
# title style
title_style = XFStyle()
title_style.alignment = unit_align
title_style.borders = unit_border
title_style.pattern = title_pat

class CMXlsVerTable():
    
    def __init__(self, wsheet, row, coloumn):
        self.fwsheet = wsheet
        self.row = row
        self.col = coloumn
        self.row_focus = row
        self.col_focus = coloumn
        return
    
    def init(self, title=u"排序", playmax=100):
        global unit_style
        global title_style
        
        self.title = title
        self.play_num = 0
        self.play_max = playmax
        
        # write title merging excel unit table
        self.fwsheet.write_merge(self.row_focus, self.row_focus+1, self.col_focus, self.col_focus+3, self.title, unit_style)
        # write table header
        self.row_focus = self.row_focus + 2
        
        self.fwsheet.write(self.row_focus, self.col_focus+0, header_names[0], title_style)
        self.fwsheet.write(self.row_focus, self.col_focus+1, header_names[1], title_style)
        self.fwsheet.write(self.row_focus, self.col_focus+2, header_names[2], title_style)
        self.fwsheet.write(self.row_focus, self.col_focus+3, header_names[3], title_style)
        
        self.row_focus = self.row_focus + 1
        return
    
    def add_movie(self, name=u"电影", starttime=u"00:00", endtime=u"00:00", id=0):
        global unit_style
        self.fwsheet.write(self.row_focus, self.col_focus+0, name, unit_style)
        self.fwsheet.write(self.row_focus, self.col_focus+1, starttime, unit_style)
        self.fwsheet.write(self.row_focus, self.col_focus+2, endtime, unit_style)
        self.fwsheet.write(self.row_focus, self.col_focus+3, str(id), unit_style)
        self.row_focus = self.row_focus + 1
        self.play_num = self.play_num + 1
        return
    
    def fini(self):
        global unit_style
        # fill last empty film units
        for idx in range(self.play_num, self.play_max):
            self.fwsheet.write(self.row_focus, self.col_focus+0, '', unit_style)
            self.fwsheet.write(self.row_focus, self.col_focus+1, '', unit_style)
            self.fwsheet.write(self.row_focus, self.col_focus+2, '', unit_style)
            self.fwsheet.write(self.row_focus, self.col_focus+3, '', unit_style)
            self.row_focus = self.row_focus + 1
        return
        
# for test
if __name__ == "__main__":
    fwbook = Workbook('utf-8')
    range_sheet = fwbook.add_sheet(u"竖版片表")
    
    vertable = CMXlsVerTable(range_sheet, 0, 0)
    vertable.init(u"按片名排序")
    for ii in range(30):
        vertable.add_movie()
    vertable.fini()

    vertable1 = CMXlsVerTable(range_sheet, 0, 5)
    vertable1.init(u"按时间排序")
    for ii in range(30):
        vertable1.add_movie() 
    vertable1.fini()
    
    fwbook.save(u"test_竖版排片表.xls")