import numpy
import praw

from textblob import TextBlob

import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#!pip install flair
# import flair
# flair_sentiment = flair.models.TextClassifier.load('en-sentiment')



reddit = praw.Reddit(client_id='gPkxqeRaHjXmug', \
                     client_secret='xNCTXJQQQIIsIGG3M9UF_DOX2I8', \
                     user_agent='dubhackScrape', \
                     username='scrollAway_throwAway', \
                     password='dubHacks2019')

#subreddits = ['WholesomeMemes', 'meirl', 'politics', 'math', 'learnpython', 'funny', 'gaming', 'Music', 'travel']
subreddits = ['CasualConversation']
for x in subreddits:
    subreddit = reddit.subreddit(x)

    sid = SentimentIntensityAnalyzer()

    avgSubmissionNeg = []
    avgSubmissionPos = []
    avgSubmissionNeu = []
    avgSubmissionPolar = []
    avgSubmissionSubj = []
    for submission in subreddit.hot(limit=8):
        negative = 0
        positive = 0
        neutral = 0
        polar = 0
        subjective = 0

        numComments = 0
        for comment in submission.comments:
            try:
                polarity = sid.polarity_scores(comment.body)
                opinion = TextBlob(comment.body)
                negative += polarity.get('neg')
                neutral += polarity.get('neu')
                positive += polarity.get('pos')

                polar += opinion.polarity
                subjective += opinion.sentiment[1]

                numComments += 1
            except:
                continue;
        if numComments == 0: continue
        negative /= numComments
        neutral /= numComments
        positive /= numComments
        polar /= numComments
        subjective /= numComments
        avgSubmissionNeg.append(negative)
        avgSubmissionNeu.append(neutral)
        avgSubmissionPos.append(positive)
        avgSubmissionPolar.append(polar)
        avgSubmissionSubj.append(subjective)

    subRedditAverage = [0, 0, 0, 0, 0]
    length = len(avgSubmissionNeg)
    for n in range(length):
        subRedditAverage[0] += avgSubmissionNeg[n]
        subRedditAverage[1] += avgSubmissionNeu[n]
        subRedditAverage[2] += avgSubmissionPos[n]
        subRedditAverage[3] += avgSubmissionPolar[n]
        subRedditAverage[4] += avgSubmissionSubj[n]

    print("Info about r/", x)
    print("negativity: ", round(subRedditAverage[0] / length, 3))
    print("neutral: ", round(subRedditAverage[1] / length,3))
    print("positivity: ", round(subRedditAverage[2] / length,3))
    print("Polarization: ", round(subRedditAverage[3] / length, 3))
    print("Subjectivity: ", round(subRedditAverage[4] / length, 3), '\n')

