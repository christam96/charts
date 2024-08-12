import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Load the data from the CSV file
df = pd.read_csv('rwa.csv')

# Drop the first and third columns
df = df.drop(df.columns[[0, 2]], axis=1)

# Print the first few rows of the DataFrame to see the data
print("DataFrame preview:")
print(df.head())

# Print the names of the columns after dropping
print("Column names after dropping:", df.columns.tolist())

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Group the data by 'Date'
grouped_data = df.groupby('Date').sum(numeric_only=True)

# Sort the categories by their final value and select the top 15
top_15_categories = grouped_data.iloc[-1].sort_values(ascending=False).head(15).index

# Filter the data to include only the top 15 categories
filtered_data_top_15 = grouped_data[top_15_categories]

# Print the amounts to double-check the results
print("Amounts for top 15 categories:")
print(filtered_data_top_15)

# Function to format the y-axis labels
def human_format(num, pos):
    if num >= 1e9:
        return f'{num*1e-9:.1f}B'
    elif num >= 1e6:
        return f'{num*1e-6:.1f}M'
    elif num >= 1e3:
        return f'{num*1e-3:.1f}K'
    else:
        return f'{num:.0f}'

# Set the font family to Tahoma, Arial, and Georgia
plt.rcParams['font.family'] = ['TEG']

# Plot the data using a stacked area plot
fig, ax = plt.subplots(figsize=(10, 6))

# Set background color
fig.patch.set_facecolor('#F2F9F9')
ax.set_facecolor('#F2F9F9')

filtered_data_top_15.plot.area(ax=ax, alpha=0.5)
ax.set_title('Global Stablecoin Addresses')
ax.set_xlabel('Date')
ax.set_ylabel('Number of Addresses')
ax.legend(title='Categories')
ax.grid(True)

# Apply the human-readable format to the y-axis
ax.yaxis.set_major_formatter(FuncFormatter(human_format))

plt.tight_layout()
plt.savefig('rwa.png', dpi=400)

plt.show()
