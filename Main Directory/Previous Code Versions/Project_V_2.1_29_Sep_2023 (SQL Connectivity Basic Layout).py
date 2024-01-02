import mysql.connector as mc

def SQL(ch1,ch2,ch3,a,b,c):
    t = (ch1,ch2,ch3,a,b,c)

    obj = mc.connect(
      host="localhost",
      user="root",
      passwd="1234"
    )

    # checking whether connection is established
    if not obj.is_connected():
        print('Not connected successfully!')

    cs = obj.cursor()

    cs.execute("create database if not exists calculus")
    cs.execute("use calculus")
    cs.execute("create table if not exists integration(ch1 int, ch2 int, ch3 int, a int, b int, c int, ans varchar(30),\
               CHECK (ch1 between 2 and 3), CHECK (ch2 between 1 and 5)")
    cs.execute("SELECT * from integration")

    table = cs.fetchall()   # tuples within a list

    for row in table:
        if row[0:6] == t:
            return row[6]
        else:
            cs.execute("insert into integration values({},{},{},{},{},{},'{}')".format(ch1, ch2, ch3, a, b, c, i))
            obj.commit()  # required after database modification