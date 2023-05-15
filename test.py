import pymysql

db=pymysql.connect(host="localhost", port=3306, db='userinfo', user="root", password='1111', charset='utf8')
cursor=db.cursor(pymysql.cursors.DictCursor)
cursor.execute('USE userinfo')
cursor.execute('select * from user')
value=cursor.fetchall()
print(value)