import glob
import twint
import time
import pandas as pd
# need to include these two lines if running this in Jupyter notebook cell
# import nest_asyncio
# nest_asyncio.apply()

twitter_user_handles = ['bbchealth', 'foxnewshealth','GdnHealthcare',
                        'KHNews', 'latimeshealth', 'NBCNewshealth',
                        'NPRHealth', 'NYTHealth', 'Reuters_Health',
                        'USNewsHealth', 'WSJHealth', 'TIMEHealth',
                        'HarvardHealth']
time_start = time.time()

# loop through each account using same configuration
for username in twitter_user_handles:
    c = twint.Config()
    c.Lang = "en"
    c.Username = username
    c.Since = '2014-01-01'
    c.Until = '2020-03-28'
    c.Pandas = True
    c.Store_pandas = True
    c.Pandas_au = True
    c.Pandas_clean = False
    twint.run.Search(c)   # run search

# store in data frame
tweets_df = twint.storage.panda.Tweets_df

print('Tweet Scraping done! Time elapsed: {} seconds'.format(time.time()-time_start))
print('{} tweets scraped'.format(len(tweets_df)))

tweets_df.to_csv(r'data/health_tweets.csv', index=False, header=True)

# merge multiple csvs together if needed
# data_dir = 'data/'
# tweets_df = pd.concat([pd.read_csv(file) for file in glob.glob(data_dir+'*.csv')], ignore_index=True)
# tweets_df.to_csv(r'data/health_tweets.csv', index=False, header=True)