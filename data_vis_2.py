import pandas as pd
from matplotlib import pyplot as plt
from wordcloud import WordCloud

def genre_analysis():
    steam_data = pd.read_csv('steam_games')

    genre_combinations = (steam_data['genre'].value_counts()).to_dict()

    simp_genre_combinations = (steam_data['genre'].value_counts())[:20].to_dict()

    genres_set = {}

    for genres in steam_data['genre']:
        if len(genres_set) == 0 and not(type(genres) == float):
            temp = genres.split(", ")
            genres_set = set(temp)
        elif not(type(genres) == float):
            temp = genres.split(", ")
            genres_set.update(set(temp))

    genres_set = sorted(genres_set)

    genre_dict = dict.fromkeys(genres_set, 0)

    for item in genres_set:
        temp = 0
        for key in genre_combinations.keys():
            if item in key:
                temp = temp + genre_combinations[key]
                genre_dict[item] = temp

    plt.style.use('seaborn-dark')

    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)

    ax1.set_title("How many Games in a Genre")
    ax1.set_xlabel("Game Count")
    ax1.set_ylabel("Genres")

    ax1.barh(list(genre_dict.keys()), genre_dict.values())

    ax2.set_title("Top 20 Genre Combinations")
    ax2.set_xlabel("Game Count")
    ax2.set_ylabel("Genres Combos")

    ax2.barh(list(simp_genre_combinations.keys()), simp_genre_combinations.values())

    wordcloud_genres = WordCloud(width=2560, height=1440, background_color='white').generate_from_frequencies(
                    frequencies=genre_dict)

    plt.figure()
    plt.imshow(wordcloud_genres)
    plt.axis("off")
    
    wordcloud_combos = WordCloud(width=2560, height=1440, background_color='white').generate_from_frequencies(
                    frequencies=genre_combinations)

    plt.figure()
    plt.imshow(wordcloud_combos)
    plt.axis("off")

    plt.subplot_tool()
    plt.show()


if __name__ == "__main__":
    genre_analysis()