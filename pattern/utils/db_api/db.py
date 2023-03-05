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

    def add_forward_in_user(self,apitoken,forward):
        self.cursor.execute(f"UPDATE `mydbsubs`.`table_bots_users` SET `forward` = '{forward}' WHERE (`apitoken` = '{apitoken}')")
        return self.conn.commit()

    def add_text_in_user(self,apitoken,text,imgpath):
        self.cursor.execute(f"UPDATE `mydbsubs`.`table_bots_users` SET `text` = '{text}',`imgpath` = '{imgpath}' WHERE (`apitoken` = '{apitoken}')")
        return self.conn.commit()

    def add_chat_in_user(self,apitoken,chat):
        self.cursor.execute(f"UPDATE `mydbsubs`.`table_bots_users` SET `chat` = '{chat}' WHERE (`apitoken` = '{apitoken}')")
        return self.conn.commit()

    def get_information(self,apitoken):
        self.cursor.execute(f"SELECT * FROM mydbsubs.table_bots_users where (`apitoken` = '{apitoken}');")
        return self.cursor.fetchone()








    def add_bots_in_bd(self,userid,apitoken,botname,username):
        self.cursor.execute(f"SELECT * FROM mydbsubs.tbsubs where (`apitoken` = '{apitoken}');")
        if self.cursor.fetchone():
            pass
        else:
            self.cursor.execute(f"INSERT INTO `mydbsubs`.`tbsubs` "
                                f"(`userid`, `apitoken`, `botname`, `username`)"
                                f" VALUES ('{userid}', '{apitoken}', '{botname}', '{username}');")

        self.conn.commit()
        self.cursor.execute(f"SELECT * FROM mydbsubs.table_bots_users where (`apitoken` = '{apitoken}');")
        if self.cursor.fetchone():
            pass
        else:
            self.cursor.execute(f"INSERT INTO `mydbsubs`.`table_bots_users` "
                                f"(`apitoken`)"
                                f" VALUES ('{apitoken}');")
        return self.conn.commit()