#coding:utf-8


import json
from config import *
import MySQLdb


def db_connect():
    try:
        conn = MySQLdb.connect(host=db_ip, user=db_user, passwd=db_passwd, db=db_database, charset="utf8")
        conn.autocommit(True)
        return conn
    except Exception, e:
        print(e,"can't connect database!")


def db_insert(db_tablename, name, info, level, type, data):
    conn = db_connect()
    cursor = conn.cursor()
    sql = "insert into %s(name, info, level, type, data, inittime, uptime) values('%s','%s','%s','%s','%s',utc_timestamp(),utc_timestamp())" % (db_tablename, name, info, level, type, data)
    cursor.execute(sql)
    cursor.close()
    conn.close()


def db_select(db_tablename, name):
    #conn = pool.connection()
    conn = db_connect()
    cursor = conn.cursor()
    sql = "select data from %s where name='%s'" % (db_tablename, name)
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data[0][0]


def db_update(db_tablename, name, data):
    #conn = pool.connection()
    conn = db_connect()
    cursor = conn.cursor()
    sql = "update %s set data='%s' where name='%s'"%(db_tablename, data, name)
    cursor.execute(sql)
    cursor.close()
    conn.close()

if __name__ == "__main__":
    r = db_select(db_payload, 'crossdomain_config_improper')
    print type(r)
    print r
    print json.loads(r)
    print type(json.loads(r))
