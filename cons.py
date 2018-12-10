from sqlite3.dbapi2 import Connection

import pandas as pd
import numpy as np
import json
import sqlite3
import csv

conn = sqlite3.connect('musicly.db')
c = conn.cursor()

def music():
    print("1.Playlists 2.Artists 3.Albums 4.Library")
    s=input()
    s=int(s)
    b=s
    if(s==1):
        show_playlists(b)
    elif(s==2):
        while(s!=3):
         print("1.show")
         print("2.ADD")
         print("3.back to hoom")
         s=input()
         s=int(s)
         if(s==1):
            show()
         elif(s==2):
            add()
         else:
             music()

    elif(s==3):
         ss=''
         while(ss!=3):
                 print("1.show")
                 print("2.ADD")
                 print("3.back to Hoom")
                 ss=input()
                 ss=int(ss)
                 if(ss==1):
                    show()
                 elif(ss==2):
                    add()
                 else:
                     music()
    else:
      s=''
      while(s!=0):
         print("1.Show)")
         print("2.ordered Playlist’s songs ")
         print("3.Add")
         print("4.Remove")
         print("5.back to Hoom ")
         print("0.stop")
         s=input()
         s=int(s)
         if(s==1):
            show()
         elif(s==2):
            order()
         elif(s==3):
            add()
         elif(s==4):
            remove()
         elif(s==5):
            music()
         else:
             return



def show_playlists(b):

        s=b
        if(s==1):

            q1=c.execute("SELECT COUNT(*) from playlistsongs where playlist='sad'")
            for sad in q1:
                  print("sad Tracks","       ","Tracks: ",sad[0])
            q2=c.execute("SELECT COUNT(*) from playlistsongs where playlist='anime'")
            for anime in q2:
                  print("anime Tracks","     ","Tracks: ",anime[0])
            q3=c.execute("SELECT COUNT(*) from playlistsongs where playlist='relaxing'")
            for relaxing in q3:
                   print("relaxing Tracks","  ","Tracks: ",relaxing[0])
            q4=c.execute("SELECT COUNT(*) from playlistsongs where playlist='romance'")
            for romance in q4:
                      print("romance Tracks","   ","Tracks: ",romance[0])
            while(s!=2):

                print("1. View playlist")
                print("2. Back to Home")
                print("3. Add Playlistt")
                print("4. Delete Playlist")
                s=input()
                s=int(s)
                if(s==1):
                         print("1. sad")
                         print("2. anime")
                         print("3. relaxing")
                         print("4. romance")

                         sss=input()
                         sss=int(sss)
                         if(sss==1):
                             qq1=c.execute("SELECT name,Songlength from song where playlist='sad' ")
                             for arr in qq1:
                               print(arr[0])
                         elif(sss==2):
                             qq2=c.execute("SELECT name,Songlength from song where playlist='anime'")
                             for arr in qq2:
                               print(arr[0])
                         elif(sss==3):
                            qq3=c.execute("SELECT name,Songlength from song where playlist='relaxing'")
                            for arr in qq3:
                               print(arr[0])
                         elif(sss==4):
                          qq4=c.execute("SELECT name,Songlength from song where playlist='romance'")
                          for arr in qq4:
                            print(arr[0])

                elif(s==2):
                           music()
                elif(s==3):
                    add()
                elif(s==4):
                    remove()

def order():

             print("orderd by")
             print("1.name")
             print("2.band")
             print("3.album")
             print("4.releaseDate")
             s=input()
             s=int(s)
             if(s==1):
                 q1=c.execute("SELECT name,band,album,releaseDate from song order by name ")
                 print(" ")
                 for name in q1:
                    print(name[0],"  ",name[1],"  ",name[2],"  ",name[3])
                 print(" ")
                 print(" ")
             elif(s==2):
                 q2=c.execute("SELECT name,band,album,releaseDate from song order by band ")
                 for band in q2:
                     print(band[0],"  ",band[1],"  ",band[2],"  ",band[3])
                 print(" ")
                 print(" ")
             elif(s==3):
                 q3=c.execute("SELECT name,band,album,releaseDate from song order by album ")
                 for album in q3:
                   print(album[0],"  ",album[1],"  ",album[2],"  ",album[3])
                 print(" ")
                 print(" ")
             else:
                 q4=c.execute("SELECT name,band,album,releaseDate from song order by releaseDate ")
                 for r in q4:
                    print(r[0],"  ",r[1],"  ",r[2],"  ",r[3])






def show():
        s=6
        while(s!=5):
            print(" 1.show you the songs of spacific album")
            print(" 2.show you the songs of spacific artist")
            print(" 3.show you the discrebtion of a spacific songs")
            print(" 4.show you the song of a spacific genre")
            print(" 5.Back to Hoom")
            s=input()
            s=int(s)
            if(s==1):
                show_album()
            elif(s==2):
                show_artist()
            elif(s==3):
                show_song()
            elif(s==4):
                show_genre()
            else:
                music()



def add():

    s=6
    while(s!=0):
        print("1.Add new songs to playlist")
        print("2.Add new album")
        print("3.Add new playlist with description and name")
        print("4.add_artist")
        print("5.Back to Hoom")
        print()
        s=input()
        s=int(s)
        if(s==1):

            add_song()

        elif(s==2):
              add_album()

        elif(s==3):
              add_playlist()

        elif(s==4):
              add_artist()
        else:
           music()

def remove():
    s=6
    while(s!=0):
        print("1.removeSongFromPlaylist")
        print("2.remove_Song")
        print("3.remove_Album")
        print("4.remove_playList")
        print("5.remove_artist")
        print("6.Back to Hoom")
        s=input()
        s=int(s)
        if(s==1):

                     removeSongFromPlaylist()

        elif(s==2):
                     remove_Song()

        elif(s==3):
                    remove_Album()

        elif(s==4):
                     remove_playList()

        elif(s==4):
                     remove_artist()

        else:
            music()



def feature16():

                   c.execute("delete from playlistSongs")
                   print("after delete")
                   vv= c.execute("SELECT * from playlistSongs")
                   for i in vv:
                     print(i[0])

                   c.execute("delete from song")
                   print("after delete")
                   vv= c.execute("SELECT * from song")
                   for i in vv:
                     print(i[0])

                   c.execute("delete from album")
                   print("after delete")
                   vv= c.execute("SELECT * from album")
                   for i in vv:
                     print(i[0])

                   c.execute("delete from artist")
                   print("after delete")
                   vv= c.execute("SELECT * from artist")
                   for i in vv:
                     print(i[0])

def show_album():
                vv=c.execute("SELECT title,NumberOfSongs from album ")
                for i in vv:
                   print(i[0])
                print("  ")
                print("  ")

                s=input()
                if(s=='y'):
                   print("enter the album name")
                   s=input()
                   cor=c.execute("SELECT name from song where album=?",(s,))
                   for i in cor:
                        print(i[0])
def show_artist():
                nn=c.execute("SELECT name from artist ")
                for i in nn:
                   print(i[0])
                print("  ")

                s=input()
                if(s=='y'):
                   print("enter the artist name")
                   s=input()
                   bb=c.execute("SELECT name from song where band=?",(s,))
                   for j in bb:
                       print(j[0])
def show_song():
                qq1=c.execute("SELECT name from song")
                for arr in qq1:
                    print(arr[0])

                s=input()
                if(s=='y'):
                   print("enter the song name")
                   s=input()
                   vv=c.execute("SELECT * from song where name=?",(s,))
                   for i in vv:
                       print(i[0],",",i[1],",",i[2],",",i[3],",",i[4],",",i[5],",",i[6],",",i[7],",",i[8],",",i[9])
def show_genre():

                s=input()
                if(s=='y'):
                   print("enter the genre type")
                   s=input()
                   c.execute("SELECT * from song where geners=?",(s,))
                   print(c.fetchall())


def add_song():
    print("name")
    s1=input()
    print("album")
    s2=input()
    print("band")
    s3=input()
    print("ft")
    s4=input()
    print("date")
    s5=input()
    print("geners")
    s6=input()
    print("duration")
    s7=input()
    print("lyrics")
    s8=input()
   # conn = sqlite3.connect('E:\musicly.db')
    conn.execute("insert into song (name,album,band,ft_artist,releaseDate,geners,Songlength,lyrics) values (?,?,?,?,?,?,?,?)",(s1,s2,s3,s4,s5,s6,s7,s8))
    #conn.commit()
    print("Song added")
    #conn.close()
    return
def add_album():
    print("title")
    s1=input()
    print("band")
    s2=input()
    print("numberOfSongs")
    s3=input()
    s3=int(s3)
    conn.execute("insert into album (title,band,numberOfSongs) values (?,?,?)",(s1,s2,s3))
    print("Done")
def add_playlist():
    print("enter the name")
    name=input()
    print("enter the discribtion")
    disc=input()
    conn.execute("insert into playlists (name,description) values (?,?)",(name,disc))
def add_artist():
    print("name")
    s1=input()
    print("dateOfBirth")
    s2=input()
    print("band")
    s3=input()
    conn.execute("insert into artist (name,dateOfBirth,band) values (?,?,?)",(s1,s2,s3))
    print("Artist added!")


def removeSongFromPlaylist():
    print("what song and playlist that you want delete ")
    s=input()
    p=input()
    conn.execute("delete from playlistSongs where song =? and playlist=?",(s,p))
    print("Song removed!")
def remove_Song():
     print("what song  that you want delete ")
     s=input()
     conn.execute("delete from playlistSongs where song =?", (s,))
     conn.execute("delete from song where name =?",(s,))
     print("Song Deleted!")
def remove_Album():
                        print("what albumthat you want delete ")
                        s=input()
                        cursor = conn.execute("select name from song where album = ?", (s,))
                        for row in cursor:
                            conn.execute("delete from playlistSongs where song =?", (row[0],))
                            conn.execute("delete from song where name =?", (row[0],))
                            conn.execute("delete from album where title =?",(s,))

                        print("Album Deleted!")
def remove_playList():
                        print("what name that you want delete ")
                        s=input()
                        conn.execute("delete from playlistSongs where playlist =?", (s,))
                        conn.execute("delete from playlists where name =?",(s,))
                        print("playList Deleted!")
def remove_artist():
                        print("what song and playlist that you want delete ")
                        s=input()
                        cursor = conn.execute("select name from song where band = ?", (s,))
                        for row in cursor:
                            conn.execute("delete from playlistSongs where song =?", (row[0],))
                            conn.execute("delete from song where name =?", (row[0],))
                        conn.execute("delete from album where band =?",(s,))
                        conn.execute("delete from artist where name =?", (s,))
                        print("Artist Deleted!")


music()
conn.commit()
conn.close()






# import pymysql


#with open('E:\\aaa\\table-3.csv', 'r') as csv_file:
 #   csv_reader = csv.reader(csv_file)
  #  flist = []
   # for line in csv_reader:
    #    flist.append(line)
#print(flist[0][0])

#Artist = flist[0][0]
#Album = flist[0][1]
#Released = flist[0][2]
#Genre = flist[0][3]
#Total_certified_copies=flist[0][4]
#songs=flist[0][5]

row =''
#c.execute("CREATE table music(Artist text,Album text,Released integer,Genre text,Total_certified_copies text,songs text)".format(Artist,Album,Released,Genre,Total_certified_copies,songs))
#for i in range(24):
   # row += "('{}','{}','{}','{}','{}','{}')".format(flist[i][0], flist[i][1], flist[i][2], flist[i][3], flist[i][4],flist[i][5])
 #   c.execute("INSERT into music values('{}','{}','{}','{}','{}','{}')".format(flist[i][0], flist[i][1], flist[i][2], flist[i][3], flist[i][4],flist[i][5]))
  #  if (row != len(flist)) - 2:
   #     row += ','
#Qinsert = "insert into music values" + row
#try:
#c.execute("INSERT into music values('{}','{}','{}','{}','{}')".format(flist[0][1], flist[0][2], flist[0][3], flist[0][4], flist[0][5]))
#c.execute(Qinsert)
 #   conn.commit()
#except:
 #    conn.rollback()
#list = []
