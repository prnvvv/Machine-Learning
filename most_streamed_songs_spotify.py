import pandas as pd

filePath = r"C:\Users\Prannavakhanth\Documents\Machine-Learning\Most Streamed Spotify Songs 2024.csv"

# Try different encodings if one fails
try:
    dataFrame = pd.read_csv(filePath, encoding='utf-8')
except UnicodeDecodeError:
    try:
        dataFrame = pd.read_csv(filePath, encoding='latin1')
    except UnicodeDecodeError:
        dataFrame = pd.read_csv(filePath, encoding='cp1252')

print(dataFrame.head())
