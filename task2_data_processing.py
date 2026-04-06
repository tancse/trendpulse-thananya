import json
import pandas as pd

# Loading JSON file using open function and json.load() to convert json file into python object.
filename = "data/trends_20260406.json"
with open("./data/trends_20260406.json", "r") as f:
    data = json.load(f)

# Loaded JSON file data into a pandas dataframe.
df = pd.DataFrame(data)

#print("Total no of rows loaded: ",len(df)) # No of rows loaded from the json file into dataframe.
print(f"Loaded {len(df)} stories from {filename}\n")


# Clean the data

# Handling duplicates
# print("shape of original dataset: ", df.shape)
# print("No of duplicated rows: ",df.duplicated(subset=['post_id']).sum())
df1 = df.drop_duplicates(subset=['post_id'], keep='first')
print(f"After removing duplicates: {len(df1)}")

# Handling missing values
# print("No of missing values:\n", df1.isnull().sum())

df1 = df1.dropna(subset=['post_id', 'title', 'score'])
print(f"After removing nulls: {len(df1)}")

# Handling Data Types of columns
# print (df1.dtypes) # the data types of score and num_comments where integers.

# Handling data with low quality(score less than 5)
df1 = df1[df1['score']>5]
print(f"After removing low scores: {len(df1)}\n")

# Removing extra whitespace from the title in the dataframe
df1['title'] = df1['title'].str.strip()

# Save as CSV

df1.to_csv("./data/trend_clean.csv")
print(f"Saved {len(df1)} rows to data/trends_clean.csv\n")


category_count = df1["category"].value_counts()

print ("Stories per category: ")
print(category_count)





# print(type(data))
# print(data[0])
# print(type(data[0]))
# print(df.head(4))
