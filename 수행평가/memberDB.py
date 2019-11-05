import pymysql
global conn
from tkinter import *
import tkinter.messagebox

class memberDb:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',
                               user='root',
                               password='mirim2',
                               db='performance',
                               charset='utf8mb4')

    def selectId(self, inId):
        try:
            with conn.cursor() as cursor:
                sql = 'SELECT * FROM profile WHERE id = %s'
                cursor.execute(sql, (inId))
                result = cursor.fetchall()
                for i in result:
                    id = i[0]

        finally:
            return id
            self.conn.close()


    def selectName(self, inId):
        name =""
        try:
            with conn.cursor() as cursor:
                sql = 'SELECT name FROM profile WHERE id = %s'
                cursor.execute(sql, (inId))
                result = cursor.fetchall()
                for i in result:
                    name = i[0]
                    print(name)

        finally:
            return name
            self.conn.close()


    def check_Id(self, inId, inPwd):
        result = 1
        id = ""
        pwd = ""
        try:
            with self.conn.cursor() as cursor:
                sql = 'SELECT id, pwd FROM profile WHERE id = %s'
                cursor.execute(sql,(inId))
                rs = cursor.fetchall()
                for i in rs:
                    id = i[0]
                    pwd = i[1]

                if id == inId:
                    if pwd == inPwd:
                        result = 1 #성공
                    else:
                        result = 3 #password 오류
                else:
                    result = 2 #id 오류
        finally:
            return result
            self.conn.close()



    def insert(self, id, pwd, name):
        try:
            with self.conn.cursor() as cursor:
                sql = 'INSERT INTO profile (id, pwd, name) VALUES (%s, %s, %s)'
                cursor.execute(sql, (id, pwd, name))
            self.conn.commit()
            tkinter.messagebox.showinfo("회원가입 완료","회원가입이 완료되었습니다!")

        finally:
            self.conn.close()