import pandas as pd
import numpy as np
import json

# Load and explore the data

df = pd.read_csv("./data/trend_clean.csv")

# Shape of the dataframe
print("Loaded data: ", df.shape, "\n")

# First 5 rows
print("First 5 rows:\n", df.head(5), "\n")

# Average of Score and num_comments column from dataframe
print("Average Score: ", df['score'].mean())
print("Average Comments: ", df['num_comments'].mean(), "\n")

# Basic Analysis with NumPy

print("--- NumPy Stats ---")
# What is the mean, median, and standard deviation of score?
mean = df['score'].mean()
median = df['score'].median()
std = df['score'].std()
print(f"Mean score   : {mean}")
print(f"Median score : {median}")
print(f"Std deviation: {std}")
#print(df['score'].aggregate(['mean', 'median', 'std']))

# What is the highest score and lowest score?
max = df['score'].max()
min = df['score'].min()
print(f"Max score    : {max}")
print(f"Min score    : {min}\n")
#print(df['score'].aggregate(['max', 'min']))

# Which category has the most stories?
category_count = df['category'].value_counts()
print(f"Most stories in: {category_count.idxmax()} ({category_count.max()} stories)\n")
#print(category_count.idxmax())

# Which story has the most comments? Print its title and comment count.
row = df.loc[df['num_comments'].idxmax()]
print(f"""Most commented story: "{row['title']}" — {row['num_comments']} comments\n""")


# Add New Columns 

# Adding engagement column to the dataframe
df['engagement'] = (df['num_comments'] / (df['score'] + 1))

# Adding is_popular column
df['is_popular'] = df['score'] > df['score'].mean()


# Save the Result

df.to_csv("./data/trend_analysed.csv", index=False)
print("Saved to data/trends_analysed.csv")


#print(df.head(5))