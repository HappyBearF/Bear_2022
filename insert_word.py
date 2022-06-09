'''
    将字典中元素传入数据库
'''

import pymysql
import re

f = open('dict_utf8.txt')

# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='Happy_1234',
                     database='dict',
                     charset='utf8')

# 获取游标（用于操作数据库，执行SQL语句）
cur = db.cursor()

# data = f.readline()
# tmp = data.split(' ')
# print(tmp)
# word = tmp[0]
# # mean = tmp[1]  # 此时经过拆分，会形成多个空格，所以：tmp[1]取不到想要的内容
# mean = ' '.join(tmp[1:]).strip()
# print(mean)  # --> v.抛弃，放弃


sql = "insert into words (word,mean) values (%s,%s)"
for line in f:
    # 获取单词和解释
    tup = re.findall(r"(\S+)\s+(.*)", line)[0]  # 返回两个子组：非空（单词）  空（空格）  可变多个字符（单词解释）
    try:
        cur.execute(sql,tup)
        db.commit()
    except:
        db.rollback()

f.close()

# 关闭数据库
db.close()
cur.close()
