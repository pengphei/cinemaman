# -*- coding: utf-8 -*-
"""
Created on Tue Sep  2 16:17:11 2014

@author: kurain
"""

# global import
from xlwt import *

# local import

# global vars
header_names = [
    u"影片名称",
    u"片长",
    u"语言",
    u"开映时间",
    u"结束时间",
    u"场间",
]


## HEADER STYLE
header_pat = Pattern()
header_pat.pattern = header_pat.SOLID_PATTERN
header_pat.pattern_fore_colour = 1
header_pat.pattern_back_colour = 1
# header alignment
header_align = Alignment()
header_align.horz = header_align.HORZ_CENTER
header_align.vert = header_align.VERT_CENTER
# header border
header_border = Borders()
header_border.top = header_border.MEDIUM
header_border.left = header_border.MEDIUM
header_border.right = header_border.MEDIUM
header_border.bottom = header_border.MEDIUM
header_style = XFStyle()
header_style.pattern = header_pat
header_style.alignment = header_align
header_style.borders = header_border

## LEFT STYLE
left_border = Borders()
left_border.left = left_border.MEDIUM
left_style = XFStyle()
left_style.borders = left_border

## RIGHT STYLE
right_border = Borders()
right_border.right = right_border.MEDIUM
right_style = XFStyle()
right_style.borders = right_border

## BOTTOM LEFT STYLE
bottom_border = Borders()
bottom_border.left = bottom_border.MEDIUM
bottom_border.bottom = bottom_border.MEDIUM
bottolleft_style = XFStyle()
bottolleft_style.borders = bottom_border

## BOTTOM RIGHT STYLE
bottom_border = Borders()
bottom_border.right = bottom_border.MEDIUM
bottom_border.bottom = bottom_border.MEDIUM
bottomright_style = XFStyle()
bottomright_style.borders = bottom_border
## BOTTOM CENTER STYLE
bottom_border = Borders()
bottom_border.bottom = bottom_border.MEDIUM
bottomcenter_style = XFStyle()
bottomcenter_style.borders = bottom_border

class CMXlsByHall():
    
    def __init__(self, wsheet, row, coloumn):
        self.fwsheet = wsheet
        self.film_num = 0
        self.row = row
        self.col = coloumn
        self.row_focus = row
        self.col_focus = coloumn
        return
    
    def init(self, hall=u"大厅", filmmax=10, sits=u"", sleep=u"00:00"):
        global header_names
        global header_style
        global left_style
        global right_style
        
        self.sits = sits
        self.sleep = sleep
        self.film_max = filmmax
        self.hall = hall
        
        # write title merging excel unit table
        self.fwsheet.write_merge(self.row_focus, self.row_focus+1, self.col_focus, self.col_focus+5, self.hall, header_style)
        # write table header
        self.row_focus = self.row_focus + 2
        
        self.fwsheet.write(self.row_focus, self.col_focus+0, header_names[0], left_style)
        self.fwsheet.write(self.row_focus, self.col_focus+1, header_names[1])
        self.fwsheet.write(self.row_focus, self.col_focus+2, header_names[2])
        self.fwsheet.write(self.row_focus, self.col_focus+3, header_names[3])
        self.fwsheet.write(self.row_focus, self.col_focus+4, header_names[4])
        self.fwsheet.write(self.row_focus, self.col_focus+5, header_names[5], right_style)
        
        self.row_focus = self.row_focus + 1
        return
    
    def add_movie(self, name=u"电影", duration=u"00:00", lang=u"未知", starttime=u"00:00", endtime=u"00:00", sleeptime=u"00:00"):
        global left_style
        global right_style
        self.fwsheet.write(self.row_focus, self.col_focus+0, name, left_style)
        self.fwsheet.write(self.row_focus, self.col_focus+1, duration)
        self.fwsheet.write(self.row_focus, self.col_focus+2, lang)
        self.fwsheet.write(self.row_focus, self.col_focus+3, starttime)
        self.fwsheet.write(self.row_focus, self.col_focus+4, endtime)
        self.fwsheet.write(self.row_focus, self.col_focus+5, sleeptime, right_style)
        self.row_focus = self.row_focus + 1
        self.film_num = self.film_num + 1
        return
    
    def fini(self):
        global left_style
        global right_style
        global bottolleft_style
        global bottomright_style
        global bottomcenter_style
        # fill last empty film units
        for idx in range(self.film_num, self.film_max):
            self.fwsheet.write(self.row_focus, self.col_focus+0, '', left_style)
            self.fwsheet.write(self.row_focus, self.col_focus+5, '', right_style)
            self.row_focus = self.row_focus + 1
        
        # write tail units
        tail_row = self.row+self.film_max + 3
        tail_col = self.col_focus
        self.fwsheet.write(tail_row, tail_col+0, self.sits, bottolleft_style)
        self.fwsheet.write_merge(tail_row, tail_row, tail_col+1, tail_col+3, u"默认场间：", bottomcenter_style)
        self.fwsheet.write_merge(tail_row, tail_row, tail_col+4, tail_col+5, self.sleep, bottomright_style)
        return

# for test
if __name__ == "__main__":
    fwbook = Workbook('utf-8')
    range_sheet = fwbook.add_sheet(u"拍片表")
    
    hall_unit = CMXlsByHall(range_sheet, 6, 0)
    hall_unit.init(u"一号厅", 10, u"数字共 8 排60座", u"00:15:00")
    for ii in range(4):
        hall_unit.add_movie(u"盗马记",	u"1:36",	u"英", u"13:00",	u"14:36", u"0:24")
    hall_unit.fini()
    
    hall_unit = CMXlsByHall(range_sheet, 6, 7)
    hall_unit.init(u"二号厅", 10, u"数字共 8 排60座", u"00:15:00")
    for ii in range(4):
        hall_unit.add_movie(u"盗马记",	u"1:36",	u"英", u"13:00",	u"14:36", u"0:24")
    hall_unit.fini()    
    
    hall_unit = CMXlsByHall(range_sheet, 6, 14)
    hall_unit.init(u"三号厅", 10, u"数字共 8 排60座", u"00:15:00")
    for ii in range(4):
        hall_unit.add_movie(u"盗马记",	u"1:36",	u"英", u"13:00",	u"14:36", u"0:24")
    hall_unit.fini()  
    
    fwbook.save(u"test_横版排片表.xls")