import sqlite3
import scraping as sc

import pandas as pd

def Create(file, code, year_s):        
    #データベース名.db拡張子で設定
    
    dbname = (str(file))
    #データベースを作成
    db = sqlite3.connect(dbname, isolation_level=None)

    #スクレイピング実施
    df = sc.multi_Brand(code, year_s)

    #dfをto_sqlでデータベースに変換する。DBのテーブル名はpriceとする
    df.to_sql('price', db, if_exists='append', index=False)

    #データベースにカーソルオブジェクトを定義
    cursor = db.cursor()
    #本当にpriceテーブルが作成されたのか？をsql関数で確認する
    sql = """SELECT name FROM sqlite_master WHERE TYPE='table'"""
    
    for t in cursor.execute(sql):
      print(t) #OKであれば('price',)と表記される
      
   
    db.close()
    
    print("DB_Create_Complete")