#coding:utf-8
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
    index = 0
    while index < len(lines):
        line = lines[index]
        print line[1]
        inputword=raw_input()
        if inputword == line[0]:
            index = index+1
        else:
            print line[0]

if __name__ == '__main__':
    conn = sqlite3.connect('db/dict.db')
    lines = init( conn )
    wordloop(lines)
