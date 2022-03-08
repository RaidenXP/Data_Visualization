import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

def genre_analysis():
    steam_data = pd.read_csv('steam_games')

    genre_occurences = (steam_data['genre'].value_counts()).to_dict()

    genre_df = pd.DataFrame(genre_occurences.keys(), columns=['genre'])
    count_df = pd.DataFrame(genre_occurences.values(), columns=['count'])

    new_df = pd.merge(genre_df, count_df, left_index=True, right_index=True)

    #plt.bar(genre_occurences.keys(), genre_occurences.values())

    sns.catplot(x='genre', data=steam_data, kind='count')

    plt.show()

if __name__ == "__main__":
    genre_analysis()