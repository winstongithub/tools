import sqlite3
import time

conn = sqlite3.connect('db/dict.db')
bak=open('bak.txt','w')

def saveword( sql ):
    cursor = conn.cursor()
    bak.write(sql+'\n')
    cursor.execute(sql)
    cursor.close()
    conn.commit()

def haveword(word):
    cursor = conn.cursor()
    sql = 'select word from dict where word = "{0}"'.format(word)
    ret = cursor.execute(sql)
    records = ret.fetchall()
    cursor.close()
    return len(records)!=0
def initdict(lines):
    total = len(lines)
    current = 0
    for line in lines:
        if current%10 == 0:
            print total,current
        parm = line.split(' ')
        if parm > 1:
            word = parm[0]
            if not haveword(word):
                definition=''
                for i in range(1,len(parm)):
                    definition = definition + parm[i]
            
                sql = 'insert into dict values ( "{0}" ,"{1}",NULL,"{2}",{3})'.format(word,definition.decode('gbk').encode('utf-8'),1,time.time())
                saveword(sql)
                current += 1
                continue
        print line
            
        



if __name__ == '__main__':
    f=open('word/word.txt','r')
    lines=f.readlines()
    initdict(lines)
    f.close()
    conn.close()
    bak.close()
    
