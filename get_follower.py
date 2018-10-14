"""
作成者：dapu_shk
機能：特定ユーザーのフォロワー(ID)を1万人分取得する
"""
import tweepy

#自分で取得したKEYとSECRETを入れる
CONSUMER_KEY = '------------'
CONSUMER_SECRET = '------------'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
api = tweepy.API(auth)

#フォロワーを取得したいユーザのIDを入れる
followers_ids = tweepy.Cursor(api.followers_ids, '==============').items(10000)

for followers_id in followers_ids:

    with open('==============.txt', 'a') as f:
        f.write(str(followers_id) + '\n')

f.close