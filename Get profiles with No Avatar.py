#Scraper https://chromewebstore.google.com/detail/ig-exporter-scraper-expor/akbfineiddmgpdlkalpcfblholabkeen
#Need the following list from Get Non-followers (v4 New Scraper).py

import csv #to get csv to text
import os #to remove files
from openpyxl import Workbook #to excel

def remove_double_quotes(input_file, output_file):
    with open(input_file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        data = [row for row in reader]

    modified_data = [[value.replace('"', '') for value in row] for row in data]

    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(modified_data)

    #print("Double quotes removed successfully!")

avatar = "44884218_345707102882519_2446069589734326272_n.jpg"
#Pick profile 
# DimisM = "dimism.eu"
# ZZR = "zzr1400.gr"
Prof = "dimism.eu"

#FOLLOWINGS
followingCSV = Prof + '_' + 'following.csv'
followingCSV_withoutQuotes = 'followinglist.csv'
remove_double_quotes(followingCSV, followingCSV_withoutQuotes)

#remove 1st splitlines
with open("followinglist.csv","r",encoding="utf-8") as arxikofollowing:
    data = arxikofollowing.read().splitlines(True)
with open("followinglist1.csv", "w",encoding="utf-8") as telikofollowing:
    telikofollowing.writelines(data[1:])
#Accessing a csv file epistoles1 is like epistoles without the 1st line
followinglist = open("followinglist1.csv","r",encoding="utf-8")

for line in followinglist:
    # Split the line into an array called "fields" using the ";" as a separator
    fields = line.split(";")
    
    # Extract the data
    followed_by_viewer = fields[0]
    fullName = fields[1]
    id = fields[2]
    isVerified = fields[3]
    profile_pic_url = fields[4]
    requested_by_viewer = fields[5]
    userName = fields[6]

    # Check if the profile_pic_url contains the specified substring
    if avatar in profile_pic_url:
        # Open the file in append mode
        with open("following_avatar.csv", "a", encoding="utf-8") as writefile:
            # Write the userName to the file
            print(userName, file=writefile)

# Close the followinglist after processing all lines
followinglist.close()

#remove unessesary files
os.remove("followinglist.csv")
os.remove("followinglist1.csv")

# Remove empty lines
# Function to remove empty lines from a CSV file
def remove_empty_lines(input_file, output_file):
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        for row in reader:
            # Only write rows that are not empty (i.e., have non-empty elements)
            if any(row):
                writer.writerow(row)

# Paths to your CSV files
list1 = "following_avatar.csv"

# Remove empty lines from both files
remove_empty_lines(list1, "cleaned_" + list1)

#DO THE COMPARE AND EXPORT
# Provide the paths to your input CSV files and the output file
list1 = "cleaned_following_avatar.csv"

# Open the input CSV file
with open('cleaned_following_avatar.csv', 'r') as input_file:
    reader = csv.reader(input_file)
    rows = list(reader)

# Modify the usernames and create a new list with the modified values
modified_rows = []
for row in rows:
    username = row[0]
    modified_username = "https://www.instagram.com/" + username + "/"
    modified_rows.append([modified_username])

# Write the modified usernames to a new CSV file
with open(Prof + '_NO-Avatar.csv', 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(modified_rows)

os.remove("cleaned_following_avatar.csv")
os.remove("following_avatar.csv")