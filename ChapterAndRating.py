import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datasets_211826_461395_Bojack Horseman Ratings (Season 1-5).csv")
"""pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)"""

"""Graphs Chapter x Rating """

"""During 2014"""
in_2014 = df[df["YEAR"] == 2014]
mean14 = (in_2014["RATING (IMDB)"].mean())
print("Mean 2014 rating:", mean14)
rating_2014 = in_2014["RATING (IMDB)"]
sea_epi = in_2014["SEASON + EPISODE"]
plt.plot(rating_2014, sea_epi, '-o')
plt.title("Rating 2014 BJH")
plt.xlabel("Rating")
plt.ylabel("Chapter")
plt.savefig("rating_2014.png")
plt.show()

"""During 2015"""
in_2015 = df[df["YEAR"] == 2015]
mean15 = (in_2015["RATING (IMDB)"].mean())
print("Mean 2015 rating:", mean15)
rating_2015 = in_2015["RATING (IMDB)"]
sea_epi = in_2015["SEASON + EPISODE"]
plt.plot(rating_2015, sea_epi, '-o')
plt.title("Rating 2015 BJH")
plt.xlabel("Rating")
plt.ylabel("Chapter")
plt.savefig("rating_2015.png")
plt.show()

"""During 2016"""
in_2016 = df[df["YEAR"] == 2016]
mean16 = (in_2016["RATING (IMDB)"].mean())
print("Mean 2016 rating:", mean16)
rating_2016 = in_2016["RATING (IMDB)"]
sea_epi = in_2016["SEASON + EPISODE"]
plt.plot(rating_2016, sea_epi, '-o')
plt.title("Rating 2016 BJH")
plt.xlabel("Rating")
plt.ylabel("Chapter")
plt.savefig("rating_2016.png")
plt.show()

"""During 2017"""
in_2017 = df[df["YEAR"] == 2017]
mean17 = (in_2017["RATING (IMDB)"].mean())
print("Mean 2017 rating:", mean17)
rating_2017 = in_2017["RATING (IMDB)"]
print(rating_2017)
sea_epi = in_2017["SEASON + EPISODE"]
plt.plot(rating_2017, sea_epi, '-o')
plt.title("Rating 2017 BJH")
plt.xlabel("Rating")
plt.ylabel("Chapter")
plt.savefig("rating_2017.png")
plt.show()

"""During 2018"""
in_2018 = df[df["YEAR"] == 2018]
mean18 = (in_2018["RATING (IMDB)"].mean())
print("Mean 2018 rating:", mean18)
rating_2018 = in_2018["RATING (IMDB)"]
sea_epi = in_2018["SEASON + EPISODE"]
plt.plot(rating_2018, sea_epi, '-o')
plt.title("Rating 2018 BJH")
plt.xlabel("Rating")
plt.ylabel("Chapter")
plt.savefig("rating_2018.png")
plt.show()

"""General mean"""
finalMean = round((df["RATING (IMDB)"].mean()),2)
print("General mean rating =", finalMean)