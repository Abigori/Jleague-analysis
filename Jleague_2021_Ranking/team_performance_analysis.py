import pandas as pd
import matplotlib.pyplot as plt

#CSVファイルを読み込む
file_path = "./Jleague_2021_Ranking/Jleague_2021_result.csv"
df=pd.read_csv(file_path)

"データの先頭５行を確認"
print(df.head())

#ホームチームの勝ち点
df["HomePoints"] = df.apply(
    lambda row: 3 if row["HomeGoal"] > row["AwayGoal"] else (1 if row["HomeGoal"] == row["AwayGoal"] else 0),
    axis=1
)

#アウェイチームの勝ち点
df["AwayPoints"] = df.apply(
    lambda row: 3 if row["AwayGoal"] > row["HomeGoal"] else (1 if row["AwayGoal"] == row["HomeGoal"] else 0),
    axis=1
)

print(df[["HomeTeam", "HomeGoal", "AwayGoal", "HomePoints", "AwayPoints"]])

#ホーム成績
home_stats = df.groupby("HomeTeam").agg(
    Points=("HomePoints", "sum"),
    Goals=("HomeGoal", "sum")
)

#アウェイ成績
away_stats = df.groupby("AwayTeam").agg(
    Points=("AwayPoints", "sum"),
    Goals=("AwayGoal", "sum")
)

#合算(チームごとに統合)
team_stats = home_stats.add(away_stats, fill_value=0).reset_index()
team_stats = team_stats.rename(columns={"HomeTeam": "Team"})

print(team_stats)
print("平均勝ち点:", team_stats["Points"].mean())
print("勝ち点の標準偏差:", team_stats["Points"].std())
print("平均得点:", team_stats["Goals"].mean())

#勝ち点で並び替え
team_stats_sorted = team_stats.sort_values("Points", ascending=False)

#上位3チームと下位3チームを表示
print("上位3チーム")
print(team_stats_sorted.head(3))
print("下位3チーム")
print(team_stats_sorted.tail(3))

#グラフ表示
plt.figure(figsize=(10,6))
plt.bar(team_stats_sorted["Team"], team_stats_sorted["Points"], color="gray")
plt.xticks(rotation=45, ha="right")
plt.title("J-league_2021_Ranking", fontsize=14)
plt.xlabel("Team")
plt.ylabel("Points")

#上位3チームのバーを赤色で強調
for i, team in enumerate(team_stats_sorted["Team"]):
    if i < 3:  #上位3
        plt.bar(team, team_stats_sorted.iloc[i]["Points"], color="red")

#下位3チームのバーを青色で強調
for i, team in enumerate(team_stats_sorted["Team"]):
    if i > 16:  #下位3
        plt.bar(team, team_stats_sorted.iloc[i]["Points"], color="blue")

plt.tight_layout()
plt.show()