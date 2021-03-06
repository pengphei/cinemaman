# -*- coding: utf-8 -*-

# global import
from xlwt import *

# local import
header_names = [
    u"影片名称",
    u"影厅",
    u"开映时间",
    u"结束时间",
    u"片长",
    u"语言",
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
        
class CMXlsByDate():
    
    def __init__(self, wsheet, row, coloumn):
        self.fwsheet = wsheet
        self.row = row
        self.col = coloumn
        self.row_focus = row
        self.col_focus = coloumn
        self.width = 6
        return
    
    def init(self, title=u"XXXX影城排期表", date=u"XXXX-XX-XX 周X 排期表", playmax=100):
        global header_names
        global unit_style
        global title_style
        self.play_num = 0
        self.play_max = playmax
        
        # write title merging excel unit table
        self.fwsheet.write_merge(self.row_focus+0, self.row_focus+0, self.col_focus+0, self.col_focus+self.width-1, title, unit_style)        
        # write date info
        self.fwsheet.write_merge(self.row_focus+1, self.row_focus+1, self.col_focus+0, self.col_focus+self.width-1, date, unit_style)
        
        # write table header
        for idx in range(len(header_names)):
            self.fwsheet.write(self.row_focus+2, self.col_focus+idx, header_names[idx], title_style)
            
        self.row_focus = self.row_focus + 3
        return
        
    def add_movie(self, name='', hall='', starttime='', endtime='', duration='', lang=''):
        self.fwsheet.write(self.row_focus, self.col_focus+0, name, unit_style)
        self.fwsheet.write(self.row_focus, self.col_focus+1, hall, unit_style)
        self.fwsheet.write(self.row_focus, self.col_focus+2, starttime, unit_style)
        self.fwsheet.write(self.row_focus, self.col_focus+3, endtime, unit_style)
        self.fwsheet.write(self.row_focus, self.col_focus+4, duration, unit_style)
        self.fwsheet.write(self.row_focus, self.col_focus+5, lang, unit_style)
        
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
            self.fwsheet.write(self.row_focus, self.col_focus+4, '', unit_style)
            self.fwsheet.write(self.row_focus, self.col_focus+5, '', unit_style)
            self.row_focus = self.row_focus + 1
        return
