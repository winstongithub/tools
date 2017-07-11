#coding:utf-8
import sqlite3
import random
import pygame
import os

randmap=dict()
conn = sqlite3.connect('db/dict.db')
def init( ):
    pygame.mixer.init()
    cursor = conn.cursor()
    ret = cursor.execute('select * from dict')
    lines = ret.fetchall()
    cursor.close()
    return lines

def initRandmap( lines):
    index=0
    for line in lines:
        linelist = list(line)
        updateRandMap(linelist,linelist[3],True)

def updateRandMap( line ,times,isinit):
    index = len(randmap)-1
    if not isinit:
        line[3]=line[3]+times
        sql = 'update dict set times = {0} where word="{1}"'.format(line[3],line[0])
        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        conn.commit()
    for i in range(0,times):
        randmap[index]=line
        index = index + 1

def getLine():
    randnum = random.randint(0,len(randmap)-1)
    return randmap[randnum]

def echoword(word):
    if  word+u'.mp3' in os.listdir(r'./voice/'+word[0]):
        pygame.mixer.music.load(u'./voice/'+word[0]+'/'+word+'.mp3')
        pygame.mixer.music.play()
    else:
        print 'error',word

        

def wordloop( ):
    flag = True
    line = None
    while True:
        if flag:
            line = getLine()
        print line[1]
        echoword(line[0])
        inputword=raw_input()
        if inputword == "quit()":
            break
        
        if inputword == line[0]:
            flag = True
            updateRandMap(line,-1,False)
        else:
            flag = False
            print line[0]
            updateRandMap(line,7,False)
        

if __name__ == '__main__':

    lines = init( )
    initRandmap(lines)
    wordloop()
