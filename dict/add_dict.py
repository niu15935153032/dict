import pymysql
import re

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='123456',
                     database='dict',
                     charset='utf8')
cur = db.cursor()
fd = open('dict.txt')
# sql='insert into diction (word,mean) values (%s,%s)'
for line in fd:
    # 获取word mean
    tup = re.findall(r"(\S+)\s+(.*)", line)[0]
    try:
        sql = 'insert into words (word,mean) values (%s,%s)'
        cur.execute(sql, tup)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
fd.close()
cur.close()
db.close()
