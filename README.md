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
```

 
# Installation
 
Requirementで列挙したライブラリのインストール方法
`conda`（Anaconda利用者）や`pip`コマンドで適当にインストールしてください。
※デフォルトでインストールされているものもありますので注意
※インストールの前に`pip`、`conda`等、今あるものは最新化しておきましょう。
 

```bash:例
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

#このパラメータ探索PKGはPATH
conda install -c conda-forge optuna

conda install -c anaconda scikit-learn

pip install jupyter
pip install ipython
pip install notebook
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
 
注意点
 
# Author

* 作成者：schecthellraiser606 
