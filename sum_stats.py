import pandas as pd
import sys

def sum_stats():
    steam_data = pd.read_csv('steam_games')

    sum_stat_pos_revs = steam_data['positive_rev'].describe()

    sum_stat_genre = steam_data['genre'].describe()

    with open('sum_stats.txt', 'w') as f:
        print(sum_stat_pos_revs, file=f)
        print(sum_stat_genre, file=f)