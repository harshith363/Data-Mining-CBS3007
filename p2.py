import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
# Replace with your actual file path
file_path = r'C:\Users\harsh\OneDrive\Documents\VIT\FALLSEM 24-25\CBS3007\DA1 main\oil-prices.csv'
data = pd.read_csv(file_path)

# Strip any leading or trailing spaces from column names
data.columns = data.columns.str.strip()

# Convert the 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'], format='%d-%m-%Y')

# Set the 'Date' column as the index
data.set_index('Date', inplace=True)

# Line Plot
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Motor Gasoline Price ($/gallon) Real'],
         marker='o', linestyle='-', color='b')
plt.title('Motor Gasoline Prices Over 25 Years (Line Plot)')
plt.xlabel('Date')
plt.ylabel('Price ($/gallon)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Bar Chart
plt.figure(figsize=(12, 6))
data['Motor Gasoline Price ($/gallon) Real'].resample(
    'Y').mean().plot(kind='bar', color='orange')
plt.title('Average Annual Motor Gasoline Prices (Bar Chart)')
plt.xlabel('Year')
plt.ylabel('Average Price ($/gallon)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Histogram
plt.figure(figsize=(12, 6))
plt.hist(data['Motor Gasoline Price ($/gallon) Real'],
         bins=20, color='green', edgecolor='black')
plt.title('Distribution of Motor Gasoline Prices (Histogram)')
plt.xlabel('Price ($/gallon)')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.show()

# Scatter Plot
plt.figure(figsize=(12, 6))
plt.scatter(
    data.index, data['Motor Gasoline Price ($/gallon) Real'], color='red', alpha=0.5)
plt.title('Motor Gasoline Prices Over Time (Scatter Plot)')
plt.xlabel('Date')
plt.ylabel('Price ($/gallon)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
