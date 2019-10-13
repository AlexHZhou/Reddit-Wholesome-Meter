#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy
import praw

import warnings
warnings.filterwarnings("ignore")

import matplotlib.pyplot as plt

from textblob import TextBlob

import nltk
#nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer


reddit = praw.Reddit(client_id='gPkxqeRaHjXmug',                      client_secret='xNCTXJQQQIIsIGG3M9UF_DOX2I8',                      user_agent='dubhackScrape',                      username='scrollAway_throwAway',                      password='dubHacks2019')

#subreddits = ['WholesomeMemes', 'meirl', 'politics', 'math', 'learnpython', 'funny', 'gaming', 'Music', 'travel']
print('What subreddit would you like to analyze the comments of? Examples: food, wholesomeMemes, learnPython')
subredditInput = input()
print('Thank you, please wait roughly 10 seconds for results.')
subreddits = [subredditInput]
for x in subreddits:
    
    subreddit = reddit.subreddit(x)

    sid = SentimentIntensityAnalyzer()
    
    numTotalComments = 0

    avgSubmissionNeg = []
    avgSubmissionPos = []
    avgSubmissionNeu = []
    avgSubmissionPolar = []
    avgSubmissionSubj = []
    for submission in subreddit.top(limit=8):
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
        numTotalComments = numComments + numTotalComments

    subRedditAverage = [0, 0, 0, 0, 0]
    length = len(avgSubmissionNeg)
    for n in range(length):
        subRedditAverage[0] += avgSubmissionNeg[n]
        subRedditAverage[1] += avgSubmissionNeu[n]
        subRedditAverage[2] += avgSubmissionPos[n]
        subRedditAverage[3] += avgSubmissionPolar[n]
        subRedditAverage[4] += avgSubmissionSubj[n]
    
    neg = round(subRedditAverage[0] / length, 3)
    pos = round(subRedditAverage[2] / length,3)
    neut = 1 - neg - pos
    sizes = [neg, neut, pos]
    colors = ['red', 'khaki', 'yellowgreen']

    labels = 'Negative', 'Neutral', 'Positive'
    # Plot
    
    print('This chart shows the percentage of ' + str(numTotalComments) + " comments from the top 8 posts of r/" + subredditInput + ".")
    
    fig = plt.figure("r/" + subredditInput)
    
    plt.pie(sizes, labels=labels, colors=colors, shadow=False, startangle=0,
           autopct='%1.1f%%', textprops={'fontsize': 14})

    plt.axis('equal')
    plt.show()


# In[ ]:




