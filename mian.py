import tkinter
from tkinter import ttk

import os, sys
sys.path.append(os.getcwd() + '/BeautifulSoup_Data')
sys.path.append(os.getcwd() + '/Predict_Models')

import BeautifulSoup_Data.GUI_Scraping as SC
import Predict_Models.GUI_Predict as PR

  

def main():
  main_win = tkinter.Tk()
  main_win.title("Select function")
  main_win.geometry("300x300")
  
  def _destroyWindow():
    main_win.quit()
    main_win.destroy()
    
  main_win.protocol('WM_DELETE_WINDOW', _destroyWindow) 
  
  # メインフレーム
  main_frm = ttk.Frame(main_win, height=200)
  main_frm.pack(expand = True, fill = tkinter.Y)
  
  def Scraping():
    SC.Scraping_win(main_win)
    
  def Predict():
    PR.Predict_win(main_win)
    
  
  Scraping_Btn = ttk.Button(main_frm, text="スクレイピング", command=Scraping, width = 20)
  Scraping_Btn.pack(expand = True, fill = tkinter.X)
  
  Predict_Btn = ttk.Button(main_frm, text="予測(機械学習)", command=Predict, width = 20)
  Predict_Btn.pack(expand = True, fill = tkinter.X)
  
  main_win.mainloop()


if __name__ == "__main__":
    main()