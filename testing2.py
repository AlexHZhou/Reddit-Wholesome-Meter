import numpy
import praw
from textblob import TextBlob


reddit = praw.Reddit(client_id='gPkxqeRaHjXmug', \
                     client_secret='xNCTXJQQQIIsIGG3M9UF_DOX2I8', \
                     user_agent='dubhackScrape', \
                     username='scrollAway_throwAway', \
                     password='dubHacks2019')

subreddit = reddit.subreddit('WholesomeMemes')

for submission in subreddit.top(limit=1):
    for comment in submission.comments:
        opinion = TextBlob(comment.body)
        print(opinion.sentiment)
        print("\n")