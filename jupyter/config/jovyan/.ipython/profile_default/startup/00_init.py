import pymysql
import pandas as pd


# 野球情報の取得
db = pymysql.connect(host='baseball_db',
                     user='baseball_user',
                     password='baseball_pass',
                     db='baseball_db',
                     charset='utf8',
                     cursorclass=pymysql.cursors.DictCursor)

try:
    pd.set_option("display.max_colwidth", 255)
    pd.set_option("display.max_columns", 150)

    bb_df = pd.read_sql_query(
            "SELECT * from batter",db)

finally:
    db.close()
