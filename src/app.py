#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-14 16:12:15
# @Author  : Your Name (you@example.org)b
# @Link    : http://example.org
# @Version : $Id$

import functools
import time
import uuid
import socket
import MySQLdb
from flask import Flask


app = Flask(__name__)


def time_me(fn):
    @functools.wraps(fn)
    def _wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = fn(*args, **kwargs)
        return "{}() cost: {}s \n {}".format(fn.__name__,
                                                  time.perf_counter() - start,
                                                  res)
    return _wrapper


@app.route('/')
@time_me
def hello_world():
    ip = ([(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in
           [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1])
    return ip


'''
@app.route('/insert')
def test():
    maxid = "SELECT MAX(id) from blog_article" 
    cursor.execute(maxid)
    maxid = cursor.fetchall()
    maxid = maxid[0][0]
    insert = "INSERT INTO blog_article(add_time, modify_time, title, content, `order`, views, author_id, category_id, type) VALUES (NOW(), NOW(), '自动测试标题{}', '自动测试内容 4', 0, 1, 1, 2, 'a')"
    [cursor.execute(insert.format(uuid.uuid1())) for i in range(500000)]
    db.commit()
    db.close()
    #print(ret)
    return insert
'''


@app.route('/select')
@time_me
def read():
    db = MySQLdb.connect(host="192.168.11.25", port=3306, charset="utf8",
                         user="root", passwd="123456", db="binblog")
    cursor = db.cursor()
    sql = "SELECT * from blog_article;"
    cursor.execute(sql)
    db.close()
    return str(sql)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)
    # test()
