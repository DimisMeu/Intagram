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
                    "posts": posts
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

# Input and output file names
input_file = Prof + '_' + 'following_list.csv'
output_file = Prof + '_' + 'profile_info.csv'

# Read the input CSV file and create the output CSV file
with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    # Write the header for the output file
    writer.writerow(['profile_url', 'posts', 'following', 'followers'])
    
    # Process each row
    for row in reader:
        profile_url = row[0]  # Assuming the profile_url is in the first column
        profile_info = get_instagram_profile_info(profile_url)
        
        if 'error' in profile_info:
            print(f"Error fetching data for {profile_url}: {profile_info['error']}")
            writer.writerow([profile_url, None, None, None])
        else:
            writer.writerow([profile_url, profile_info['posts'], profile_info['following'], profile_info['followers']])
            print(f"Fetched data for {profile_url}: Posts: {profile_info['posts']}, Following: {profile_info['following']}, Followers: {profile_info['followers']}")
        
        # Delay of 0.3 seconds
        time.sleep(1.5)

print(f"Profile information has been written to {output_file}.")
