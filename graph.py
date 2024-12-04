import pandas as pd
import matplotlib.pyplot as plt
import mplcursors


data_path = "scraping.csv"  # Replace with the actual path to your CSV file

# Read the CSV data using pandas
df = pd.read_csv(data_path)
# Assuming your data is in a DataFrame named 'df' with columns 'x_values' and 'y_values'

# Create the bar plot


 # Replace with the actual path to your CSV file

# Read the CSV data using pandas

# Check for NaN values and fill or drop them as appropriate
df['Name'] = df['Name'].fillna('Unknown')  # Replace NaN with a placeholder in 'Name' column
df['Price'] = df['Price'].fillna(0)  # Replace NaN with 0 in 'Price' column

# Convert columns to appropriate types
df['Name'] = df['Name'].astype(str)
df['Price'] = pd.to_numeric(df['Price'], errors='coerce').fillna(0)  # Convert 'Price' to numeric, replacing errors with 0



# Create the bar plot
plt.figure(figsize=(12, 6))  # Adjust figure size as needed
plt.bar(df['Name'], df['Price'])

# Customize the plot
plt.xlabel('Name Label')
plt.ylabel('Price Label')
plt.title('Clearer Bar Plot')

# Rotate x-axis labels for better readability

# plt.xticks(ticks=range(0, len(df['Name']), 10), labels=df['Name'][::10], rotation=45, ha='right')
# plt.xticks(rotation=45, ha='right')
# plt.tight_layout()

# cursor = mplcursors.cursor(bars)
# cursor.connect("add", lambda sel: sel.annotation.set_text(df['Name'][sel.target.index]))
# Adjust spacing between x-axis labels

plt.show()
