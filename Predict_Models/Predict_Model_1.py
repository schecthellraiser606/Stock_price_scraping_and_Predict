import pandas as pd
import sqlite3

def Model_1(file):
    #データベース呼びだし
    dbname = (str(file))
    db = sqlite3.connect(dbname)
    
    #PandasでDBの値を読み込み
    df_db = pd.read_sql('SELECT * FROM price', db)
    
    

