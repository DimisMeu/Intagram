# Need the following list from {Create following list with urls.py}

import requests
from bs4 import BeautifulSoup
import csv
import time

# Profile and post limit
Prof = "dimism.eu"
NumberOfPosts = 13
input_file = f"{Prof}_following_list.csv"
output_file = f"{Prof}_profiles_under_{NumberOfPosts}_posts.csv"

# Helper function to convert strings like '15K', '5,325' to integers
def parse_number(value):
    if 'K' in value:
        return int(float(value.replace('K', '')) * 1000)
    elif 'M' in value:
        return int(float(value.replace('M', '')) * 1000000)
    else:
        return int(value.replace(',', ''))

# Function to scrape the number of posts, followers, and following from a public Instagram profile
def get_instagram_profile_info(profile_url):
    try:
        response = requests.get(profile_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            meta_tag = soup.find("meta", property="og:description")
            
            if meta_tag:
                content = meta_tag["content"]
                parts = content.split(", ")
                followers = parse_number(parts[0].split(" ")[0])
                following = parse_number(parts[1].split(" ")[0])
                posts = parse_number(parts[2].split(" ")[0])
                
                return {
                    "followers": followers,
                    "following": following,
                    "posts": posts
                }
            else:
                return {"error": "Meta tag not found"}
        else:
            return {"error": f"Error: {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}

# Read input CSV file and create the output CSV file
with open(input_file, 'r', encoding='utf-8') as infile:
    for row in infile:
        profile_url = row.strip()
        profile_info = get_instagram_profile_info(profile_url)
        
        if 'error' in profile_info:
            print(f"Error fetching data for {profile_url}: {profile_info['error']}")
        else:
            # Only write to file if posts are under the specified limit
            if profile_info['posts'] < NumberOfPosts:
                # Open output file in append mode and write immediately
                with open(output_file, 'a', newline='', encoding='utf-8') as outfile:
                    writer = csv.writer(outfile)
                    writer.writerow([profile_url])
                    print(f"Profile with under {NumberOfPosts} posts: {profile_url}")
        
        time.sleep(0.3)

print(f"Profiles with under {NumberOfPosts} posts have been written to {output_file} as they were found.")
