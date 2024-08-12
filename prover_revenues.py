import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np

# Function to format the y-axis labels
def human_format(num, pos=None):
    if num >= 1e12:
        return f'{num*1e-12:.1f}T'
    elif num >= 1e9:
        return f'{num*1e-9:.1f}B'
    elif num >= 1e6:
        return f'{num*1e-6:.1f}M'
    else:
        return f'{num:.1f}'

# Parameters
average_transaction_value = 100  # in dollars
annual_transactions = 100_000_000_000  # 100 billion transactions
prover_charge_percentage = 0.001  # 0.1%
annual_growth_rate = 0.1  # 50% growth per year
years = 10  # Project over 10 years

# BTC Miners
mining_years = [2018, 2019, 2020, 2021, 2022, 2023]
mining_revenue = [5.937e+09, 11.248e+09, 13.5985e+09, 11.4617e+09, 9.8725e+09, 6.5673e+09]

# Apply logarithmic growth to BTC mining revenue
for i in range(1, years + 1):
    mining_revenue.append(mining_revenue[3] * np.log(i + 1) * 0.9)

# Global payment revenue
payment_years = [2018, 2019, 2020, 2021, 2022, 2023]
payment_revenue = [1.7e+12, 1.75e+12, 1.8e+12, 2.2e+12, 2.22e+12, 2.24e+12]

# Apply linear growth to global payment revenue
for i in range(1, years + 1):
    payment_revenue.append(payment_revenue[-1] + 0.02e+12)

# Calculate projected revenues and transaction volumes for each year
projected_revenues = []
transaction_volumes = []
revenue = average_transaction_value * annual_transactions * prover_charge_percentage
transactions = annual_transactions
for year in range(years):
    if year != 0:
        revenue *= (1 + annual_growth_rate)
        transactions *= (1 + annual_growth_rate)
    projected_revenues.append(revenue)
    transaction_volumes.append(transactions)

# Apply exponential growth to projected prover revenues
projected_revenues = [revenue * (1 + annual_growth_rate) ** i for i in range(years)]

# Extend the years for projected revenues
start_year = max(mining_years + payment_years) + 1
projected_years = list(range(start_year, start_year + years))

# Set the font family to Tahoma, Arial, and Georgia
plt.rcParams['font.family'] = ['TEG']

# Visualization
fig, ax1 = plt.subplots(figsize=(10, 6))

# Set background color
fig.patch.set_facecolor('#F2F9F9')
ax1.set_facecolor('#F2F9F9')

# Set log scale for y-axis
ax1.set_yscale('log')

# Plot BTC mining revenue
ax1.plot(mining_years + list(range(2024, 2024 + years)), mining_revenue, marker='s', color='r', label='BTC Mining Revenue')

# Plot global payment revenue
ax1.plot(payment_years + list(range(2024, 2024 + years)), payment_revenue, marker='d', color='m', label='Global Payment Revenue')

# Plot projected prover revenues
ax1.plot(projected_years, projected_revenues, marker='o', color='b', label='Projected Prover Revenue')

# Titles and labels
ax1.set_xlabel('Years')
ax1.set_ylabel('Revenue ($)')
ax1.yaxis.set_major_formatter(FuncFormatter(human_format))
plt.title('BTC Mining Revenue, Global Payment Revenue, and Projected Prover Revenue Over Years')
ax1.set_xticks(range(min(mining_years), max(projected_years) + 1))
ax1.grid(True, axis='both', color='gray', alpha=0.7)

# Increase y-axis limit to make space for the legend
ax1.set_ylim(1e9, 1e14)

# Show legends
fig.tight_layout()
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))

plt.savefig('revenue.png', dpi=400)
plt.show()
