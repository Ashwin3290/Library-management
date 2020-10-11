import mysql.connector as myc
mysql=myc.connect(host='localhost',user='root',password='12345',database='testdb')
cursor=mysql.cursor()
def connect():
    mysql=myc.connect(host='localhost',user='root',password='12345',database='testdb')
    cursor=mysql.cursor()

if mysql.is_connected():
    print('Database connected')

def insert(a,d,b,c):
    connect()
    v="insert into libd (membership_num,book_name,book_serial,doi) values('{0}','{1}',{2},'{3}')".format(a,d,b,c)
    cursor.execute(v)
    mysql.commit()
    mysql.close
def minsert(a,b,c):
    connect()
    v="insert into membership values('{0}',{1},{2})".format(a,b,c)
    cursor.execute(v)
    mysql.commit()
    mysql.close
def  update(A,B):
    connect()
    cursor.execute("update libd set dor='{0}' where book_serial={1}".format(B,A))  
    mysql.commit()
    mysql.close()
def show(num):
        cursor.execute("select * from libd where book_serial={0}".format(num))
        data=cursor.fetchall()
        s='_'*125
        m=int(15)
        w=' '
        for row in data:
            for i in row:
                h=0
                o=len(str(i))
                h=15-o
                print(i,w*h,'|' , end='')
            print('\n')
            print(s)
def delete (name):
    try:
        cursor.execute("delete from membership where name={}".format(name))
        mysql.close()
        return True
    except:
        print('data does not exist')
        return False
print('database ok')

