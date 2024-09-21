#Need the following list from Create following list with urls.py

import requests
from bs4 import BeautifulSoup
import csv
import time  # Import time module for sleep function

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
                
                followers = parts[0].split(" ")[0]
                following = parts[1].split(" ")[0]
                posts = parts[2].split(" ")[0]
                
                return {
                    "followers": followers,
                    "following": following,
                    "posts": int(posts)  # Convert posts to an integer for comparison
                }
            else:
                return {"error": "Meta tag not found"}
        else:
            return {"error": f"Error: {response.status_code}"}

    except Exception as e:
        return {"error": str(e)}
    
#Pick profile 
# DimisM = "dimism.eu"
# ZZR = "zzr1400.gr" 
Prof = "dimism.eu"
NumberOfPosts = 15

# Input and output file names
input_file = f"{Prof}_following_list.csv"
output_file = f"{Prof}_profiles_under_{NumberOfPosts}_posts.csv"

# Read the input CSV file and create the output CSV file
with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    
    # Process each row
    for row in infile:
        profile_url = row.strip()  # Read and strip newline characters
        profile_info = get_instagram_profile_info(profile_url)
        
        if 'error' in profile_info:
            print(f"Error fetching data for {profile_url}: {profile_info['error']}")
        else:
            # Only write the full URL if posts are under NumberOfPosts Var
            if profile_info['posts'] < NumberOfPosts:
                writer.writerow([profile_url])
                print(f"Profile with under {NumberOfPosts} posts: {profile_url}")
        
        # Delay of 0.3 seconds
        time.sleep(0.4)

print(f"Profile URLs with under {NumberOfPosts} posts have been written to {output_file}.")
