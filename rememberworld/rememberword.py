import sqlite3
import sys
import io

def init( conn ):
    cursor = conn.cursor()
    ret = cursor.execute('select * from dict')
    lines = ret.fetchall()
    cursor.close()
    return lines
def wordloop( lines ):
    for line in lines:
        print line[1]#.decode('utf-8').encode('gb2312')
        a=input()

if __name__ == '__main__':
    conn = sqlite3.connect('db/dict.db')
    lines = init( conn )
    wordloop(lines)
