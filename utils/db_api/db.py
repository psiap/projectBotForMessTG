import datetime
import pymysql

from utils.db_api.configdb import *

class BotDB:

    def __init__(self):
        self.conn = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.conn.cursor()

    def check_bots(self,apitoken):
        self.cursor.execute(f"SELECT * FROM mydbsubs.tbsubs where (`apitoken` = '{apitoken}');")
        answer = self.cursor.fetchone()
        print(answer)
        if answer:
            if answer['pid'] == 'None' or answer['pid'] == None:
                return True
            else:
                return False
        else:
            return False

    def edit_pid_bot(self,apitoken,pid):
        self.cursor.execute(f"SELECT * FROM mydbsubs.tbsubs where (`apitoken` = '{apitoken}');")
        answer = self.cursor.fetchone()
        if answer:
            self.cursor.execute(f"UPDATE mydbsubs.tbsubs SET `pid` = '{pid}' WHERE (`apitoken` = '{apitoken}');")
            self.conn.commit()

    def get_all_bots(self):
        self.cursor.execute(f"SELECT * FROM mydbsubs.tbsubs;")
        return self.cursor.fetchall()

    def get_all_bots_in_user(self,userid):
        self.cursor.execute(f"SELECT * FROM mydbsubs.tbsubs where (`userid` = '{userid}');")
        return self.cursor.fetchall()

    def get_bot_in_api_token(self, apitoken):
        self.cursor.execute(f"SELECT * FROM mydbsubs.tbsubs where (`apitoken` = '{apitoken}');")
        return self.cursor.fetchone()

    def del_bot_in_api_token(self,apitoken):
        self.cursor.execute(f"DELETE FROM mydbsubs.tbsubs WHERE (`apitoken` = '{apitoken}');")
        return self.conn.commit()

    def get_all_users_token(self):
        self.cursor.execute(f"SELECT DISTINCT userid FROM mydbsubs.tbsubs;")
        return self.cursor.fetchall()

    def add_bots_in_bd(self,userid,apitoken,botname,username):
        self.cursor.execute(f"SELECT * FROM mydbsubs.tbsubs where (`apitoken` = '{apitoken}');")
        if self.cursor.fetchone():
            pass
        else:
            self.cursor.execute(f"INSERT INTO mydbsubs.tbsubs "
                                f"(`userid`, `apitoken`, `botname`, `username`)"
                                f" VALUES ('{userid}', '{apitoken}', '{botname}', '{username}');")

        return self.conn.commit()
