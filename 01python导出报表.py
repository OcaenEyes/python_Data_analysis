#!/usr/bin/python
# -*- coding:utf-8 -*-

import datetime
import time
import mysql.connector
import xlwt
import sys
import os

# 默认样式
default_style =xlwt.easyxf(
    '''
    pattern:pattern solid;
    borders: left 1,right 1,top 1,bottom 1;
    align: horiz center
    ''',
    num_format_str='0,000.00'
)


# 标题样式
title_style = xlwt.easyxf(
    '''
        pattern : pattern solid,fore_colour yellow;
        font : name Times New Roman , color-index black, bold on ;
        borders : left 1, right 1,top 1,bottom 1;
        align : horiz center
    ''',
    num_format_str='0,000.00'

)

# 时间格式样式
time_style = xlwt.easyxf(
    num_format_str='YYYY-MM-DD h:mm:ss'
)

def get_sql():
    '''
    创建需要的sql语句
    :return:
    '''

    sql = '''
        SELECT title,filming_time,crt_time,orders FROM material_img_info;
    '''

    return sql

def get_title(cursor):
    '''
    通过游标获得excel文件 title
    :param cursor:
    :return:
    '''

    return cursor.column_names

def get_select_data(cursor):
    '''
    通过游标获得数据列表（list）
    :param cursor:
    :return:
    '''

    return [row for row in cursor]

def create_excel_title(work_sheet,title,title_style=None):
    '''
    生产 excel title
    :param work_sheet:
    :param title:
    :param title_style:
    :return:
    '''

    if not title_style:
        title_style = default_style
    for col_index,col_name in enumerate(title):
        work_sheet.write(0,col_index,col_name,title_style)
    return work_sheet

def create_excel_body(work_sheet,body,body_style = None):
    '''
    生成excel body 信息
    :param work_sheet:
    :param body:
    :param body_style:
    :return:
    '''
    if not title_style:
        body_style = default_style

    for row_num,row_data in enumerate(data,1):
        for col_index,col_value in enumerate(row_data):
            work_sheet.write(row_num,col_index,col_value)
    return work_sheet


def get_col_max_length(data,title):
    '''
    获取数据每列最大值长度
    :param data:
    :param title:
    :return:
    '''
    col_len = map(len ,map(str ,title) )
    func = lambda x,y: y if y >x else x
    for row in data:
        row_len = map(len,map(str,row))
        col_len = map (func ,col_len,row_len)
    return col_len


def set_work_sheet_col_len(work_sheet,max_len):
    '''
    设置列长度
    :param work_sheet:
    :param max_len:
    :return:
    '''

    for col,len in enumerate(max_len):
        work_sheet.col(col).width = 256 * (len-1)
    return work_sheet


if __name__ == '__main__':
    info = {
        'host':'',
        'user':'',
        'password':'',
        'database':''
    }

    conn = mysql.connector.connect(**info)
    cursor = conn.cursor()
    sql = get_sql()
    cursor.execute(sql)

    # 获得excel的title
    title = get_title(cursor)

    # 获得需要的数据
    data = get_select_data(cursor)

    # 获得每一列的最大长度
    max_len = get_col_max_length(data,title)
    work_book = xlwt.Workbook(encoding='utf-8')

    # 创建一个excel模版
    work_sheet = work_book.add_sheet('查询数据')

    # 生成excel title
    work_sheet = create_excel_title(work_sheet,title,title_style)

    # 生成excel数据
    work_sheet = create_excel_body(work_sheet,data)

    # 设置每一列适当的长度
    work_sheet = set_work_sheet_col_len(work_sheet,max_len)

    # 保存excel
    work_book.save('data_{time}_统计表.xls',format(time = time.strftime('%Y-%m-%d',time.localtime(time.time()))))



