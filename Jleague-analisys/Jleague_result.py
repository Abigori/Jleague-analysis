import csv

# CSVを読み込み、辞書リストとして保持
teams = []
with open("./Jleague_score.csv", "r", encoding="cp932") as f:
    lines = f.readlines()
    headers = lines[0].strip().strip('"').split(",")  # ヘッダーを整形
    for line in lines[1:]:
        values = line.strip().strip('"').split(",")   # 各行を整形
        row = dict(zip(headers, values))
        teams.append(row)

# 勝ち点を計算する関数
def calc_points(team):
    return int(team['勝ち']) * 3 + int(team['引き分け'])

# 各チームに勝ち点を追加
for t in teams:
    t["勝ち点"] = calc_points(t)

# 勝ち点でソートして順位を決定
ranking = sorted(teams, key=lambda x: x["勝ち点"], reverse=True)

# 結果を表示&ファイルに保存
with open("Jleague_ranking.txt", "w", encoding="cp932") as f:
    for i, team in enumerate(ranking, 1):
        line = f"{i}位: {team['チーム名']} (勝点: {team['勝ち点']})\n"
        print(line.strip())
        f.write(line)
