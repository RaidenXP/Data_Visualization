import pandas as pd
from matplotlib import pyplot as plt

def visualize_owner_to_pos_revs():
    steam_data = pd.read_csv('steam_games')

    owners = steam_data['owners']
    positive_revs = steam_data['positive_rev']
    negative_revs = steam_data['negative_rev']

    simp_owners = []
    percent_of_pos_rev = []

    for instances in owners:
        temp = instances.split(" .. ")
        simp_owners.append(int(temp[1].replace(",", "")))

    for rev in range(len(positive_revs)):
        if (positive_revs[rev] + negative_revs[rev]) == 0:
            percent_of_pos_rev.append(0)
        else:
            percent = positive_revs[rev] / (positive_revs[rev] + negative_revs[rev])
            percent_of_pos_rev.append(percent)

    plt.scatter(simp_owners, positive_revs, c=percent_of_pos_rev, cmap="Greens", edgecolor='black',
        linewidth=1, alpha=0.75)

    cbar = plt.colorbar()
    cbar.set_label('Percent of Positive Reviews')

    plt.xscale('log')
    plt.yscale('log')

    plt.title('Owner count to Positive Reviews')
    plt.xlabel('Rough Estimate of Owners')
    plt.ylabel('Positive Reviews')

    plt.show()
    


if __name__ == "__main__":
    visualize_owner_to_pos_revs()