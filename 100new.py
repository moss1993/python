#!usr/bin/env python
#coding=utf8

 
import MySQLdb  
import xlrd  
import time  
import sys
  
reload(sys) 
sys.setdefaultencoding('utf8')
  
# 从users.xls文件获取10000条用户数据  
 
def get_table():  
    FILE_NAME = '100new.xls'  
    data = xlrd.open_workbook(FILE_NAME)
    table = data.sheets()[0]
    return table  

  
# 批量插入executemany  
def insert_by_many(table):  
    nrows = table.nrows
    param=[]  
    for i in xrange(1,nrows): 
        param.append([str(table.cell(i, 0).value)+'<br><br/>'+str(table.cell(i, 4).value)+'<br><br/>'+'<a href='+'"/Download/'+str(table.cell(i, 5).value)+'" target="_blank">点击下载附件</a>',str(table.cell(i, 2).value),str(table.cell(i, 1).value),'/Download/'+str(table.cell(i, 5).value)])
    try:
        sql = "INSERT INTO t_question(content,score,questiontype,attachmentpath) values(%s,%s,%s,%s)"
        #print param
        # 批量插入  
        rem = cur.executemany(sql, param)
        conn.commit()
        print rem		
    except Exception as e:  
        print e  
        conn.rollback()      
  
# 连接本地数据库  设置编码 导入数据库名字 输入虚拟机IP或者拖入机器直接 运行
conn = MySQLdb.connect(host="192.168.146.129", port=3306, user="root", passwd="root", db="100ti",charset="utf8")  
cur = conn.cursor()  
  
# 从excel文件获取数据  
table = get_table() 

  
# 使用批量插入  
start = time.clock()  
insert_by_many(table)  
end = time.clock()  
  
  
# 释放数据连接  
if cur:
   cur.close()  
if conn:  
   conn.close()  