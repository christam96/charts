import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter
from matplotlib.patches import Patch

# Data
systems = ['Visa', 'Mastercard', 'Solana', 'Ethereum', 'Bitcoin']
annual_transactions = [
    268e9,  # Visa
    175e9,  # Mastercard
    [1.10376e11, 2.05e12],  # Solana and Solana (capacity)
    [11e9, 3.15e12],  # Ethereum and Ethereum (sharding)
    220e6  # Bitcoin
]
TPS = [8498, 5549, 3500, 65000, 300, 100000, 7]  # Transactions Per Second

# Plotting
x = np.arange(len(systems))
width = 0.5  # the width of the bars

# Define colors for each system
# colors = ['#1f77b4', '#FFB74D', '#66BB6A', '#4B9CD3', '#ff7f0e']  # Blue, Orange, Light Blue, Red, Light Orange
colors = ['#5a9bd4', '#FFD27F', '#99D3A6', '#7FBCE6', '#ff9f4e']  # Lighter Blue, Lighter Orange, Lighter Light Blue, Lighter Red, Lighter Light Orange

# Define opacity for specific bars
opacities = [1.0, 1.0, 1.0, 1.0, 1.0]
# opacities = [0.8, 0.8, 0.8, 0.8, 0.8]

# Function to format the y-axis labels and bar labels
def human_format(num, pos=None):
    if num >= 1e12:
        return f'{num*1e-12:.1f}T'
    elif num >= 1e9:
        return f'{num*1e-9:.1f}B'
    elif num >= 1e6:
        return f'{num*1e-6:.1f}M'
    else:
        return f'{num:.1f}'

# Set the font family to Tahoma, Arial, and Georgia
plt.rcParams['font.family'] = ['TEG']

# Create the first figure for annual transactions
# fig1, ax1 = plt.subplots(figsize=10, 6))
fig1, ax1 = plt.subplots(figsize=(10, 6))

# Set background color
fig1.patch.set_facecolor('#F2F9F9')
ax1.set_facecolor('#F2F9F9')

# Create bars for annual transactions
bars1 = []
for i, (system, transactions) in enumerate(zip(systems, annual_transactions)):
    if isinstance(transactions, list):
        bottom = 0
        for j, part in enumerate(transactions):
            # Set opacity to 0.5 for the top half of the bar
            alpha = 0.5 if j == 1 else opacities[i]
            bar = ax1.bar(x[i], part, width, color=colors[i], edgecolor='black', bottom=bottom, alpha=alpha)
            bottom += part
            bars1.append(bar)
            # Display the value on top of each partition
            ax1.text(x[i], bottom, human_format(part), ha='center', va='bottom')
    else:
        bar = ax1.bar(x[i], transactions, width, color=colors[i], edgecolor='black', alpha=opacities[i])
        bars1.append(bar)
        # Display the value on top of each bar
        ax1.text(x[i], transactions, human_format(transactions), ha='center', va='bottom')

# Labels and titles for the first plot
ax1.set_xlabel('Payment Network')
ax1.set_ylabel('Annual Transactions')
ax1.set_title('2023 Annual Transactions')
ax1.set_xticks(x)
ax1.set_xticklabels(systems, rotation=15)
ax1.grid(True, linestyle=':', alpha=0.4)

# Set log scale for y-axis
ax1.set_yscale('log')

# Apply human-readable format to y-axis labels
ax1.yaxis.set_major_formatter(FuncFormatter(human_format))

# Create a custom legend with half green and half blue boxes
# Create custom legend
legend_elements = [
    # Patch(facecolor='#66BB6A', edgecolor='black', alpha=1.0, label='SOL Actual Transactions'),
    Patch(facecolor='#66BB6A', edgecolor='black', alpha=0.5, label='SOL Capacity'),
    # Patch(facecolor='#4B9CD3', edgecolor='black', alpha=1.0, label='ETH Actual Transactions'),
    Patch(facecolor='#4B9CD3', edgecolor='black', alpha=0.5, label='ETH Capacity w/ Sharding')
]
ax1.legend(handles=legend_elements, loc='upper left')

plt.tight_layout()
plt.savefig('tps.png', dpi=400)

plt.show()
