import pandas as pd
from matplotlib import pyplot as plt

def visualize_owner_to_pos_revs():
    steam_data = pd.read_csv('steam_games')

    owners = steam_data['owners']
    positive_revs = steam_data['positive_rev']
    negative_revs = steam_data['negative_rev']

    simp_owners = []
    percent_of_pos_rev = []

    for amount in owners:
        temp = amount.split(" .. ")
        simp_owners.append(temp[1])

    for rev in range(len(positive_revs)):
        percent = positive_revs[rev] / (positive_revs[rev] + negative_revs[rev])
        percent_of_pos_rev.append(percent)

    plt.style.use('seaborn')

    plt.scatter(simp_owners, positive_revs, c=percent_of_pos_rev, cmap="Greens", edgecolor='black', 
        linewidth=1, alpha=0.75)

    cbar = plt.colorbar()
    cbar.set_label('Percent of Positive Reviews')

    plt.yscale('log')

    plt.title('Owner count to Positive Reviews')
    plt.xlabel('Rough Estimate of Owners')
    plt.ylabel('Positive Reviews')

    plt.show()
    


if __name__ == "__main__":
    visualize_owner_to_pos_revs()