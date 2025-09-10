import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib

teams = np.array([
    "鹿島アントラーズ", "浦和レッズ", "柏レイソル", "FC東京", "東京V", "町田ゼルビア", "川崎F", "横浜FM", "横浜FC", "湘南ベルマーレ",
    "新潟アルビレックス", "清水エスパルス", "名古屋グランパス", "京都サンガ", "G大阪", "C大阪", "ヴィッセル神戸", "ファジアーノ岡山", "サンフレッチェ広島",
    "アビスパ福岡"
    ])

#勝ち点(第28節終了時点)
points  = np.array([51, 44, 50, 30, 32, 50, 42, 25, 23, 25, 20, 
                    32, 28, 54, 37, 38, 53, 39, 49, 37])

#得点数(第28節終了時点)
goals = np.array([41, 39, 42, 30, 16, 45, 50, 26, 18, 26, 27, 
                  31, 34, 52,38, 42, 37, 26, 34, 28])

mean_points = np.mean(points)
median_points = np.median(points)
std_points = np.std(points)
print("【勝ち点分析】")
print(f"平均：{mean_points:.2f}、中央値：{median_points:.2f}、標準偏差：{std_points:.2f}")

if std_points < 5:
    print("➩勝ち点が団子状態で接戦！")
else:
    print("➩上位と下位で差が大きい可能性あり")

#得点力のZスコア分析
z_scores = (goals - np.mean(goals)) / np.std(goals)

print("\n【得点力スコア】")

for teams, z in zip(teams, z_scores):
    if z >= 1:
        label = "◎得点力高いチーム"
    elif z <=-1:
        label = "×得点力が低いチーム"
    else:
        label = "△平均的"
    print(f"{teams}:Z={z:.2f} ➩ {label}")

#勝ち点シミュレーション
np.random.seed(42)
target_team = "C大阪"
current_points = points[15]
remaining_games = 10

#勝率50%で勝ち/引き分け/負けを仮定
#勝ち=3点、引き分け=1点、負け=0点
simulations=[]
for _ in range(1000):
    results = np.random.choice([0, 1, 3], size=remaining_games, p=[0.25, 0.25, 0.5])
    total = current_points + np.sum(results)
    simulations.append(total)

simulations = np.array(simulations)

print(f"\n【{target_team}の勝ち点シミュレーション】")
print(f"予測範囲：{np.min(simulations)} ~ {np.max(simulations)}")
print(f"平均予測：{np.mean(simulations):.0f}")

#ヒストグラム描画
plt.hist(simulations, bins=15, edgecolor="black")
plt.title(f"{target_team} 勝ち点シミュレーション")
plt.xlabel("勝ち点")
plt.ylabel("出現回数")
plt.show()