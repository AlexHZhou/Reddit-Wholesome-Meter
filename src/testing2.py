import numpy
import praw

from textblob import TextBlob

import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#!pip install flair
import flair
flair_sentiment = flair.models.TextClassifier.load('en-sentiment')

reddit = praw.Reddit(client_id='gPkxqeRaHjXmug', \
                     client_secret='xNCTXJQQQIIsIGG3M9UF_DOX2I8', \
                     user_agent='dubhackScrape', \
                     username='scrollAway_throwAway', \
                     password='dubHacks2019')

subreddit = reddit.subreddit('WholesomeMemes')

sid = SentimentIntensityAnalyzer()

for submission in subreddit.hot(limit=1):
    for comment in submission.comments:
        opinion = TextBlob(comment.body)
        s = flair.data.Sentence(comment.body)
        flair_sentiment.predict(s)
        total_sentiment = s.labels
        print(total_sentiment)
        print(comment.body)
        print(sid.polarity_scores(comment.body))
        print(opinion.sentiment)
        print("\n")