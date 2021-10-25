import tkinter
from tkinter import Entry, ttk
from tkinter import filedialog
from tkinter import messagebox
import CreateDB as CDB
import sys

#validation を行う関数を作成する   
def isOk(diff):
  
  if not diff.encode('utf-8').isdigit():
      # 妥当でない（半角数字でない）場合はFalseを返却
      return False

  # 妥当（半角数字である）の場合はTrueを返却
  return True


# メインウィンドウ
main_win = tkinter.Tk()
main_win.title("DATA to DB")
main_win.geometry("600x500")

# メインフレーム
main_frm = ttk.Frame(main_win)
main_frm.grid(column=0, row=0, sticky=tkinter.NSEW, padx=5, pady=10)

# ウィジェット作成（フォルダパス）
file_label = ttk.Label(main_frm, text="ファイル作成")

def ask_file():
    """ 作成ボタンの動作
    """
    filename = filedialog.asksaveasfilename(
    title = "名前を付けて保存",
    filetypes = [("DB", ".db")], # ファイルフィルタ
    initialdir = "./DB", # 自分自身のディレクトリ
    defaultextension = "db"
    )
    
    file_path.set(filename)
    
file_path = tkinter.StringVar()
file_box = ttk.Entry(main_frm, textvariable=file_path)
file_btn = ttk.Button(main_frm, text="参照", command=ask_file) 


#作成したisOk関数を基にしたTcl関数を作成する
tcl_isOk = main_win.register(isOk)

#証券コードウィジェット定義、一旦５つ分
Code_Number_1= tkinter.StringVar()
Code_label_1 = ttk.Label(main_frm, text="証券コード: 1")
Code_box_1 = ttk.Entry(main_frm, textvariable=Code_Number_1, validate='key', validatecommand=(tcl_isOk, '%S'))
Code_box_1.insert(0,"1308")

Code_Number_2= tkinter.StringVar()
Code_label_2 = ttk.Label(main_frm, text="証券コード: 2")
Code_box_2 = ttk.Entry(main_frm, textvariable=Code_Number_2, validate='key', validatecommand=(tcl_isOk, '%S'))
Code_box_2.insert(0,"1308")

Code_Number_3= tkinter.StringVar()
Code_label_3 = ttk.Label(main_frm, text="証券コード: 3")
Code_box_3 = ttk.Entry(main_frm, textvariable=Code_Number_3, validate='key', validatecommand=(tcl_isOk, '%S'))
Code_box_3.insert(0,"1308")

Code_Number_4= tkinter.StringVar()
Code_label_4 = ttk.Label(main_frm, text="証券コード: 4")
Code_box_4 = ttk.Entry(main_frm, textvariable=Code_Number_4, validate='key', validatecommand=(tcl_isOk, '%S'))
Code_box_4.insert(0,"1308")

Code_Number_5= tkinter.StringVar()
Code_label_5 = ttk.Label(main_frm, text="証券コード: 5")
Code_box_5 = ttk.Entry(main_frm, textvariable=Code_Number_5, validate='key', validatecommand=(tcl_isOk, '%S'))
Code_box_5.insert(0,"1308")

#取得年数ウィジェット定義
Year_module = ('1', '2', '3', '4', '5') #5年上限
Year_label = ttk.Label(main_frm, text="取得年数")
v = tkinter.StringVar()
Year_Box = ttk.Combobox(main_frm,textvariable= v, values=Year_module)
Year_Box.current(0)

#スクレイピング、データベース作成関数へ丸投げ
def SQL():
  f = open(file_path.get(), 'w')
  f.write('')
  f.close()
  
  #証券コードエントリーの中身を配列統合
  entries = []
  if Code_box_1.get():
    entries.append(Code_box_1.get())
  if Code_box_2.get():
    entries.append(Code_box_2.get())
  if Code_box_3.get():
    entries.append(Code_box_3.get())
  if Code_box_4.get():
    entries.append(Code_box_4.get())
  if Code_box_5.get():
    entries.append(Code_box_5.get())
  
  #関数へ渡す際の空白判定 
  if  file_path.get() and entries and Year_Box.get():
    CDB.Create(str(file_path.get()), list(set(entries)), int(Year_Box.get()))
    
  else:
      if not entries:
        messagebox.showwarning('Warning', '`証券コードがよろしくありません')
        
      if not file_path.get():
        messagebox.showwarning('Warning', 'ファイルパスがよろしくありません')
        
      if not Year_Box.get():
        messagebox.showwarning('Warning', '取得年数がよろしくありません')
      sys.exit()  
  
  messagebox.showinfo("Status", "Finish")
  main_win.after(2000, lambda: main_win.destroy()) 

# ウィジェット作成（実行ボタン）
app_btn = ttk.Button(main_frm, text="実行", command=SQL)

file_label.grid(column=0, row=0, pady=10)
file_box.grid(column=1, row=0, sticky=tkinter.EW, padx=5)
file_btn.grid(column=2, row=0)
Year_label.grid(column=0, row=1)
Year_Box.grid(column=1, row=1, sticky=tkinter.W, padx=5)

Code_label_1.grid(column=3, row=0)
Code_box_1.grid(column=4, row=0, padx=10, pady=5)

Code_label_2.grid(column=3, row=1)
Code_box_2.grid(column=4, row=1, padx=10, pady=5)

Code_label_3.grid(column=3, row=2)
Code_box_3.grid(column=4, row=2, padx=10, pady=5)

Code_label_4.grid(column=3, row=3)
Code_box_4.grid(column=4, row=3, padx=10, pady=5)

Code_label_5.grid(column=3, row=4)
Code_box_5.grid(column=4, row=4, padx=10, pady=5)

app_btn.grid(column=1, row=10)

main_win.mainloop()