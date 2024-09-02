# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('/mnt/data/wwe-champions-dataset.csv')

# Task 1: Average Reign Length per Belt Type (Bar Chart)
avg_reign_length = df.groupby('Belt')['Length'].mean().sort_values()

plt.figure(figsize=(10, 6))
sns.barplot(x=avg_reign_length.index, y=avg_reign_length.values, palette='viridis')
plt.title('Average Reign Length per Belt Type')
plt.xlabel('Belt Type')
plt.ylabel('Average Reign Length (Days)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('/mnt/data/average_reign_length_per_belt_type.png')
plt.show()

# Task 2: Top 5 Longest Reigning WWE Champions (Horizontal Bar Chart)
top_5_reigns = df.nlargest(5, 'Length')[['Name', 'Length']].set_index('Name')

plt.figure(figsize=(10, 6))
top_5_reigns['Length'].plot(kind='barh', color='orange')
plt.title('Top 5 Longest Reigning WWE Champions')
plt.xlabel('Reign Length (Days)')
plt.ylabel('Wrestler')
plt.tight_layout()
plt.savefig('/mnt/data/top_5_longest_reigning_champions.png')
plt.show()

# Task 3: The Fabulous Moolah's Contribution (Pie Chart)
moolah_total_days = df[df['Name'] == 'The Fabulous Moolah']['Length'].sum()
total_days = df['Length'].sum()
moolah_contribution = [moolah_total_days, total_days - moolah_total_days]

plt.figure(figsize=(8, 8))
plt.pie(moolah_contribution, labels=['The Fabulous Moolah', 'Others'], autopct='%1.1f%%', colors=['gold', 'lightblue'])
plt.title("The Fabulous Moolah's Contribution to Total Days")
plt.tight_layout()
plt.savefig('/mnt/data/moolah_contribution.png')
plt.show()

# Task 4: Analyzing The Fabulous Moolah's Impact on WWE Women's Championship (Bar Chart)
moolah_reigns = df[(df['Name'] == 'The Fabulous Moolah') & (df['Belt'] == "WWE Women's Championship")]['Length'].sum()
total_women_champ_days = df[df['Belt'] == "WWE Women's Championship"]['Length'].sum()

impact_data = [moolah_reigns, total_women_champ_days - moolah_reigns]

plt.figure(figsize=(8, 6))
sns.barplot(x=['Moolah', 'Others'], y=impact_data, palette='coolwarm')
plt.title("The Fabulous Moolah's Impact on WWE Women's Championship")
plt.ylabel('Total Days Held')
plt.tight_layout()
plt.savefig('/mnt/data/moolah_women_champ_impact.png')
plt.show()

# Task 5: Unique Champions vs Total Championship Reigns (Bar Chart)
champ_reign_counts = df['Name'].value_counts()

plt.figure(figsize=(10, 6))
champ_reign_counts.plot(kind='bar', color='green')
plt.title('Unique Champions vs Total Championship Reigns')
plt.xlabel('Wrestler')
plt.ylabel('Number of Reigns')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('/mnt/data/unique_champions_vs_total_reigns.png')
plt.show()

# Task 6: Top Five Wrestlers with Most Reigns (Horizontal Bar Chart)
top_5_reigns_count = champ_reign_counts.nlargest(5)

plt.figure(figsize=(10, 6))
top_5_reigns_count.plot(kind='barh', color='purple')
plt.title('Top 5 Wrestlers with Most Reigns')
plt.xlabel('Number of Reigns')
plt.ylabel('Wrestler')
plt.tight_layout()
plt.savefig('/mnt/data/top_5_most_reigns.png')
plt.show()

# Task 7: Distribution of WWE Champions and Their Reign Lengths (Histogram)
plt.figure(figsize=(10, 6))
sns.histplot(df['Length'], bins=30, kde=True, color='red')
plt.title('Distribution of WWE Champions and Their Reign Lengths')
plt.xlabel('Reign Length (Days)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('/mnt/data/reign_length_distribution.png')
plt.show()

# Task 8: Number of Reigns by Birth Decade (Bar Chart)
# Assume there's a 'BirthYear' column in the dataset
df['BirthDecade'] = (df['BirthYear'] // 10) * 10
reigns_by_birth_decade = df.groupby('BirthDecade')['Name'].count()

plt.figure(figsize=(10, 6))
reigns_by_birth_decade.plot(kind='bar', color='teal')
plt.title('Number of Reigns by Birth Decade')
plt.xlabel('Birth Decade')
plt.ylabel('Number of Reigns')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('/mnt/data/reigns_by_birth_decade.png')
plt.show()

# Task 9: Number of WWE Champs per Belt Type (Bar Chart)
champs_per_belt = df.groupby('Belt')['Name'].nunique().sort_values()

plt.figure(figsize=(10, 6))
sns.barplot(x=champs_per_belt.index, y=champs_per_belt.values, palette='magma')
plt.title('Number of WWE Champs per Belt Type')
plt.xlabel('Belt Type')
plt.ylabel('Number of Unique Champs')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('/mnt/data/champs_per_belt.png')
plt.show()

# Task 10: Distribution of Reigns by Belt Type (Pie Chart)
reigns_per_belt = df['Belt'].value_counts()

plt.figure(figsize=(8, 8))
reigns_per_belt.plot(kind='pie', autopct='%1.1f%%', colors=sns.color_palette('pastel'))
plt.title('Distribution of Reigns by Belt Type')
plt.ylabel('')
plt.tight_layout()
plt.savefig('/mnt/data/reigns_distribution_by_belt.png')
plt.show()

# Task 11: Most Days as Champion by Belt (Grouped Bar Chart)
most_days_per_belt = df.groupby(['Belt', 'Name'])['Length'].sum().unstack().fillna(0)
most_days_per_belt_top5 = most_days_per_belt.nlargest(5, most_days_per_belt.sum(axis=1).idxmax())

most_days_per_belt_top5.T.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='Paired')
plt.title('Most Days as Champion by Belt')
plt.xlabel('Belt')
plt.ylabel('Total Days')
plt.tight_layout()
plt.savefig('/mnt/data/most_days_as_champ_by_belt.png')
plt.show()

# Task 12: Total Days Held by Rest of Wrestlers
top_5_wrestlers = champ_reign_counts.nlargest(5).index
top_5_days = df[df['Name'].isin(top_5_wrestlers)]['Length'].sum()
total_days_all = df['Length'].sum()
rest_days = total_days_all - top_5_days

rest_contribution = [top_5_days, rest_days]

plt.figure(figsize=(8, 8))
plt.pie(rest_contribution, labels=['Top 5 Wrestlers', 'Rest'], autopct='%1.1f%%', colors=['gold', 'lightgreen'])
plt.title('Total Days Held by Top 5 Wrestlers vs Rest')
plt.tight_layout()
plt.savefig('/mnt/data/total_days_held_by_rest.png')
plt.show()

# Task 13: Comparison of Top 5 Contributors vs Rest of Wrestlers in WWE Championship Total Days
plt.figure(figsize=(8, 8))
sns.barplot(x=['Top 5 Wrestlers', 'Rest of Wrestlers'], y=rest_contribution, palette='dark')
plt.title('Comparison of Top 5 Contributors vs Rest in WWE Championship Total Days')
plt.ylabel('Total Days Held')
plt.tight_layout()
plt.savefig('/mnt/data/comparison_top_5_vs_rest.png')
plt.show()

