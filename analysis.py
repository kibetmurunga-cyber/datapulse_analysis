
# analysis.py — DataPulse starter analysis

# Imports at the top — always
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# CREATE SAMPLE DATA
data = {
    'week': ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5'],
    'sales': [12400, 15800, 13200, 18900, 21500],
    'returns': [320, 410, 290, 500, 380],
}

df = pd.DataFrame(data)

# INSPECT
print('Shape:', df.shape)
print(df.head())
print(df.dtypes)

# COMPUTE
sales = df['sales'].tolist()

print(f'Mean sales  : GHS {np.mean(sales):,.0f}')
print(f'Total sales : GHS {np.sum(sales):,.0f}')
print(f'Best week   : GHS {np.max(sales):,.0f}')
print(f'Worst week  : GHS {np.min(sales):,.0f}')

# VISUALISE
plt.figure(figsize=(8, 4))
plt.bar(df['week'], df['sales'], color='steelblue', edgecolor='white')
plt.title('DataPulse — Weekly Sales Overview')
plt.ylabel('Sales (GHS)')
plt.tight_layout()
plt.show()
