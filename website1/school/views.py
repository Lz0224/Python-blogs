# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import xlrd
import xlwt
from datetime import date, datetime
# Create your views here.

def read_excel():
    #打开文件
    workbook = xlrd.open_workbook(r'cekong.xls')
    #获取所有sheet
    print workbook.sheet_name()
    sheet2_name = workbook.sheet_name()[1]

    #根据sheet索引或者名称获取sheet内容
    sheet2 = workbook.sheet_by_index(1)
    sheet2 = workbook.sheet_by_name('sheet2')

    #sheet 的名称，行数，列数
    print sheet2.name,sheet2.nrows,sheet2.ncols

    rows = sheet2.row_values(3)     #获取第四行的内容
    cols = sheet2.col_values(2)     #获取第三行的内容

    print rows
    print cols

    #获取单元格的内容
    print sheet2.cell(1,0).value.encode('utf-8')
    print sheet2.cell_value(1,0).encode('utf-8')
    print sheet2.row(1)[0].value.encode('utf-8')

    #获取单元格内容的数据类型
    print sheet2.cell(1,0).ctype

if __name__ == '__main__':
    read_excel()
