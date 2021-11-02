# Scraping and Machine learning

株価スクレイピングとProphetを用いた株価予想（機械学習）。

上記２機能を備えたアプリ。
 
# DEMO
 
以下図のように株価を予測できる。

![Prophet_img](https://user-images.githubusercontent.com/89838264/139519280-7a94aa1e-3483-4064-9f6b-5f98e371c124.jpeg)

GUIの例は以下の図である。

※そこまで分かりやすいものではないかもしれないが。

![GUI](https://user-images.githubusercontent.com/89838264/139519752-b5587cbb-6a3b-4d8d-a3c2-1257ed83a5a2.png)

 
# Requirement
本アプリで必要となるPythonパッケージを以下に記載する。
※環境は基本的にWindows依存

```bash
pandas                    1.3.3
requests                  2.26.0
bs4                       0.0.1
sqlite3                   3.8.6
tk                        8.6.11
matplotlib                3.4.3
numpy                     1.19.5
optuna                    2.10.0
scikit-learn              0.24.2

#Cython, pystan等色々依存あり
fbprophet                 0.7.1

#任意
jupyter                   1.0.0
reppy                     0.4.14
```

 
# Installation
 
Requirementで列挙したライブラリのインストールは基本的にymlの仮想環境を構築してもらうことになるが
その前に、以下のコマンドで`conda`は最新化しておいたほうがいいだろう。
また`git`コマンドも使うので入れておく。

```bash
conda update conda
conda install -c anaconda git
```
 
# Usage
 
本アプリの使い方は以下を実行。
実行後はGUIにしたがって入力。

ProphetのHyper_Modelはものすごく時間がかかります。
ハイスぺのPCを使用することをオヌヌメします。
※CPUは16Gはほしいなぁ、GPUは死ぬほど欲しい。

```bash
#gitクローン
git clone https://github.com/schecthellraiser606/Stock_price_scraping_and_Predict

#conda仮想環境構築
#以下の２行のうちどちらか選択（基本上にしておけばOS依存せずにコマンドは走るが、エラーが出ないとは言ってない）
conda env create -f ./anaconda/Scraping-Learning.yml
conda create -n Scraping-Learning -f ./anaconda/Scraping-Learning.yml

#仮想環境へ移動
conda activate Scraping-Learning

#実行
cd ./code
python main.py

```
 
# Note
 
注意点としては、スクレイピングを行えるサイトは限られるので、しっかり各サイトの「robots.txt」を確認しよう。

`ipynb`形式で簡易にスクレイピングOKかどうか確認できるソースを組んだので、活用をしてみてほしい。

これで`False`が出た場合は一度ブラウザ直打ちで確認してみるのもいいだろう。

※サイトによって「robots.txt」の記載方法が違うため。


```Python
from reppy.robots import Robots

robots = Robots.fetch('https://...../robots.txt')
print(robots.allowed('https://...', '*'))
```
 
# Author

* 作成者：schecthellraiser606 
