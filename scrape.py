import praw
import csv
import sys

#input your own information
reddit = praw.Reddit(client_id = 'clientID', 
                     client_secret = 'clientSecret',
                     username = 'username',
                     password = 'password',
                     user_agent = 'RedScrape/v1.0/VyNgo')
#open txt document with list of games
gamelist = open("games.txt", "r")
#split .txt document into array 
lines = gamelist.read().split('\n')
#create new file for scraped data
newData = open('sentDat.txt', 'w')

#searches gaming subreddit for submissions that contain game name and returns title and writes to sentDat file
for line in lines:
    for submission in reddit.subreddit('gaming').search(line, sort='top', time_filter='all', limit=1):
        posts= submission.title.encode("utf-8", 'ignore')
        print(posts)
        newData.write(str(posts) + "\n")
        

#close files
gamelist.close()
newData.close()
