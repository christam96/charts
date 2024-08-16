'''
Framework: 
- Global payment revenues are expected to grow by 7% annually to 3.2T by 2027 (McKinsey, 2023)
- Global real-time payments climbed to a new record high in 2023, reaching 266.2B transactions (ACI Worldwide, 2023)
- Global real-time payments are expected to grow by 16.7% annually to 575.1B transactions by 2028 (ACI Worldwide, 2023)
'''

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Revenue Growth Function
def revenue_growth(volume, cagr, years):
    revenue = [volume]
    for i in range(1, years):
        revenue.append(revenue[i - 1] * (1 + cagr))
    return revenue

# Formatter function to convert large numbers to human-readable format
def trillions(x, pos):
    'The two args are the value and tick position'
    return '%1.1fT' % (x * 1e-12)

# Projected Years
years = [2024, 2025, 2026, 2027, 2028, 2029, 2030]

# Global Payment Revenue (GPR)
gpr_2023_tx_volume = 2.4e+12 # 2.4T transactions
gpr_cagr = 0.07  # 7% CAGR
gpr_projections = revenue_growth(gpr_2023_tx_volume, gpr_cagr, len(years))

# Real-Time Payments (RTP)
rtp_2023_tx_volume = 266.2e+09 # 266.2B transactions
rtp_cagr = 0.167  # 16.7% CAGR
rtp_projections_0 = revenue_growth(rtp_2023_tx_volume, rtp_cagr, len(years))

# Scenario 1: RTP growth of 30%
rtp_cagr_scenario1 = 0.30  # 30% CAGR
rtp_projections_1 = revenue_growth(rtp_2023_tx_volume, rtp_cagr_scenario1, len(years))

# Scenario 2: RTP growth of 45%
rtp_cagr_scenario2 = 0.45  # 45% CAGR
rtp_projections_2 = revenue_growth(rtp_2023_tx_volume, rtp_cagr_scenario2, len(years))

# Plotting the projections
fig, ax = plt.subplots(figsize=(12, 8))

# # Set background color
# fig.patch.set_facecolor('#F2F9F9')
# ax.set_facecolor('#F2F9F9')

# Plot GPR
ax.plot(years, gpr_projections, label='Global Payments', marker='o', color='blue', linewidth=2)

# Plot RTP scenarios
ax.plot(years, rtp_projections_2, label='Real-Time Payments (45% CAGR)', marker='o', color='red', linewidth=2)
ax.plot(years, rtp_projections_1, label='Real-Time Payments (30% CAGR)', marker='o', color='orange', linewidth=2)
ax.plot(years, rtp_projections_0, label='Real-Time Payments (16% CAGR)', marker='o', color='green', linewidth=2)

# Fill between RTP scenarios
ax.fill_between(years, rtp_projections_0, rtp_projections_2, color='gray', alpha=0.2)

# Adding labels and title
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Transaction Volumes', fontsize=14)
ax.set_title('Demand for Global and Real-Time Payments', fontsize=16)
ax.legend(loc='upper left', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.7)

# Format the y-axis to human-readable format
formatter = FuncFormatter(trillions)
ax.yaxis.set_major_formatter(formatter)

# Improve font and style
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()

# Save the figure
plt.savefig('market_opportunity.png', dpi=400)

# Display the plot
plt.show()
