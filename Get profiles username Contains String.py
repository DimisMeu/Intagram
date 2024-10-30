# Need the following list from {Create following list with urls.py}

import pandas as pd

# Pick Profile Post setup
Prof = "dimism.eu"
StringForSearch ="8"

# Get the profile name and search string from the user
#Prof = input("Enter the profile name (for filename): ")
#StringForSearch = input("Enter the string to search for in usernames: ")

# Input and output filenames
input_file = f"{Prof}_following_list.csv"
output_file = f"{Prof}_profiles_contain_string_{StringForSearch}.csv"

# Load the list of Instagram URLs
try:
    df = pd.read_csv(input_file, header=None, names=['url'])
    
    # Extract usernames from URLs and filter based on the search string
    df['username'] = df['url'].apply(lambda x: x.split('/')[-2])
    filtered_df = df[df['username'].str.contains(StringForSearch, case=False, na=False)]

    # Reformat results to full URLs
    filtered_df['filtered_url'] = "https://www.instagram.com/" + filtered_df['username'] + "/"
    
    # Save filtered URLs to the output file without a header
    filtered_df.to_csv(output_file, index=False, columns=['filtered_url'], header=False)
    
    print(f"Filtered URLs saved to {output_file}")

except FileNotFoundError:
    print(f"Error: {input_file} not found.")