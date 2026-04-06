import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("./data/trend_analysed.csv")

os.makedirs("outputs", exist_ok=True)

# Chart 1: Top 10 Stories by Score 
rows = df.sort_values(by="score", ascending=False).head(10)
rows["short_title"] = rows["title"].apply(
    lambda x: x[:50] + "..." if len(x) > 50 else x
)
#print(rows)
plt.figure()
plt.barh(rows["short_title"], rows["score"])

plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Most Commented Stories")

plt.tight_layout()
plt.savefig("outputs/chart1_top_stories.png")
plt.show()

# Chart 2: Stories per Category 
category_count = df['category'].value_counts()
colors = ["red", "blue", "green", "orange", "purple"]

plt.figure()
plt.bar(category_count.index, category_count.values, color=colors)

plt.xlabel("Category")
plt.ylabel("Count")
plt.title("Stories per Category")

plt.tight_layout()
plt.savefig("outputs/chart2_categories.png")
plt.show()

# Chart 3: Score vs Comments

sns.scatterplot(data=df,
               x="score",
               y="num_comments",
               hue="is_popular",
               alpha=0.7)

plt.xlabel("Score")
plt.ylabel("Num of Comments")
plt.title("Score VS Comments")

plt.tight_layout()
plt.legend()
plt.savefig("outputs/chart3_scatter.png")
plt.show()

# Bonus -- Dashboard Combining all three plots

fig, axes = plt.subplots(1,3,figsize=(12, 5))

axes[0].barh(rows["short_title"], rows["score"])
axes[0].set_xlabel("Score")
axes[0].set_ylabel("Story Title")
axes[0].set_title("Top 10 Most Commented Stories")

axes[1].bar(category_count.index, category_count.values, color=colors)
axes[1].set_xlabel("Category")
axes[1].set_ylabel("Count")
axes[1].set_title("Stories per Category")

code = df['is_popular'].astype("category").cat.codes
axes[2].scatter(df['score'],
                df['num_comments'],
                c=code)
axes[2].set_xlabel("Score")
axes[2].set_ylabel("No of Comments")
axes[2].set_title("Score VS Comments")
axes[2].legend()

plt.title("TrendPulse Dashboard")
plt.tight_layout()
plt.savefig("outputs/dashboard.png")
plt.show()