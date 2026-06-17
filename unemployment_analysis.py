import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Unemployment in India.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# Basic Information
print("Dataset Shape:", df.shape)
print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistics:")
print(df.describe())

# -------------------------------
# Average Unemployment by Region
# -------------------------------
plt.figure(figsize=(12,6))

region_unemployment = df.groupby('Region')['Estimated Unemployment Rate (%)'].mean()
region_unemployment.sort_values().plot(kind='bar')

plt.title("Average Unemployment Rate by Region")
plt.ylabel("Unemployment Rate (%)")
plt.xlabel("Region")
plt.xticks(rotation=90)

plt.tight_layout()
plt.show()

# -------------------------------
# Monthly Trend
# -------------------------------
monthly = df.groupby('Date')['Estimated Unemployment Rate (%)'].mean()

plt.figure(figsize=(12,6))
monthly.plot()

plt.title("Unemployment Rate Trend Over Time")
plt.ylabel("Unemployment Rate (%)")
plt.xlabel("Date")

plt.grid(True)
plt.tight_layout()
plt.show()

# -------------------------------
# Covid-19 Impact
# -------------------------------
covid = df[df['Date'] >= '2020-03-01']

plt.figure(figsize=(12,6))

sns.lineplot(
    data=covid,
    x='Date',
    y='Estimated Unemployment Rate (%)'
)

plt.title("Impact of Covid-19 on Unemployment")
plt.ylabel("Unemployment Rate (%)")

plt.tight_layout()
plt.show()

# -------------------------------
# Rural vs Urban
# -------------------------------
plt.figure(figsize=(8,5))

sns.boxplot(
    data=df,
    x='Area',
    y='Estimated Unemployment Rate (%)'
)

plt.title("Rural vs Urban Unemployment")
plt.tight_layout()
plt.show()

# -------------------------------
# Heatmap
# -------------------------------
pivot = df.pivot_table(
    values='Estimated Unemployment Rate (%)',
    index='Region',
    aggfunc='mean'
)

plt.figure(figsize=(8,10))
sns.heatmap(pivot, annot=True, cmap='YlOrRd')

plt.title("Region-wise Unemployment Heatmap")
plt.show()

print("\nAnalysis Completed Successfully!")