# -*- coding: utf-8 -*-

# global import
from xlwt import *

from xls import *

def test_xlsbydate():
    movie_table = [
        ['盗马记',	'1',	'13:00',	'14:36',	'1:36',	'粤语'],
        ['盗马记',	'1',	'15:00',	'16:36',	'1:36',	'粤语'],
        ['盗马记',	'1',	'17:30',	'19:06',	'1:36',	'粤语'],
        ['极品飞车3D',	'6',	'13:40',	'15:50',	'2:10',	'英语'],    
    ]
    
    fwbook = Workbook('utf-8')
    range_sheet = fwbook.add_sheet(u"Sheet1")
    
    xls = CMXlsByDate(range_sheet, 0, 0)
    xls.init(u"菲尔姆国际影城排期表", u"2014-4-1  周二全天观影半价")
    for movie in movie_table:
        xls.add_movie(movie[0], movie[1], movie[2], movie[3], movie[4], movie[5])
    xls.fini()
    
    fwbook.save(u"test_礼宾表.xls")
    return

def test_xlsbyhall():
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
    return

def test_xlsvtable():
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
    return
    
if __name__ == "__main__":
    test_xlsbydate()
    test_xlsbyhall()
    test_xlsvtable()