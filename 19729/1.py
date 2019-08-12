import pymysql

#打开数据库
db=pymysql.connect("47.105.40.52","root","Jdkc0912..","student")
#建立游标对象
cursor=db.cursor()
#使用excute执行sql
sql="SELECT name,age FROM demo"
cursor.execute(sql)
#使用fetchone获取单条数据
data = cursor.fetchall()
for i in data:
    print("age :%s"% i[1])
    print("name :%s"% i[0])

#关闭数据库
db.close()