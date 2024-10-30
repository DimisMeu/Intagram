# Scraper https://chromewebstore.google.com/detail/ig-exporter-scraper-expor/akbfineiddmgpdlkalpcfblholabkeen
# Need the following list from Get Non-followers (v4 New Scraper).py

import csv

# Pick profile 
# DimisM = "dimism.eu"
# ZZR = "zzr1400.gr"
Prof = "dimism.eu"

# Input and output file names
input_file = Prof + '_' + 'following.csv'
output_file = Prof + '_' + 'following_list.csv'

# Read the input CSV file and create the output CSV file
with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile, delimiter=';')
    writer = csv.writer(outfile)
    
    # Skip the header
    next(reader)
    
    # Write the header for the output file
    # writer.writerow(['profile_url'])
    
    # Process each row
    for row in reader:
        username = row[6]  # Assuming the username is the 7th column (index 6)
        profile_url = f"https://www.instagram.com/{username}/"
        writer.writerow([profile_url])  # Write the profile URL to the output file

print(f"Profile URLs have been written to {output_file}.")
