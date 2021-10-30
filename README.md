# Scraping and Machine learning

株価スクレイピングとProphetを用いた株価予想（機械学習）

上記２機能を備えたアプリ
 
# DEMO
 

 
# Requirement
本アプリで必要となるPythonパッケージを以下に記載する。

```bash
pandas                    1.3.3
requests                  2.26.0
bs4                       0.0.1
lxml                      4.6.3
sqlite3                   3.8.6
tk                        8.6.11
matplotlib                3.4.3
fbprophet                 0.7.1
numpy                     1.19.5
optuna                    2.10.0
scikit-learn              0.24.2
ipython                   7.27.0
notebook                  6.4.3
jupyter                   1.0.0
reppy                     0.4.14
```

 
# Installation
 
Requirementで列挙したライブラリのインストール方法
`conda`（Anaconda利用者）や`pip`コマンドで適当にインストールしてください。

※デフォルトでインストールされているものもありますので注意

※インストールの前に`pip`、`conda`等、今あるものは最新化しておきましょう。
 
{例}

```bash
pip install pandas

pip install requests

pip install bs4
pip install lxml
conda install -c anaconda beautifulsoup4

conda install -c blaze sqlite3

conda install -c anaconda tk

pip install matplotlib

#このProphetをインストールする際にはWindowsの場合「C++」が必須で必要
#Anacondaでインストールしましょう
conda install -c conda-forge fbprophet

pip install numpy

#このパラメータ探索PKGはPATH関係でエラーが出やすい、PKG最新化をお忘れなく。
conda install -c conda-forge optuna

conda install -c anaconda scikit-learn

pip install jupyter
pip install ipython
pip install notebook

#このreppyをインストールする際には「C++」が必須で必要
pip install reppy
```
 
# Usage
 
本アプリの使い方は以下を実行。
実行後はGUIにしたがって入力。

ProphetのHyper_Modelはものすごく時間がかかります。
ハイスぺのPCを使用することをオヌヌメします。
※CPUは16Gはほしいなぁ、GPUは死ぬほど欲しい。

```bash
git clone https://github.com/schecthellraiser606/Stock_price_scraping_and_Predict
python main.py
```
 
# Note
 
注意点としては、スクレイピングを行えるサイトは限られるので、しっかり各サイトの「robots.txt」を確認しよう。

`ipynb`形式で簡易にスクレイピングOKかどうか確認できるソースを組んだので、活用をしてみてほしい。

これで`False`が出た場合は一度ブラウザ直打ちで確認してみるのもいいだろう。

※サイトによって「robots.txt」の記載方法が違うため。


```Python:Robots.ipynb
from reppy.robots import Robots

robots = Robots.fetch('https://...../robots.txt')
print(robots.allowed('https://...', '*'))
```
 
# Author

* 作成者：schecthellraiser606 
