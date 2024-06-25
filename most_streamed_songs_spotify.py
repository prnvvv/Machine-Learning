import numpy as np
import pandas as pd

filePath = "C:\Users\Prannavakhanth\Documents\Machine-Learning\Most Streamed Spotify Songs 2024.csv"

dataFrame = pd.read_csv(filePath)

print(dataFrame.head(10))