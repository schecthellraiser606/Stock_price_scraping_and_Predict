import tkinter
from tkinter import ttk
from matplotlib import pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot(win, fig, num):
  win.destroy()
  # メインウィンドウ
  plot_win = tkinter.Tk()
  plot_win.title("Plot Predict")
  plot_win.geometry("2400x1500")

  
  def _destroyWindow():
    plot_win.quit()
    plot_win.destroy()
  
  plot_win.protocol('WM_DELETE_WINDOW', _destroyWindow) 
  
  # メインフレーム
  plot_frm = ttk.Frame(plot_win)
  plot_frm.grid(column=0, row=0, sticky=tkinter.NSEW, padx=5, pady=10)
  
  # 各グラフプロット
  for i in range(num):
    # 証券コード名前表示
    Code_label = ttk.Label(plot_frm, text="証券コード :" + str(fig[i][0]), font=('Ricty Diminished', 16, 'underline'))
    Code_label.grid(column=i, row=0, pady=10)
    
    # 予測グラフ
    plot_predict_label= ttk.Label(plot_frm, text='plot_predict')
    plot_predict_label.grid(column=i, row=1, pady=5)
    
    canvas0 = FigureCanvasTkAgg(fig[i][1], master=plot_frm)
    canvas0.get_tk_widget().grid(column=i, row=2, pady=5, sticky=tkinter.NSEW)
    canvas0.draw()
    
    # トレンド等のグラフ    
    components_label= ttk.Label(plot_frm, text='components')
    components_label.grid(column=i, row=3, pady=5)

    canvas1 = FigureCanvasTkAgg(fig[i][2], master=plot_frm)
    canvas1.get_tk_widget().grid(column=i, row=4, pady=5, sticky=tkinter.NSEW)
    canvas1.draw()
    
    # 簡易評価関数    
    perfomance_label= ttk.Label(plot_frm, text='perfomance')
    perfomance_label.grid(column=i, row=5, pady=5)
    
    canvas2 = FigureCanvasTkAgg(fig[i][3], master=plot_frm)
    canvas2.get_tk_widget().grid(column=i, row=6, pady=5, sticky=tkinter.NSEW)
    canvas2.draw()
    
  plot_win.mainloop()
    
    
  