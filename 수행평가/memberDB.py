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


    #id에 맞는 이름을 출력해주는 함수
    def  selectName(self, inId):
        name =""
        try:
            with self.conn.cursor() as cursor:
                sql = 'SELECT NAME FROM profile WHERE id = %s'
                cursor.execute(sql, (inId))
                result = cursor.fetchall()
                for i in result:
                    name = i[0]

        finally:
            self.conn.close()
            return name

    #회원정보와 로그인 입력 정보를 비교하는 함수
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


    #데이터베이스 테이블에 데이터를 넣어주는 함수
    def insert(self, id, pwd, name):
        try:
            with self.conn.cursor() as cursor:
                sql = 'INSERT INTO profile (id, pwd, name) VALUES (%s, %s, %s)'
                cursor.execute(sql, (id, pwd, name))
            self.conn.commit()
            tkinter.messagebox.showinfo("회원가입 완료","회원가입이 완료되었습니다!")

        finally:
            self.conn.close()