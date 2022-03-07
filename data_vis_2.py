from turtle import pos, position
import pandas as pd
from matplotlib import pyplot as plt

def genre_analysis():
    steam_data = pd.read_csv('steam_games')

    genre_occurences = (steam_data['genre'].value_counts()).to_dict()

if __name__ == "__main__":
    genre_analysis()