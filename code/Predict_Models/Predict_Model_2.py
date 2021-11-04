import pandas as pd
import sqlite3
from fbprophet.diagnostics import cross_validation
from fbprophet.diagnostics import performance_metrics
from matplotlib import pyplot as plt
from matplotlib.dates import MonthLocator, num2date
from matplotlib.ticker import FuncFormatter

import numpy as np

import Model_Class as MC


def Model_2(file, days, train_time):
    #データベース呼びだし
    dbname = (str(file))
    db = sqlite3.connect(dbname)
    
    #PandasでDBの値を読み込み
    df_db = pd.read_sql('SELECT * FROM price', db)
    
    #欲しいデータのみ抜き出し
    df_db = df_db.rename(columns={'日付': 'ds', '終値調整': 'y'})
    df_db = df_db[["ds", "y", "code"]]
    
    #コードの一意なリスト抜き出し
    code_lists = df_db["code"].unique()
    
    #モデル格納リストなどの初期化
    model_on_code = [] 
    future_data_on_code = [] 
    forecast_data_on_code = [] 
    df_CV = []
    df_performance = []
    
    figlist = []
    
    for i, code in enumerate(code_lists):

        #証券コードごとに分析
        df_tmp = df_db.loc[df_db["code"]==code]
        df_tmp.reset_index(drop=True, inplace=True)
        rows = len(df_tmp)
        
        try :
            df_tmp = df_tmp.astype({'y': float})
                        
            #ハイパーパラメータに合わせたモデル作成
            cap = int(np.percentile(df_tmp.y,95))
            floor = int(np.percentile(df_tmp.y,5))
            
            #モデル作成
            Hyper_model = MC.hyper_search_model(code, days, train_time)
            Hyper_model.Create_Model(df_tmp)
        
            
            df_tmp['cap']=cap
            df_tmp['floor']=floor

            #モデルフィット
            model_on_code.append(Hyper_model.model)
            model_on_code[i].fit(df_tmp)
            
            #予測していく
            future_data_on_code.append(Hyper_model.Hyper_FutureFrame())
            future_data_on_code[i]['cap'] =cap
            future_data_on_code[i]['floor'] =floor
            forecast_data_on_code.append(model_on_code[i].predict(future_data_on_code[i]))
            
        except (ValueError, IndexError, AttributeError): 
            '''
            ハイパーパラメータの探索が何らかの要因でうまくいかなかった場合
            デフォルトのパラメータを使用し、モデル作成
            '''
           #デフォルトでのモデル作成
            Nomal_model = MC.Model_Nomal_Prophet(code, days)
            #モデルフィット
            model_on_code.append(Nomal_model.model)
            model_on_code[i].fit(df_tmp)
             #予測していく
            future_data_on_code.append(Nomal_model.Nomal_FutureFrame())
            
            forecast_data_on_code.append(model_on_code[i].predict(future_data_on_code[i]))
        
        #プロット
        fig0 = model_on_code[i].plot(forecast_data_on_code[i], xlabel='Date', ylabel=str(code)+': Adj Close', figsize=(6.5, 5)) 
        fig1 = model_on_code[i].plot_components(forecast_data_on_code[i], figsize=(6.5, 6))
        
        #モデル評価のための交差検証(Cross_Validation)
        df_CV.append(cross_validation(model_on_code[i], initial='1 days', period=str(rows/8)+' days', horizon=str(rows/4)+' days'))
        
        df_performance.append(performance_metrics(df_CV[i]))
        
        #モデル評価の見える化
        draw = MC.figure_draw()
        fig2 = draw.plot_MSE_MAPE(df_performance[i])
        fig2.tight_layout()
        
        figlist.append([code, fig0, fig1, fig2])
        
        
    db.close()
    
    return figlist, len(code_lists)
    

