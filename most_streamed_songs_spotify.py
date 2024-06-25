import pandas as pd
import numpy as np

filePath = r"C:\Users\Prannavakhanth\Documents\Machine-Learning\Most Streamed Spotify Songs 2024.csv"

try:
    dataFrame = pd.read_csv(filePath, encoding='utf-8')
except UnicodeDecodeError:
    try:
        dataFrame = pd.read_csv(filePath, encoding='latin1')
    except UnicodeDecodeError:
        dataFrame = pd.read_csv(filePath, encoding='cp1252')

print(dataFrame.columns)
