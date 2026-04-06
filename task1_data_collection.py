import os
import requests
import json
import time
from datetime import datetime

# Fetch Data from API

# Make the API calls, fetching story ID's using the first API link given and storing it in the ids.
API_ID = "https://hacker-news.firebaseio.com/v0/topstories.json"
headers = {"User-Agent": "TrendPulse/1.0"}

try:
    response = requests.get(API_ID, headers=headers)

    print("Status code: ", response.status_code)

    if response.status_code == 200:
        ids = response.json()
        print(len(ids))
    else:
        print(f"Error: Received status code {response.status_code}")
except requests.exceptions.RequestException as e:
    print("Request failed: ", e)

# Fetch the stories according to the story id, with sleep time 2 in between the story data fetching for each id.
stories = []

for id in ids:
    try:
        url = f"https://hacker-news.firebaseio.com/v0/item/{id}.json"
        response = requests.get(url, headers=headers)

        if response.status_code==200:
            story = response.json()
            stories.append(story)
        else:
            print(f"Error: Received status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print("Request failed: ", e)

time.sleep(2)
print("stories data length: ", len(stories))

# Fetch the 7 data fields in the json format based on category upto 125 dataset with 25 each category.
stories_data=[]

category_count = {
    "technology":0,
    "worldnews":0,
    "sports":0,
    "science":0,
    "entertainment":0
}
max_per_cat = 25

def select_category(title):
    title = title.lower()

    if any(word in title for word in ["ai", "software", "tech", "code", "computer", "data", 
                                      "cloud", "api", "gpu", "llm"]):
        return "technology"
    elif any(word in title for word in ["war", "government", "country", "president", "election", 
                                        "climate", "attack", "global"]):
        return "worldnews"
    elif any(word in title for word in ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"]):
        return "sports"
    elif any(word in title for word in ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"]):
        return "science"
    elif any(word in title for word in ["movie", "film", "music", "Netflix", "game", "book", "show", "award", "streaming"]):
        return "entertainment"
    
for story in stories:
    title = story.get("title", "")
    category = select_category(title)
    
    if category is None:
        continue
    if category_count[category] >= max_per_cat:
        continue
    else:
        stories_data.append({
            "post_id": story.get("id"),
            "title": title,
            "category": category,
            "score": story.get("score",0),
            "num_comments": story.get("descendants",0),
            "author": story.get("by"),
            "collected_at": datetime.now().isoformat()
        })
        category_count[category] += 1

    if len(stories_data) >= 125:
        break

# Save the data into json file 
os.makedirs("data", exist_ok=True)
file_name = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

with open(file_name, "w") as f:
    json.dump(stories_data, f, indent=4)

print("\nTotal stories collected:", len(stories_data))
print("Saved to:", file_name)
        
        