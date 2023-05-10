import praw
import pandas as pd

print("running web scrapper...")

stories = []

reddit_read_only = praw.Reddit(client_id="jLUlVg8u0M_7UCebmhBHVw",
                               client_secret="Rwk3mUteGF_F5HkVAFGnK-TfF8y6Sw",
                               user_agent="RobertTAS")

subreddit = reddit_read_only.subreddit("worldnews")

for post in subreddit.hot(limit=2):
    print("scraping story...")
    stories.append(post.title)

stories.pop(0)

print("opening text file...")
file = open("stories.txt", "w")

for story in stories:
    print("writing story to file...")
    file.write(story)
    file.write("\n")

file.close()
print("scraping complete...")