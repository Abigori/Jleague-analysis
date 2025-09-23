# J-League 2021 Ranking Analysis

このリポジトリでは、2021年Jリーグの試合結果データを用いて **各チームの勝ち点・得点を集計し、ランキングを可視化** しています。  
Python（pandas / matplotlib）を使って、上位3チーム・下位3チームを強調表示した棒グラフを描画するサンプルコードです。

---

## 📂 ディレクトリ構成
Jleague_2021_Ranking/
├── Jleague_2021_result.csv # Jリーグ2021シーズンの試合結果データ
├── jleague_analysis.py # 分析用スクリプト（このリポジトリのメイン）
└── README.md

## 🚀 使い方

1. リポジトリをクローン
   ```bash
   git clone https://github.com/yourname/Jleague_2021_Ranking.git
   cd Jleague_2021_Ranking

2. 必要なライブラリをインストール
pip install pandas matplotlib

3. スクリプトを実行
python jleague_analysis.py


📊 分析内容
▪ホームチームとアウェイチームの勝ち点を計算
▪各チームのホーム＋アウェイ成績を統合
▪平均勝ち点、標準偏差、平均得点を出力
▪勝ち点順にソートし、上位3チーム・下位3チームを強調して可視化

出力されるグラフイメージ：
▪棒グラフで全チームの勝ち点を表示
▪上位3チーム：赤色
▪下位3チーム：青色

🛠 使用技術
▪Python 3.11.0
▪pandas
▪matplotlib