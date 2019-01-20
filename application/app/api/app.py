import json

import pymysql
import responder

api = responder.API()


@api.route("/")
def hello_world(req, resp):
    resp.text = "hello, world!"


@api.route("/player/{id}")
def get_player_info(req, resp, *, id):
    conn = pymysql.connect(host='172.17.0.2',
                           user='baseball_user',
                           password='baseball_pass',
                           db='baseball_db',
                           charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)

    try:
        with conn.cursor() as cursor:
            sql = "SELECT name from batter"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result[0])
    finally:
        conn.close()
    resp.text = json.dumps(result, ensure_ascii=False)


if __name__ == '__main__':
    api.run(address="0.0.0.0")
