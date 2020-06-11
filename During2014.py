import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datasets_211826_461395_Bojack Horseman Ratings (Season 1-5).csv")
"""pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)"""
in_2014 = df[df["YEAR"] == 2014]
mean = (in_2014["RATING (IMDB)"].mean())
print("Mean:", mean)
rating_2014 = in_2014["RATING (IMDB)"]
sea_epi = in_2014["SEASON + EPISODE"]
plt.plot(rating_2014, sea_epi, '-o')
plt.title("Rating 2014 BJH")
plt.xlabel("Rating")
plt.ylabel("Chapter")
plt.savefig("rating_2014.png")
plt.show()
