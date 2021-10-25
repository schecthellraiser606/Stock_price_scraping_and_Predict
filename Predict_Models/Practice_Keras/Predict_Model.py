import sqlite3
from matplotlib.pyplot import axis
import numpy as np
import matplotlib.pylab as plt
import pandas as pd

import Model_Keras_Class as MK

def shape_data(data, axis=None):
  data_mean = data.mean(axis=axis, keepdims=True)
  data_std  = np.std(data, axis=axis, keepdims=True)
  data_zscore = (data-data_mean)/data_std
  return data_zscore

def load_data(data, n_prev = 31):  
   
    docX, docY = [], []
    for i in range(len(data)-n_prev):
        docX.append(data.iloc[i:i+n_prev])
        docY.append(data.iloc[i+n_prev])
    alsX = np.array(docX)
    alsY = np.array(docY)
    
    return alsX, alsY

def train_test_split(df, test_size=0.25, n_prev = 31):  
    """
    学習用とテスト用データを分割
    31日（だいたい1か月）の株価データを用いて翌日を予測する方針
    """
    ntrn = round(len(df) * (1 - test_size))
    ntrn = int(ntrn)
    X_train, y_train = load_data(df.iloc[0:ntrn], n_prev)
    X_test, y_test = load_data(df.iloc[ntrn:], n_prev)

    return (X_train, y_train), (X_test, y_test)
  

def Model_3(file, model_name, model_nummidle):
  #データベース呼びだし
    dbname = (str(file))
    db = sqlite3.connect(dbname)
    
    #PandasでDBの値を読み込み
    df_db = pd.read_sql('SELECT * FROM price', db)
    
    #欲しいデータのみ抜き出し,
    df_db = df_db.rename(columns={'日付': 'ds', '終値調整': 'y'})
    df_db = df_db[["ds", "y", "code"]]
    #コードの一意なリスト抜き出し
    code_lists = df_db["code"].unique()
    #データの整形（標準化）
    df_db = df_db.astype({'y': float})
    df_db['data_zscore'] = shape_data(df_db['y'].values)
    
    Keras_model = []
    predicted = []
    
    
    i = 0
    for code in code_lists:
      df_tmp = df_db.loc[df_db["code"]==code]
      df_tmp.reset_index(drop=True, inplace=True)
      
      length_of_sequences = 31
      (X_train, y_train), (X_test, y_test) = train_test_split(df_tmp['data_zscore'], test_size = 0.25, n_prev = length_of_sequences)
      
      X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
      y_train = np.reshape(y_train, (y_train.shape[0], 1))
      X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
      
      
      
      length_of_sequences = X_train.shape[1]
      Keras_model_tmp = MK.Keras_Model(model_name, model_nummidle)
      Keras_model.append(Keras_model_tmp.build_model(length_of_sequences))
      history = Keras_model[i].fit(X_train, y_train, batch_size=128, epochs=60, validation_split=0.2)
      
      predicted.append(Keras_model[i].predict(X_test))

      
      df_keras =  pd.DataFrame(predicted[i])
      df_keras.columns = ["predict"]
      df_keras["Stock price"] = y_test
      
      df_keras.plot()
      
      i += 1
      
      
          
    

