import tkinter
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import sys

from Predict_Model_1 import Model_1
from Predict_Model_2 import Model_2
import GUI_plot as gpl

#validation を行う関数を作成する   
def isOk(diff):
  
  if not diff.encode('utf-8').isdigit():
      # 妥当でない（半角数字でない）場合はFalseを返却
      return False

  # 妥当（半角数字である）の場合はTrueを返却
  return True




def Predict_win(win):
  win.destroy()
  # メインウィンドウ
  main_win = tkinter.Tk()
  main_win.title("Predict")
  main_win.geometry("680x280")
  
  def _destroyWindow():
    main_win.quit()
    main_win.destroy()
    
  main_win.protocol('WM_DELETE_WINDOW', _destroyWindow) 
  
  # メインフレーム
  main_frm = ttk.Frame(main_win)
  main_frm.grid(column=0, row=0, sticky=tkinter.NSEW, padx=5, pady=10)
  
 
  
  # ウィジェット作成（モデル選択）
  model_select_label = ttk.Label(main_frm, text="モデル選択")
  model_list = ('Nomal_Prophet', 'Hyper_Prophet') #5年上限
  v = tkinter.StringVar()
  model_Box = ttk.Combobox(main_frm,textvariable= v, values=model_list)
  model_Box.current(0)
  
  
  #モデル詳細設定
  def model_para():
    # ウィジェット作成（フォルダパス）
    file_label = ttk.Label(main_frm, text="ファイル選択")
    file_label.grid(column=0, row=1)
    file_path = tkinter.StringVar()
    file_box = ttk.Entry(main_frm, textvariable=file_path)
    file_box.grid(column=1, row=1, sticky=tkinter.EW, padx=5)
    
    
    def ask_file():
      """ 参照ボタンの動作
      """
      filename = filedialog.askopenfilename(
      title = "開く",
      filetypes = [("DB", ".db")], # ファイルフィルタ
      initialdir = "../BeautifulSoup_Data/DB", # 自分自身のディレクトリ
      defaultextension = "db"
      )
      
      file_path.set(filename)
    
    file_btn = ttk.Button(main_frm, text="参照", command=ask_file) 
    file_btn.grid(column=2, row=1)
    
    
    #予測期間選択
    tcl_isOk = main_win.register(isOk)
    During_day_Number= tkinter.StringVar()
    During_label = ttk.Label(main_frm, text="予測する日数(ex.31 :一か月)")
    During_label.grid(column=0, row=2)
    During_Box = ttk.Entry(main_frm, textvariable=During_day_Number, validate='key', validatecommand=(tcl_isOk, '%S'))
    During_Box.insert(0,"62")
    During_Box.grid(column=1, row=2, padx=10, pady=5)
    
    #ハイパーモデルの際のパラメータ探索期間指定
    if model_Box.get() == 'Nomal_Prophet' :
      pass
    elif model_Box.get() == 'Hyper_Prophet':
      train_label = ttk.Label(main_frm, text="1証券毎のパラメータ探索秒数(10秒とかで)")
      train_label.grid(column=2, row=2)
      train_Number = tkinter.StringVar()
      train_Box = ttk.Entry(main_frm, textvariable=train_Number, validate='key', validatecommand=(tcl_isOk, '%S'))
      train_Box.insert(0,"20")
      train_Box.grid(column=3, row=2)
      
      warr_label = ttk.Label(main_frm, text="Hyperを使う貴様は相当★暇★であるようだな！", font=('Ricty Diminished', 16, 'underline'))
      warr_label.grid(column=0, row=4, columnspan=3, pady=10)
    else :
      messagebox.showwarning('Warning', 'モデルが存在しません')
      sys.exit() 
      
    
    #実行処理  
    def Predict_exe():
      
      app_btn.config(state=tkinter.DISABLED)
      model_btn.config(state=tkinter.DISABLED)
      file_btn.config(state=tkinter.DISABLED)

      
      if model_Box.get() == 'Nomal_Prophet' :#デフォルトモデル
        
        #関数へ渡す際の空白判定
        if file_path.get() and During_Box.get():        
          
          figlist, num = Model_1(str(file_path.get()), int(During_Box.get()))        
          gpl.plot(main_win, figlist, num)
        
        else:
          if not file_path.get():
            messagebox.showwarning('Warning', 'ファイルパスがよろしくありません')
          if not During_Box.get():
            messagebox.showwarning('Warning', '予測期間がよろしくありません') 
          sys.exit() 
        
      elif model_Box.get() == 'Hyper_Prophet':#ハイパーモデル
        
        #関数へ渡す際の空白判定
        if file_path.get() and During_Box.get() and train_Box.get():
          
          figlist, num = Model_2(str(file_path.get()), int(During_Box.get()), int(train_Box.get()))                  
          gpl.plot(main_win, figlist, num)

        else:
          if not file_path.get():
            messagebox.showwarning('Warning', 'ファイルパスがよろしくありません')
          if not During_Box.get():
            messagebox.showwarning('Warning', '予測期間がよろしくありません') 
          if not train_Box.get():
            messagebox.showwarning('Warning', 'パラメータ探索期間がよろしくありません') 
          sys.exit() 
        
      else :#モデルの指定がよろしくないときの処理
        messagebox.showwarning('Warning', 'モデルが存在しません')
        sys.exit() 
    
      

           
    
    #実行ボタン
    app_label_1 = ttk.Label(main_frm, text="死ぬほど時間かかるよ★")
    app_label_1.grid(column=0, row=9, columnspan=1)
    app_label_2 = ttk.Label(main_frm, text="応答あるまで待ってね★")
    app_label_2.grid(column=0, row=10, columnspan=1)
    
    app_btn = ttk.Button(main_frm, text="実行", command=Predict_exe)
    app_btn.grid(column=2, row=10)
    
      
     
  #詳細指定ボタン
  model_btn = ttk.Button(main_frm, text="詳細設定へ", command=model_para)
  
  model_select_label.grid(column=0, row=0, pady=10)
  model_Box.grid(column=1, row=0, sticky=tkinter.EW, padx=5)
  model_btn.grid(column=2, row=0)
  
  main_win.mainloop()