#Need the following list from Create following list with urls.py

import requests
from bs4 import BeautifulSoup
import csv
import time  # Import time module for sleep function

# Helper function to convert strings like '15K', '5,325' to integers
def parse_number(value):
    if 'K' in value:
        # Remove 'K' and multiply by 1000
        return int(float(value.replace('K', '')) * 1000)
    elif 'M' in value:
        # Handle millions (if it ever happens)
        return int(float(value.replace('M', '')) * 1000000)
    else:
        # Remove commas if any and return as int
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
                    "posts": posts  # Already an integer due to parse_number
                }
            else:
                return {"error": "Meta tag not found"}
        else:
            return {"error": f"Error: {response.status_code}"}

    except Exception as e:
        return {"error": str(e)}

# Pick profile 
Prof = "dimism.eu"
NumberOfPosts = 0

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
            if profile_info['posts'] == NumberOfPosts:
                writer.writerow([profile_url])
                print(f"Profile with under {NumberOfPosts} posts: {profile_url}")
        
        # Delay in seconds
        time.sleep(0.3)

print(f"Profile URLs with under {NumberOfPosts} posts have been written to {output_file}.")
