# Scraper https://chromewebstore.google.com/detail/ig-exporter-scraper-expor/akbfineiddmgpdlkalpcfblholabkeen
# Need the 2 lists from the scraper

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

# Pick profile 
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
    #Let's split the line into an array called "fields" using the ";" as a separator
    fields = line.split(";")
    #and let's extract the data:
    followed_by_viewer = fields[0]
    fullName = fields[1]
    id = fields[2]
    isVerified = fields[3]
    profile_pic_url = fields[4]
    requested_by_viewer = fields[5]
    userName = fields[6]

    writefile = open("following_uns.csv","a",encoding="utf-8")
    print(userName, file=writefile)
    writefile.close()

followinglist.close()

#FOLLOWERS 
followersCSV = Prof + '_' + 'followers.csv'
followersCSV_withoutQuotes = 'followerlist.csv'
remove_double_quotes(followersCSV, followersCSV_withoutQuotes)

#remove 1st splitlines
with open("followerlist.csv","r",encoding="utf-8") as arxikofollower:
    data = arxikofollower.read().splitlines(True)
with open("followerlist1.csv", "w",encoding="utf-8") as telikofollower:
    telikofollower.writelines(data[1:])
#Accessing a csv file epistoles1 is like epistoles without the 1st line
followerlist = open("followerlist1.csv","r",encoding="utf-8")

for line in followerlist:
    #Let's split the line into an array called "fields" using the ";" as a separator
    fields = line.split(";")
    #and let's extract the data:
    followed_by_viewer = fields[0]
    fullName = fields[1]
    id = fields[2]
    isVerified = fields[3]
    profile_pic_url = fields[4]
    requested_by_viewer = fields[5]
    userName = fields[6]

    writefile = open("follower_uns.csv","a",encoding="utf-8")
    print(userName, file=writefile)
    writefile.close()

followerlist.close()

#remove unessesary files
os.remove("followinglist.csv")
os.remove("followinglist1.csv")
os.remove("followerlist.csv")
os.remove("followerlist1.csv")

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
list1 = "following_uns.csv"
list2 = "follower_uns.csv"

# Remove empty lines from both files
remove_empty_lines(list1, "cleaned_" + list1)
remove_empty_lines(list2, "cleaned_" + list2)

#DO THE COMPARE AND EXPORT
# Provide the paths to your input CSV files and the output file
list1 = "cleaned_following_uns.csv"
list2 = "cleaned_follower_uns.csv"
output_file = "UN_nonfollowers.csv"

def check_usernames(list1, list2, output_file):
    with open(list1, 'r') as file1, open(list2, 'r') as file2, open(output_file, 'w', newline='') as output:
        reader1 = csv.reader(file1)
        reader2 = csv.reader(file2)
        writer = csv.writer(output)

        usernames1 = set(row[0] for row in reader1)
        usernames2 = set(row[0] for row in reader2)

        missing_usernames = usernames1 - usernames2

        for username in missing_usernames:
            writer.writerow([username])

check_usernames(list1, list2, output_file)


#remove unessesary files
os.remove("following_uns.csv")
os.remove("follower_uns.csv")
os.remove("cleaned_following_uns.csv")
os.remove("cleaned_follower_uns.csv")

# Open the input CSV file
with open('UN_nonfollowers.csv', 'r') as input_file:
    reader = csv.reader(input_file)
    rows = list(reader)

# Modify the usernames and create a new list with the modified values
modified_rows = []
for row in rows:
    username = row[0]
    modified_username = "https://www.instagram.com/" + username + "/"
    modified_rows.append([modified_username])

# Write the modified usernames to a new CSV file
with open(Prof + '_NON-followers.csv', 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(modified_rows)

os.remove("UN_nonfollowers.csv")