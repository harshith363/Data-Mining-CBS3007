import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = r'C:\Users\harsh\OneDrive\Documents\VIT\FALLSEM 24-25\CBS3007\DA1 main\oil-prices.csv'  # Replace with your actual file path
data = pd.read_csv(file_path)

# Strip any leading or trailing spaces from column names
data.columns = data.columns.str.strip()

# Convert the 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'], format='%d-%m-%Y')

# Set the 'Date' column as the index
data.set_index('Date', inplace=True)

# Plot the data
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Motor Gasoline Price ($/gallon) Real'], marker='o', linestyle='-', color='b')
plt.title('Motor Gasoline Prices Over 25 Years')
plt.xlabel('Date')
plt.ylabel('Price ($/gallon)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()
