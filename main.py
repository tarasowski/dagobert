import snscrape.modules.twitter as snstwitter
import pandas as pd

tweet_list = []

for i, tweet in enumerate(snstwitter.TwitterSearchScraper("from:dagorenouf exclude:replies").get_items()):
    if i > 1000:
        break
    tweet_list.append([tweet.date, tweet.id, tweet.content, tweet.likeCount, tweet.retweetCount, tweet.replyCount, tweet.quoteCount])


df = pd.DataFrame(tweet_list)
df.to_csv("list.csv", index=False)


