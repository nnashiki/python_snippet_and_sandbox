import pymysql
import pandas as pd


# 野球情報の取得
db = pymysql.connect(host=  '172.17.0.2',
                     user='baseball_user',
                     password='baseball_pass',
                     db='baseball_db',
                     charset='utf8',
                     cursorclass=pymysql.cursors.DictCursor)

try:
    bb_df = pd.read_sql_query(
            "SELECT * from batter",db)

finally:
    db.close()
