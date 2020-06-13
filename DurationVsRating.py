import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("datasets_211826_461395_Bojack Horseman Ratings (Season 1-5).csv")

durationmean = round(df["EPISODE TIME (NETFLIX)"].mean(), 2)
ratingmean = (df["RATING (IMDB)"].mean())
dfNamRatDur = df[['SEASON + EPISODE', 'EPISODE TIME (NETFLIX)', 'RATING (IMDB)']]

moremeantimeandrating = len((dfNamRatDur.where(dfNamRatDur['EPISODE TIME (NETFLIX)'] > durationmean).where(
    dfNamRatDur['RATING (IMDB)'] > ratingmean).dropna()))
moremeantimelessrating = len((dfNamRatDur.where(dfNamRatDur['EPISODE TIME (NETFLIX)'] < durationmean).where(
    dfNamRatDur['RATING (IMDB)'] > ratingmean).dropna()))

objects = ('> duration mean', '< duration mean')
y_pos = np.arange(len(objects))
performance = moremeantimeandrating, moremeantimelessrating
plt.bar(y_pos, performance, align='center', alpha=0.5, color='g')
plt.xticks(y_pos, objects)
plt.ylabel('Rating')
plt.title('Duration mean vs Rating')
#plt.savefig("duration_rating.png")
plt.show()