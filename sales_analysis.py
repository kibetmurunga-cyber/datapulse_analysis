
# IMPORTS
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# LOAD DATA
df = pd.read_csv('sales_data.csv')

# INSPECT THE DATA
print(f'Shape: {df.shape[0]} rows, {df.shape[1]} columns')

print('\nFirst five records:')
print(df.head())

print('\nColumn data types:')
print(df.dtypes)

print('\nStatistical summary:')
print(df.describe())

# COMPUTE WITH NUMPY
revenue = df['revenue'].tolist()

print(f'\nMean revenue  : GHS {np.mean(revenue):,.2f}')
print(f'Total revenue : GHS {np.sum(revenue):,.2f}')
print(f'Highest day   : GHS {np.max(revenue):,.2f}')

# VISUALISE WITH MATPLOTLIB
plt.figure(figsize=(10, 4))
plt.plot(df['date'], df['revenue'],
 color='steelblue', linewidth=2)

plt.title('Daily Revenue Trend')
plt.xlabel('Date')
plt.ylabel('Revenue (GHS)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
