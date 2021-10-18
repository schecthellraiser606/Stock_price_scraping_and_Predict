from pandas.core.frame import DataFrame
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import datetime
import time

def get_DataFrame(code, For_Years):
    """
    証券コードからスクレイピング情報を取得し、Datafrrameにして返す関数
    """
    
    main_url = 'https://kabuoji3.com/stock/'
    
     # 取得する年の割り出し
    today = datetime.date.today()
    years = [0] * For_Years 
    for i in range(For_Years):
      years[i] = today.year - i
          
    
    try:
      code_url = main_url + str(code) + "/" 
      
      #取得したHTMLからBeautifulSoupオブジェクト作成(First Page)
      response = requests.get(code_url)
      soup = bs(response.content, "html.parser")
      
      #証券コードを取得する
      code_name = soup.findAll("span", {"class":"jp"})[0]
      
      #ヘッダー(カラム)情報を取得する
      tag_thead_tr = soup.find('thead').find_all('tr')
      head = [h.text for h in tag_thead_tr[0].find_all('th')] 
      
      # 空DataFrameの作成
      df = pd.DataFrame(columns = head)
      
      time.sleep(0.5)
      
      
      # year年間の株価データの取得
      for year in years:
        url = code_url + str(year) + "/" 
      
        #取得したHTMLからBeautifulSoupオブジェクト作成(Year Pages)
        response = requests.get(url)
        soup = bs(response.content, "html.parser")

        #株価データを取得し、Dataframe化する
        table = soup.findAll("table", {"class":"stock_table stock_data_table"})[0]
        tag_tbody_tr = table.findAll("tr")[1:]

        data = []
        for i in range(len(tag_tbody_tr)):
            data.append([d.text for d in tag_tbody_tr[i].find_all('td')])
        df_tmp = pd.DataFrame(data, columns = head)
        df = pd.concat([df, df_tmp], ignore_index = True) #データを結合

        #codeカラムをassignでDataframeに新規追加する ※code_nameの最初の4桁までが証券コード
        df = df.assign(code=code_name.get_text()[:4])
        
        time.sleep(1)

    except (ValueError, IndexError, AttributeError):
        return None

    return df
  
  
def multi_Brand(code_range, years):
    """
    証券コードを生成し、取得した情報を結合する関数
    """

    #株価を入れる空のデータフレームを新規作成
    cols = ['日付', '始値', '高値', '安値', '終値', '出来高', '終値調整', 'code']
    df = pd.DataFrame(index=[], columns=cols)

    for code in code_range:          

        #生成した証券コードをスクレイピング関数へ渡す          
        brand = get_DataFrame(code, years)

        #情報が取得できていれば、情報を結合していく
        if brand is not None:
            df = pd.concat([df, brand]).reset_index(drop=True)                                  

        time.sleep(0.5)

    return df