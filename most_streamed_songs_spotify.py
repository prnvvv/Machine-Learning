import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import r2_score

filePath = r"C:\Users\Prannavakhanth\Documents\Machine-Learning\Most Streamed Spotify Songs 2024.csv"

try:
    dataFrame = pd.read_csv(filePath, encoding='utf-8')
except UnicodeDecodeError:
    try:
        dataFrame = pd.read_csv(filePath, encoding='latin1')
    except UnicodeDecodeError:
        dataFrame = pd.read_csv(filePath, encoding='cp1252')

dataFrame = dataFrame.dropna(axis = 0)

X = dataFrame[['Artist','All Time Rank', 'Spotify Streams',
       'Spotify Playlist Count', 'Spotify Playlist Reach',
       'Spotify Popularity', 'YouTube Views', 'YouTube Likes', 'TikTok Posts',
       'TikTok Likes', 'TikTok Views', 'YouTube Playlist Reach',
       'Apple Music Playlist Count', 'AirPlay Spins', 'SiriusXM Spins',
       'Deezer Playlist Count', 'Deezer Playlist Reach',
       'Amazon Playlist Count', 'Pandora Streams', 'Pandora Track Stations',
       'Soundcloud Streams', 'Shazam Counts', 'Explicit Track']]

y = dataFrame['Track Score']

trainX, testX, trainy, testy = train_test_split(X, y, test_size = 0.25, random_state = 1)

model = RandomForestClassifier(random_state = 1)

model.fit(trainX, trainy)

prediction = model.predict(testX)

accuracy = model.score(testX, testy)
print(f'Accuracy: {accuracy:.2f}')

r2 = r2_score(testy, prediction)
print(f'R-squared score: {r2:.2f}')
