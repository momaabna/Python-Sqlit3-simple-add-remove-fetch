import sqlite3

def add():
    name =raw_input('Enter Class Name :')
    file = raw_input('Enter File Link :')
    info =raw_input('Enter Class Info :')
    con.execute("INSERT INTO CLASSES(NAME ,FILE,INFO) VALUES ('"+name +"','"+file+"','"+info+"');")
    con.commit()
    print "Added ('"+name +"','"+file+"','"+info+"') Successfully ."

def rem():
    name = raw_input('Enter Class Name :')
    con.execute("DELETE FROM CLASSES WHERE NAME='"+name+"';")
    con.commit()
    print 'Deleted Succefully .'

def fetch():
    s = con.execute("SELECT NAME,FILE,INFO FROM CLASSES;")
    print 'NAME    |     FILE   |    INFO'
    print '----------------------'
    for i in s :
        print i[0]+'  |  '+i[1]+'  |  '+i[2]



con = sqlite3.connect('be.db')
print 'Connected To Database ..'
while 1:

    ed = raw_input('Enter a to add ,r to remove,f to fetch ,e to END :')
    if ed =='a':
        add()
    elif ed=='r':
        rem()
    elif ed=='f':
        fetch()
    elif ed =='e':
        con.close()
        quit()



