import praw
import pandas as pd

print("running web scrapper...")

stories = []

reddit_read_only = praw.Reddit(client_id="jLUlVg8u0M_7UCebmhBHVw",
                               client_secret="Rwk3mUteGF_F5HkVAFGnK-TfF8y6Sw",
                               user_agent="RobertTAS")

subreddit = reddit_read_only.subreddit("worldnews")

for post in subreddit.hot(limit=25):
    stories.append(post.title)

stories.pop(0)

for story in stories:
    print(story)